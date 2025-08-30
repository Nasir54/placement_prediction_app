# src/perceptron_model.py
import pandas as pd
import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os

def load_data_and_train():
    """
    Load data, train perceptron model, and save both model and scaler
    """
    print("Loading data from data/placement.csv...")
    df = pd.read_csv('data/placement.csv')
    
    print("Data loaded successfully!")
    print(f"Dataset shape: {df.shape}")
    print(f"Columns: {df.columns.tolist()}")
    
    # Remove the index column if it exists
    if 'Unnamed: 0' in df.columns:
        df = df.drop(columns=['Unnamed: 0'])
        print("Removed index column 'Unnamed: 0'")
    
    # Use the correct column names
    X = df[['cgpa', 'iq']]    # Feature columns
    y = df['placement']       # Target column
    
    print(f"Features: {X.columns.tolist()}")
    print(f"Target: {y.name}")
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Scale the features
    print("Scaling features...")
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Create and train model
    print("Training Perceptron model...")
    model = Perceptron()
    model.fit(X_train_scaled, y_train)
    
    # Make predictions and calculate accuracy
    y_pred = model.predict(X_test_scaled)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model accuracy: {accuracy:.4f}")
    
    # Save the model and scaler
    os.makedirs('model', exist_ok=True)
    
    joblib.dump(model, 'model/model.joblib')
    joblib.dump(scaler, 'model/scaler.joblib')
    print("Model and scaler saved to model/ folder")
    
    return model, scaler, accuracy

def load_trained_model():
    """
    Load the pre-trained model and scaler
    """
    try:
        model = joblib.load('model/model.joblib')
        scaler = joblib.load('model/scaler.joblib')
        print("Successfully loaded pre-trained model and scaler")
        return model, scaler
    except FileNotFoundError:
        print("No pre-trained model found. Please train first.")
        return None, None

if __name__ == "__main__":
    # Check if model already exists
    model, scaler = load_trained_model()
    
    if model is None:
        # Train new model if none exists
        model, scaler, accuracy = load_data_and_train()
    else:
        print("Using existing trained model")
