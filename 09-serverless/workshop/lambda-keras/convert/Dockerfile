FROM python:3.13.5-slim

ARG COMMIT_ID

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    build-essential \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

RUN pip install git+https://github.com/onnx/tensorflow-onnx.git@${COMMIT_ID}
RUN pip install tensorflow

WORKDIR /models

CMD ["bash"]
