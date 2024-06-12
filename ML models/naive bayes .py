# -*- coding: utf-8 -*-
"""final_ml_assigment (1).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VQJbQSaREdj4673QJT18E-X2vWr1Yin7
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.naive_bayes import GaussianNB as gnb
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV

df=pd.read_csv("titanic.csv");
print(df.info())
print(df.describe())
df.drop('Cabin',axis=1,inplace=True)
#fill the non existing age column values with the midean of ages
imputer = SimpleImputer(strategy='median')
df['Age'] = imputer.fit_transform(df[['Age']])
#fill the missing embarked values with the most frequent value
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Convert categorical features into numerical ones using one-hot encoding
categorical_cols = ['Sex', 'Embarked']
df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
# scaling numerical data
scaler = StandardScaler()
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])

#selecting the feature that might actually play a part in the survival like we drop
#the id and name and the ticket because imo not very mofeda
scaler = StandardScaler()
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])
x=df.drop(['PassengerId','Survived','Name','Ticket'],axis=1)
y=df['Survived']
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=85)

# a5od el model mn el library
nb_classifier=gnb(var_smoothing=0.000000000000000000000000000000001)
nb_classifier.fit(xtrain,ytrain)

# predict
ypredicted = nb_classifier.predict(xtest)
print("Size of xtest:", len(xtest))
print("Size of ytest:", len(ytest))
print("Size of ypredicted:", len(ypredicted))

#el metrics
print("Accuracy:", accuracy_score(ytest, ypredicted))
print("Precision:", precision_score(ytest, ypredicted))
print("Recall:", recall_score(ytest, ypredicted))
print("F1 Score:", f1_score(ytest, ypredicted))
print("Classification Report:")
print(classification_report(ytest, ypredicted))

# Performing cross-validation
cv_scores = cross_val_score(nb_classifier, x, y, cv=5)
print("Cross Validation Scores:", cv_scores)