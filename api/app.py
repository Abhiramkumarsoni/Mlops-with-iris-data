import os
import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the trained model
#model_path = os.path.join(os.path.dirname(__file__), "../model.pkl")
model_path='model.pkl'
with open(model_path, "rb") as f:
    model = pickle.load(f)

@app.route("/predict", methods=["POST"])
def predict():
    # Extract features list from request JSON
    features = request.json["features"]
    
    # Predict directly using scikit-learn (no numpy required for list input)
    prediction = model.predict([features])[0]
    
    return jsonify({"prediction": int(prediction)})

if __name__ == "__main__":
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", "5000"))
    app.run(host=host, port=port)



# http://localhost:5000/predict
# {"features": [5.1, 3.5, 1.4, 0.2]}

"""curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
"""