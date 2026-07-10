import os
import pickle
import streamlit as st

st.set_page_config(page_title="Iris Classifier", layout="centered")

st.title("🌸 Iris Flower Classifier")
st.write("A simple machine learning UI to predict Iris flower species.")

# Load the trained model
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")

if not os.path.exists(model_path):
    st.error("Model file `model.pkl` not found! Please run `python train.py` first.")
else:
    with open(model_path, "rb") as f:
        model = pickle.load(f)

    # Input forms for the flower measurements
    st.subheader("Enter Flower Characteristics:")
    
    sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.1, 0.1)
    sepal_width = st.slider("Sepal Width (cm)", 2.0, 5.0, 3.5, 0.1)
    petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 1.4, 0.1)
    petal_width = st.slider("Petal Width (cm)", 0.1, 3.0, 0.2, 0.1)

    # Predict button
    if st.button("Predict Species", type="primary"):
        features = [sepal_length, sepal_width, petal_length, petal_width]
        prediction = model.predict([features])[0]
        
        # Target classes
        class_names = ["Setosa", "Versicolor", "Virginica"]
        predicted_class = class_names[prediction]
        
        # Display the result
        st.success(f"Predicted Species: **{predicted_class}** (Class {prediction})")
