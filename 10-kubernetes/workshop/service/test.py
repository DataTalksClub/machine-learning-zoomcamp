import requests

url = 'http://localhost:8080/predict'

request = {
    "url": "http://bit.ly/mlbookcamp-pants"
}

response = requests.post(url, json=request)
result = response.json()

print(f"Top prediction: {result['top_class']} ({result['top_probability']:.2%})")
print(f"\nAll predictions:")
for cls, prob in result['predictions'].items():
    print(f"  {cls:12s}: {prob:.2%}")
