from api.app import app

client = app.test_client()
response = client.post("/predict", json={"features": [5.1, 3.5, 1.4, 0.2]})

assert response.status_code == 200
assert response.json["prediction"] == 0
print("Test passed!")
