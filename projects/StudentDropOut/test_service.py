"""Send the example students to a running service and print the answers.

Usage:
    python test_service.py                       # local service on port 9696
    python test_service.py http://<host>:<port>  # any other deployment
"""

import json
import sys
from pathlib import Path

import requests

EXAMPLES_DIR = Path(__file__).parent / "examples"


def main(base_url: str) -> None:
    health = requests.get(f"{base_url}/health", timeout=10)
    health.raise_for_status()
    print(f"GET  {base_url}/health -> {health.json()}")

    for path in sorted(EXAMPLES_DIR.glob("*.json")):
        student = json.loads(path.read_text())
        response = requests.post(f"{base_url}/predict", json=student, timeout=10)
        response.raise_for_status()
        print(f"POST {base_url}/predict ({path.name}) -> {response.json()}")


if __name__ == "__main__":
    main(sys.argv[1].rstrip("/") if len(sys.argv) > 1 else "http://127.0.0.1:9696")
