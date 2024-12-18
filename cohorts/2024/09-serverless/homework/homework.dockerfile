FROM public.ecr.aws/lambda/python:3.10

COPY model_2024_hairstyle_v2.tflite .

RUN pip install numpy==1.23.1
