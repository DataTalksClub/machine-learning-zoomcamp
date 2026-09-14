from __future__ import annotations

import json
import os
from io import BytesIO
from pathlib import Path
from urllib import request

import numpy as np
import onnxruntime as ort
from PIL import Image


MODEL_PATH = Path(
    os.getenv("MODEL_PATH", Path(__file__).with_name("hair_classifier_v1.onnx"))
)
session = ort.InferenceSession(
    str(MODEL_PATH),
    providers=["CPUExecutionProvider"],
)
INPUT_NAME = session.get_inputs()[0].name
OUTPUT_NAME = session.get_outputs()[0].name


def download_image(url: str) -> Image.Image:
    with request.urlopen(url, timeout=30) as response:
        return Image.open(BytesIO(response.read())).convert("RGB")


def prepare_image(image: Image.Image) -> np.ndarray:
    image = image.resize((200, 200), Image.Resampling.BILINEAR)
    array = np.asarray(image, dtype=np.float32) / 255.0
    array = (array - np.array([0.485, 0.456, 0.406], dtype=np.float32)) / np.array(
        [0.229, 0.224, 0.225], dtype=np.float32
    )
    return np.transpose(array, (2, 0, 1))[None, ...]


def predict_image_url(image_url: str) -> dict[str, object]:
    image = download_image(image_url)
    tensor = prepare_image(image)
    output = session.run([OUTPUT_NAME], {INPUT_NAME: tensor})[0]
    probability = float(output.reshape(-1)[0])
    return {
        "straight_probability": round(probability, 6),
        "straight": probability >= 0.5,
    }


def lambda_handler(event: dict, context: object) -> dict[str, object]:
    del context
    payload = event
    if isinstance(event.get("body"), str):
        payload = json.loads(event["body"])

    result = predict_image_url(payload["image_url"])
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(result),
    }
