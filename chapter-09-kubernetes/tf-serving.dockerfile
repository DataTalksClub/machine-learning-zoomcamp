# FROM tensorflow/serving:2.3.0-gpu
FROM tensorflow/serving:2.3.0

ENV MODEL_NAME clothing-model
COPY clothing-model /models/clothing-model/1
