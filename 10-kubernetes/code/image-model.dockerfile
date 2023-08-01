FROM tensorflow/serving:2.7.0

COPY clothing-model /models/clothing-model/1
ENV MODEL_NAME="clothing-model"