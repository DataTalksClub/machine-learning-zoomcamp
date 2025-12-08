import time
import requests

from concurrent.futures import ThreadPoolExecutor, as_completed


url = 'http://localhost:30080/predict'

request_data = {
    "url": "http://bit.ly/mlbookcamp-pants"
}

def send_request(_):
    try:
        response = requests.post(url, json=request_data, timeout=5)
        return response.status_code
    except Exception as e:
        return f"Error: {e}"


print("Starting load test...")

print("Watch HPA with: kubectl get hpa -w")
print("Watch pods with: kubectl get pods -w")

num_requests = 1000
concurrent_workers = 50


print(f"Sending {num_requests} requests with {concurrent_workers} concurrent workers")
print()

start_time = time.time()


with ThreadPoolExecutor(max_workers=concurrent_workers) as executor:
    futures = [executor.submit(send_request, i) for i in range(num_requests)]
    results = [future.result() for future in as_completed(futures)]


end_time = time.time()
duration = end_time - start_time

success_count = sum(1 for r in results if r == 200)
error_count = len(results) - success_count


print("Load test complete!")

print(f"Duration: {duration:.2f} seconds")
print(f"Requests per second: {len(results)/duration:.2f}")
print(f"Successful requests: {success_count}")
print(f"Failed requests: {error_count}")
print()