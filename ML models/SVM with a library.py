# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hOdS89zU64C1mxpiObBphF05Gz8tt8bE
"""

from google.colab import drive
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
drive.mount('/content/drive')
files_path=['/content/drive/MyDrive/Flame.txt','/content/drive/MyDrive/Aggregation.txt','/content/drive/MyDrive/Jain.txt',
            '/content/drive/MyDrive/Compound.txt','/content/drive/MyDrive/Pathbased.txt','/content/drive/MyDrive/Spiral.txt']

"""def svmwithlibraries(file_path):
   file_path_to_be_used=file_path;
   df=pd.read_csv(file_paht,skip_)
"""

def svm(filepath):
  filepath_this = filepath
  df = pd.read_csv(filepath_this, skiprows=7, delimiter='\t', header=None)
  df = df.iloc[:, :3]
  df.columns = ['X1','X2', 'Y']
  Ys = df['Y'].unique()
  X = df[['X1', 'X2']]
  Y = df['Y']

  max_X1 = X['X1'].max()
  max_X2 = X['X2'].max()

  combinations = []
  for x1 in range(int(max_X1)+3):
      for x2 in range(int(max_X2)+3):
          combinations.append({'X1': x1, 'X2': x2})

  max_values_df = pd.DataFrame(combinations)

  X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
  svm_model = SVC(kernel='rbf', random_state=42, C=10)
  svm_model.fit(X_train, Y_train)
  y_pred = svm_model.predict(X_test)
  accuracy_of_model = accuracy_score(Y_test, y_pred)
  print("The accuracy:", accuracy_of_model)

  plt.scatter(X['X1'], X['X2'], c=svm_model.predict(X), cmap=plt.cm.coolwarm, s=40)
  plt.scatter(max_values_df['X1'], max_values_df['X2'],c=svm_model.predict(max_values_df), cmap=plt.cm.coolwarm, s=10)
  plt.xlabel('X1')
  plt.ylabel('X2')
  plt.show()

for i in files_path:
  svm(i)