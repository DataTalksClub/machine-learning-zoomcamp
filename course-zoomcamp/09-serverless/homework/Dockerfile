FROM agrigorev/zoomcamp-cats-dogs-lambda:v2

RUN pip install keras-image-helper
RUN pip install https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.7.0-cp38-cp38-linux_x86_64.whl

COPY homework.py .
ENV MODEL_NAME=cats-dogs-v2.tflite

CMD [ "homework.lambda_handler" ]