import os
import pickle
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

def train_model():
    print("Loading Iris dataset...")
    iris = load_iris()
    X, y = iris.data, iris.target

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("Initializing RandomForestClassifier...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)

    print("Training the model...")
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model accuracy: {accuracy:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=iris.target_names))

    # Define model save path
    model_path = "model.pkl"
    print(f"Saving the model to {model_path}...")
    with open(model_path, "wb") as f:
        pickle.dump(model, f)
    print("Model saved successfully!")

if __name__ == "__main__":
    train_model()
