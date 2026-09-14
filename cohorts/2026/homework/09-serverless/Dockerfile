FROM public.ecr.aws/lambda/python:3.13@sha256:0fc65c4c9bace18ce7cb5b670119b847140a9c1c45f2b24d06ce4e35bef0a9be

COPY requirements-lambda.txt ${LAMBDA_TASK_ROOT}/
RUN python -m pip install --no-cache-dir -r ${LAMBDA_TASK_ROOT}/requirements-lambda.txt \
    --target ${LAMBDA_TASK_ROOT}

COPY lambda_function.py hair_classifier_v1.onnx hair_classifier_v1.onnx.data ${LAMBDA_TASK_ROOT}/

CMD ["lambda_function.lambda_handler"]
