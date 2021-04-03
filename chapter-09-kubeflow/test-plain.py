import requests
from keras_image_helper import create_preprocessor

preprocessor = create_preprocessor('xception', target_size=(299, 299))


url = 'https://clothing-model.default.kubeflow.mlbookcamp.com/v1/models/clothing-model:predict'

image_url = "http://bit.ly/mlbookcamp-pants"
X = preprocessor.from_url(image_url)

data = {
    "instances": X.tolist()
}

resp = requests.post(url, json=data)

results = resp.json()
pred = results['predictions'][0]

labels = [
    'dress',
    'hat',
    'longsleeve',
    'outwear',
    'pants',
    'shirt',
    'shoes',
    'shorts',
    'skirt',
    't-shirt'
]

result = {c: p for c, p in zip(labels, pred)}
print(result)
