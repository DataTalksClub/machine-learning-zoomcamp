## Running TF-Serving locally

Get the model from Chapter 7:

```bash
wget https://github.com/alexeygrigorev/mlbookcamp-code/releases/download/chapter7-model/xception_v4_large_08_0.894.h5
```

Convert it to `saved_model`:

```bash
python convert.py
```

Run TF-Serving with Docker:

```bash
docker run -it --rm \
    -p 8500:8500 \
    -v "$(pwd)/clothing-model:/models/clothing-model/1" \
    -e MODEL_NAME=clothing-model \
    tensorflow/serving:2.3.0
```

Now open [09-image-preparation.ipynb](09-image-preparation.ipynb) and
execute the code there to test it
