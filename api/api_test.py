# test_api.py
import requests

# Test classification
response = requests.get(
    "http://127.0.0.1:8000/classify",
    params={"text": "This is a sample document about technology and AI"}
)
print(response.json())

print("Status:", response.status_code)
print("Response:", response.text)


