## Homework 9: Serverless Deep Learning

In this homework we package the hair classifier behind an AWS Lambda-compatible
handler and run it locally in a Lambda container. The model and sample image
are frozen by SHA-256 checksums. Use the provided reference ONNX model for the
graded inference questions; do not export a different local checkpoint from a
stochastic training run.

## Download the reference assets

Run these commands in this directory:

```bash
PREFIX="https://github.com/alexeygrigorev/large-datasets/releases/download/hairstyle"
curl -fL -o hair_classifier_v1.onnx.data "${PREFIX}/hair_classifier_v1.onnx.data"
curl -fL -o hair_classifier_v1.onnx "${PREFIX}/hair_classifier_v1.onnx"
curl -fL -o sample.jpeg \
  "https://habrastorage.org/webt/yf/_d/ok/yf_dokzqy3vcritme8ggnzqlvwa.jpeg"
```

Verify the files against `asset_manifest.json`:

```bash
sha256sum hair_classifier_v1.onnx hair_classifier_v1.onnx.data sample.jpeg
```

The ONNX file and its external-data file must remain next to each other with
these exact names. The sample image is 1024x1024 RGB JPEG. The manifest records
all three checksums and the model graph interface.

Install the pinned local dependencies if you want to run the handler directly:

```bash
python -m pip install -r requirements.txt
```

## Question 1 — look at the ONNX graph

Load the model with ONNX Runtime and look at `session.get_inputs()` and
`session.get_outputs()`. What is the output node name?

- `output`
- `sigmoid`
- `softmax`
- `prediction`

The input node is `input` and has shape `(batch, 3, 200, 200)`. The output is a
single float: the probability of the `straight` class (`straight=1`).

## Image preprocessing

Use the same preprocessing as the fixed deep-learning reference setup:

```python
from io import BytesIO
from urllib import request

import numpy as np
from PIL import Image


def download_image(url):
    with request.urlopen(url, timeout=30) as response:
        return Image.open(BytesIO(response.read())).convert("RGB")


def prepare_image(image):
    image = image.resize((200, 200), Image.Resampling.BILINEAR)
    array = np.asarray(image, dtype=np.float32) / 255.0
    array = (array - np.array([0.485, 0.456, 0.406], dtype=np.float32)) / np.array(
        [0.229, 0.224, 0.225], dtype=np.float32
    )
    return np.transpose(array, (2, 0, 1))[None, ...]
```

The interpolation method, RGB conversion, channel order, normalization, and
`float32` conversion are part of the interface. In 2025 the interpolation was
left implicit in one homework and set to `NEAREST` in the next one, which made
the first pixel and model output disagree. Here both modules explicitly use
bilinear resizing.

## Question 2 — target size

What target size does `prepare_image` use?

- `64x64`
- `128x128`
- `200x200`
- `256x256`

## Question 3 — normalized input

Download `sample.jpeg`, run `prepare_image`, and report the first value of the
R channel (`tensor[0, 0, 0, 0]`) rounded to three decimal places. The grader
accepts an absolute error of `0.01`.

## Question 4 — local ONNX inference

Run the session with:

```python
import onnxruntime as ort

session = ort.InferenceSession(
    "hair_classifier_v1.onnx",
    providers=["CPUExecutionProvider"],
)
output = session.run(
    ["output"],
    {"input": prepare_image(download_image(SAMPLE_URL))},
)[0]
```

Report the output probability rounded to three decimal places. The grader
accepts an absolute error of `0.02`. Because the model, image, and preprocessing
are checksummed and CPU inference is used, this is no longer a choice between
platform-dependent options.

## Lambda handler

The provided `lambda_function.py` implements the complete handler. Read it and
test it locally with:

```bash
python smoke_test.py
```

The handler accepts either a direct event or an API Gateway-style event. The
request payload is:

```json
{
  "image_url": "https://habrastorage.org/webt/yf/_d/ok/yf_dokzqy3vcritme8ggnzqlvwa.jpeg"
}
```

It returns HTTP status `200` and a JSON body containing
`straight_probability` and the boolean `straight` prediction.

## Container

Build the Lambda-compatible image from the checked-in Dockerfile:

```bash
docker build -t mlzoomcamp-2026-serverless .
docker run --rm -p 9000:8080 mlzoomcamp-2026-serverless
```

Invoke it from another terminal:

```bash
curl -s \
  -XPOST 'http://localhost:9000/2015-03-31/functions/function/invocations' \
  -H 'Content-Type: application/json' \
  -d '{"image_url":"https://habrastorage.org/webt/yf/_d/ok/yf_dokzqy3vcritme8ggnzqlvwa.jpeg"}'
```

The Dockerfile uses the AWS Lambda Python 3.13 base image, installs the
exact runtime dependencies from `requirements-lambda.txt`, and copies the same
checksummed ONNX pair. It does not substitute an empty or different model.

## Question 5 — look at the Lambda configuration

Which runtime base image is declared in the Dockerfile?

- `public.ecr.aws/lambda/python:3.9`
- `public.ecr.aws/lambda/python:3.11`
- `public.ecr.aws/lambda/python:3.13`
- `python:3.13-slim-bookworm`

The local image's displayed size is intentionally not graded: it depends on
architecture, Docker version, and cached layers.

## Question 6 — invoke the container

Inspect the JSON string in the Lambda response body and report
`straight_probability` rounded to three decimal places. The grader accepts an
absolute error of `0.02`. It must match Question 4 because both paths use the
same model, image, preprocessing, and CPU execution provider.

## Optional AWS deployment

You may publish the image to ECR, create a Lambda function from it, and expose
it through API Gateway. Use an immutable image digest when deploying. The AWS
step is optional and not graded; the local container invocation is the
reproducible local path.

## Submit the results

Submit the results here:
<https://courses.datatalks.club/ml-zoomcamp-2026/homework/hw09>.

Numeric answers use the precision and tolerance stated in each question. There
numeric answers use the tolerance stated in each question.
