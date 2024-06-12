# -*- coding: utf-8 -*-
"""Logistic_regression_from_scratch.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wmRLjKqUvrpLQYEczq21RCB1xM8HuacI
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load the given dataset
heart_data = pd.read_csv("heart.csv")
# There are no mentioned nulls and there are no categorical variables so no need fo one-hot encoding and also no need to drop any values
#i will just scale it
scaler = StandardScaler()
numerical_features = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
heart_data[numerical_features] = scaler.fit_transform(heart_data[numerical_features])

# Splitting the dataset into training and testing sets
X = heart_data.drop(columns=['target'])
y = heart_data['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

class LogisticRegression:
    def __init__(self, learning_rate=0.01, num_iterations=1000):
        self.learning_rate = learning_rate
        self.num_iterations = num_iterations
        self.weights = None
        self.bias = None

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def fit(self, X, y):
        num_samples, num_features = X.shape
        self.weights = np.zeros(num_features)
        self.bias = 0

        # Gradient Descent
        for _ in range(self.num_iterations):
            linear_model = np.dot(X, self.weights) + self.bias
            y_predicted = self.sigmoid(linear_model)

            # Gradient descent updates
            dw = (1 / num_samples) * np.dot(X.T, (y_predicted - y))
            db = (1 / num_samples) * np.sum(y_predicted - y)

            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

    def predict(self, X):
        linear_model = np.dot(X, self.weights) + self.bias
        y_predicted = self.sigmoid(linear_model)
        y_predicted_cls = [1 if i > 0.5 else 0 for i in y_predicted]
        return y_predicted_cls

model = LogisticRegression(learning_rate=0.01, num_iterations=1000)
model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions)
recall = recall_score(y_test, predictions)
f1 = f1_score(y_test, predictions)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)



"""Discussion section:
Observations about the dataset:

The dataset we apply comprises multiple variables connected with heart health, such as age, blood pressure, cholesterol level and angina caused by exercise.
In particular, the dataset encompasses these 14 features out of the overall 76 attributes attributed to a target variable that takes the value 0 in case of less /no chance of heart disease and 1 where there is more chance of heart disease.

Scaling of numerical objects was accomplished by using StandardScaler.
Challenges faced during data cleaning and model implementation:Challenges faced during data cleaning and model implementation:

ive read the dataset and it is not categorical it doesnt need to be encoded
Insights gained from the model's performance:Insights gained from the model's performance:

The model has shown statisitcs of:
Accuracy: 0.8688524590163934
Precision: 0.875
Recall: 0.875
F1-score: 0.875
Summary:
Although the logistic regression model is indeed showing this performance with a high accuracy, it can still be boosted. beacause the accuracy can still be raised.
"""