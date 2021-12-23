import kserve
from typing import List, Dict

from keras_image_helper import create_preprocessor


class ImageTransformer(kserve.KFModel):
    def __init__(self, name: str, predictor_host: str):
        super().__init__(name)
        self.predictor_host = predictor_host
        self.preprocessor = create_preprocessor('xception', target_size=(299, 299))
        self.classes = [
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

    def prepare_input(self, url: str) -> List:
        X = self.preprocessor.from_url(url)
        return X[0].tolist()

    def preprocess(self, request: Dict) -> Dict:
        result = []

        for url in request['instances']:
            row = self.prepare_input(url)
            result.append(row)

        return {'instances': result}

    def postprocess(self, response: Dict) -> Dict:
        result = []

        for prediction in response['predictions']:
            output = dict(zip(self.classes, prediction))
            result.append(output)

        return {'predictions': result}

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(parents=[kserve.kfserver.parser])
    parser.add_argument("--predictor_host", help="The URL for the model predict function", required=True)
    parser.add_argument("--model_name", help="The name of the model", required=True)

    args, _ = parser.parse_known_args()

    model_name = args.model_name
    host = args.predictor_host

    tranformer = ImageTransformer(model_name, predictor_host=host)

    server = kserve.KFServer()
    server.start(models=[tranformer])
