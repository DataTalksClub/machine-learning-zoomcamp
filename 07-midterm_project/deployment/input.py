import requests

url = "http://localhost:9696/predict"

bacteria = {
  "growth_rate": 0.1338005,
  "peaks": 23,
  "circularity": 0.96578,
  "eccentricity": 0.18561,
  "RGB_mean_1": 246.7854,
  "RGBt_mean_2": 225.925,
  "RGBt_mean_3": 217.3063,
  "RGBt_std_1": 22.9483,
  "RGBt_std_2": 31.6416,
  "RGBt_std_3": 36.2281,
  "Lab_mean_1": 89.0539,
  "Lab_mean_2": 8.08953,
  "Lab_mean_3": 10.7003,
  "Lab_std_1": 11.1602,
  "Lab_std_2": 6.90168,
  "Lab_std_3": 8.14749,
  "Labt_mean_1": 91.3267,
  "Labt_mean_2": 6.5164,
  "Labt_mean_3": 7.15765,
  "Labt_std_1": 10.7217,
  "Labt_std_2": 4.70734,
  "Labt_std_3": 7.27739,
}

response = requests.post(url, json=bacteria)
activity = response.json()
print("activity:", activity)