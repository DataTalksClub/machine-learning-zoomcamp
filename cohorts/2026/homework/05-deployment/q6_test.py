from __future__ import annotations

import json
import sys
from urllib.request import Request, urlopen


url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:9696/predict"
client = {
    "lead_source": "organic_search",
    "industry": "technology",
    "employment_status": "employed",
    "location": "europe",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0,
    "interaction_count": 7,
    "lead_score": 0.74,
}
request = Request(
    url,
    data=json.dumps(client).encode("utf-8"),
    headers={"Content-Type": "application/json"},
    method="POST",
)

with urlopen(request) as response:
    result = json.load(response)

assert set(result) == {"conversion_probability", "conversion"}
assert 0 <= result["conversion_probability"] <= 1
assert isinstance(result["conversion"], bool)
print(result)
