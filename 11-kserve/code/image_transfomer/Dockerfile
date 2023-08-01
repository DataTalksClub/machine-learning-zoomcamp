FROM python:3.8.12-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY "image_tranformer.py" .

ENTRYPOINT ["python", "image_tranformer.py"]