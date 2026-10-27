"""Test the /predict API without starting the Flask server.

Run this test from the project folder with: python test_api.py
"""

from api.app import app

client = app.test_client()
response = client.post(
    "/predict",
    json={"features": [5.1, 3.5, 1.4, 0.2]},
)

# These Iris features should produce prediction class 0.
assert response.status_code == 200
assert response.get_json() == {"prediction": 0}

print("API test passed")
