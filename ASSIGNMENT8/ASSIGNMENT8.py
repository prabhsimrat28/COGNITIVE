import numpy as np
import pandas as pd

# Load the dataset (using Pandas for convenience)
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
df = pd.read_csv(url, names=columns)

# Convert categorical species names to numerical labels
df["species"] = df["species"].astype("category").cat.codes  # Converts classes to {0,1,2}

# Extract features and labels
X = df.iloc[:, :-1].values  # Features
y = df.iloc[:, -1].values   # Labels (0,1,2 for species)

# Convert multi-class problem into a binary classification (for simplicity, classify setosa vs. non-setosa)
y_binary = (y == 0).astype(int)  # Convert to 0 or 1 (setosa = 1, others = 0)

# Normalize features for better convergence
X = (X - X.mean(axis=0)) / X.std(axis=0)

# Add bias term (column of ones)
X = np.c_[np.ones(X.shape[0]), X]

# Train-Test Split (80-20)
np.random.seed(42)
indices = np.random.permutation(X.shape[0])
train_size = int(0.8 * X.shape[0])
train_idx, test_idx = indices[:train_size], indices[train_size:]

X_train, X_test = X[train_idx], X[test_idx]
y_train, y_test = y_binary[train_idx], y_binary[test_idx]

# Sigmoid function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Cost function (Binary Cross-Entropy)
def compute_cost(X, y, weights):
    m = len(y)
    h = sigmoid(X @ weights)
    return (-1/m) * np.sum(y * np.log(h) + (1 - y) * np.log(1 - h))

# Gradient Descent
def gradient_descent(X, y, weights, alpha, epochs):
    m = len(y)
    cost_history = []

    for _ in range(epochs):
        h = sigmoid(X @ weights)
        gradient = (1/m) * (X.T @ (h - y))
        weights -= alpha * gradient
        cost_history.append(compute_cost(X, y, weights))

    return weights, cost_history

# Initialize weights
weights = np.zeros(X_train.shape[1])

# Hyperparameters
alpha = 0.1   # Learning rate
epochs = 2000  # Iterations

# Train the model
weights, cost_history = gradient_descent(X_train, y_train, weights, alpha, epochs)

# Predictions
y_pred = sigmoid(X_test @ weights) >= 0.5
accuracy = np.mean(y_pred == y_test) * 100

print(f"Model Accuracy: {accuracy:.2f}%")
