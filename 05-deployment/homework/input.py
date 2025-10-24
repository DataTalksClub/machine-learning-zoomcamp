import requests

url = "http://localhost:9696/predict"

client = {
    "lead_source": "organic_search",
    "number_of_courses_viewed": 4,
    "annual_income": 0
}

response = requests.post(url, json=client)
probability = response.json()
print("response:", probability)