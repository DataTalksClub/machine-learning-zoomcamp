FROM public.ecr.aws/lambda/python:3.13

RUN pip install onnxruntime keras-image-helper==0.0.2

ARG MODEL_NAME=clothing_classifier_mobilenet_v2_latest.onnx
ENV MODEL_NAME=${MODEL_NAME}

COPY ${MODEL_NAME} ${MODEL_NAME}

COPY lambda_function.py ./

CMD ["lambda_function.lambda_handler"]