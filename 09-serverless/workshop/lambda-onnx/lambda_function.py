import os

import numpy as np
import onnxruntime as ort
from keras_image_helper import create_preprocessor


model_name = os.getenv("MODEL_NAME", "clothing-model-new.onnx")


def preprocess_pytorch_style(X):
    # X: shape (1, 299, 299, 3), dtype=float32, values in [0, 255]
    X = X / 255.0

    mean = np.array([0.485, 0.456, 0.406]).reshape(1, 3, 1, 1)
    std = np.array([0.229, 0.224, 0.225]).reshape(1, 3, 1, 1)

    # Convert NHWC → NCHW
    # from (batch, height, width, channels) → (batch, channels, height, width)
    X = X.transpose(0, 3, 1, 2)  

    # Normalize
    X = (X - mean) / std

    return X.astype(np.float32)


preprocessor = create_preprocessor(
    preprocess_pytorch_style,
    target_size=(224, 224)
)



session = ort.InferenceSession(
    model_name, providers=["CPUExecutionProvider"]
)
input_name = session.get_inputs()[0].name
output_name = session.get_outputs()[0].name

classes = [
    "dress",
    "hat",
    "longsleeve",
    "outwear",
    "pants",
    "shirt",
    "shoes",
    "shorts",
    "skirt",
    "t-shirt",
]


def predict(url):
    X = preprocessor.from_url(url)
    result = session.run([output_name], {input_name: X})
    float_predictions = result[0][0].tolist()
    return dict(zip(classes, float_predictions))


def lambda_handler(event, context):
    url = event["url"]
    result = predict(url)
    return result
