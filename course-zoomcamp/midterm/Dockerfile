FROM agrigorev/zoomcamp-model:3.8.12-slim

RUN pip install --upgrade pip 

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 9696

ENTRYPOINT [ "gunicorn", "--bind", "0.0.0.0:9696", "predict:app" ]