# -*- coding: utf-8 -*-
"""assignment 3 redo

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17z6MRkfDcPV-mk42vw1pa9mpqeWDpybh

## **Problem 1:** Using diabetes dataset to build a logitisic regression binary classifier for positive diabetes.
"""

# Importing the dataset

import pandas as pd
from google.colab import drive
drive.mount('/content/drive')

file_path = '/content/drive/My Drive/ECGR 4105/Assignment 3/diabetes.csv'
diabetes_dataset = pd.DataFrame(pd.read_csv(file_path))
diabetes_dataset.head()

'''

Data Preprocessing

'''

X = diabetes_dataset.drop('Outcome', axis=1)
y = diabetes_dataset['Outcome']

# Performing scaling/normalization on features (x values) to scale the data between 0 and 1 to achieve better accuracy
from sklearn.preprocessing import StandardScaler

X_scaler = StandardScaler()
X_standard = X_scaler.fit_transform(X)


# Performing 80% and 20% split between training and evaluation (test)
from sklearn.model_selection import train_test_split

X_training, X_test, y_training, y_test = train_test_split(X_standard, y, test_size = 0.2, random_state = 0)

'''
Instance Classifier Creation for Logitistic Regression
'''
from sklearn.linear_model import LogisticRegression

classifier = LogisticRegression(max_iter = 1000, random_state = 0)
classifier.fit(X_training, y_training)

y_prediction = classifier.predict(X_test)


'''

Results

'''
from sklearn import metrics

# Accuracy

accuracy = metrics.accuracy_score(y_test, y_prediction)

# Precision

precision = metrics.precision_score(y_test, y_prediction)

# Recall

recall = metrics.recall_score(y_test, y_prediction)

# F1 Score

f1 = metrics.f1_score(y_test, y_prediction)

print("Accuracy: ", accuracy)
print("Precision: ", precision)
print("Recall: ", recall)
print("F1 Score: ", f1)

'''

Plotting Results

'''

# Confusion Matrix - Representing Binary Classifier

from sklearn.metrics import confusion_matrix

confusion_matrix = confusion_matrix(y_test, y_prediction)

# Visualizing Matrix

import seaborn as sns
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
class_names = ["Negative", "Positive"]
sns.heatmap(pd.DataFrame(confusion_matrix), annot=True, cmap='summer', fmt='g')
plt.title('Confusion Matrix for Problem 1')
ax.xaxis.set_label_position("top")
ax.set_xticklabels(class_names)
ax.set_yticklabels(class_names)
plt.xlabel('Predicted')
plt.ylabel('Actual')

X[0:5]

"""## **Problem 2 - Part 1:** Using cancer dataset to build a logitisic regression binary classifier to classify type of cancer (Malignant vs. benign)"""

import pandas as pd
from google.colab import drive
drive.mount('/content/drive')

file_path = '/content/drive/My Drive/ECGR 4105/Assignment 3/cancer.csv'
cancer_dataset = pd.DataFrame(pd.read_csv(file_path))
cancer_dataset.head()

'''

Data Preprocessing

'''

# Cleaning data
# Drop the 'Unnamed: 32' column
cancer_dataset.drop(['id', 'Unnamed: 32'], axis=1, inplace=True)

# Mapping M and B values of the diagnosis to 1 and 0
cancer_dataset['diagnosis'] = cancer_dataset['diagnosis'].map({'M': 1, 'B': 0})

X = cancer_dataset.drop('diagnosis', axis=1)
y = cancer_dataset['diagnosis']

# Performing scaling/normalization on features (x values) to scale the data between 0 and 1 to achieve better accuracy
from sklearn.preprocessing import StandardScaler

X_scaler = StandardScaler()
X_standard = X_scaler.fit_transform(X)

# Performing 80% and 20% split between training and evaluation (test)
from sklearn.model_selection import train_test_split

X_training, X_test, y_training, y_test = train_test_split(X_standard, y, test_size = 0.2, random_state = 0)

'''
Instance Classifier Creation for Logitistic Regression
'''
from sklearn.linear_model import LogisticRegression

classifier = LogisticRegression(max_iter = 1000, random_state = 0)
classifier.fit(X_training, y_training)

y_prediction = classifier.predict(X_test)

'''

Results

'''
from sklearn import metrics

# Accuracy

accuracy = metrics.accuracy_score(y_test, y_prediction)

# Precision

precision = metrics.precision_score(y_test, y_prediction)

# Recall

recall = metrics.recall_score(y_test, y_prediction)

# F1 Score

f1 = metrics.f1_score(y_test, y_prediction)

print("Accuracy: ", accuracy)
print("Precision: ", precision)
print("Recall: ", recall)
print("F1 Score: ", f1)

'''

Plotting Results

'''

# Confusion Matrix - Representing Binary Classifier

from sklearn.metrics import confusion_matrix

confusion_matrix = confusion_matrix(y_test, y_prediction)

# Visualizing Matrix

import seaborn as sns
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
class_names = ["Negative", "Positive"]
sns.heatmap(pd.DataFrame(confusion_matrix), annot=True, cmap='summer', fmt='g')
plt.title('Confusion Matrix for Problem 2a')
ax.xaxis.set_label_position("top")
ax.set_xticklabels(class_names)
ax.set_yticklabels(class_names)
plt.xlabel('Predicted')
plt.ylabel('Actual')

X[0:5]

"""## **Problem 2 - Part  2:** Repeating Part 1 with a weight penalty, considering the number of parameters."""

penalty_Values = 0.1
classifier_weight = LogisticRegression(max_iter = 1000, penalty = "l2", C = penalty_Values)
classifier_weight.fit(X_training, y_training)
y_prediction = classifier_weight.predict(X_test)

'''

Results

'''
from sklearn import metrics

# Accuracy

accuracy = metrics.accuracy_score(y_test, y_prediction)

# Precision

precision = metrics.precision_score(y_test, y_prediction)

# Recall

recall = metrics.recall_score(y_test, y_prediction)

# F1 Score

f1 = metrics.f1_score(y_test, y_prediction)

print("Accuracy: ", accuracy)
print("Precision: ", precision)
print("Recall: ", recall)
print("F1 Score: ", f1)

'''

Plotting Results

'''

# Confusion Matrix - Representing Binary Classifier

from sklearn.metrics import confusion_matrix

confusion_matrix = confusion_matrix(y_test, y_prediction)

# Visualizing Matrix

import seaborn as sns
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
class_names = ["Negative", "Positive"]
sns.heatmap(pd.DataFrame(confusion_matrix), annot=True, cmap='summer', fmt='g')
plt.title('Confusion Matrix for Problem 2b')
ax.xaxis.set_label_position("top")
ax.set_xticklabels(class_names)
ax.set_yticklabels(class_names)
plt.xlabel('Predicted')
plt.ylabel('Actual')

X[0:5]

"""## **Problem 3:** Using cancer dataset to build a naive Bayesian model to classify type of cancer (Malignant vs. benign)"""

import pandas as pd
from google.colab import drive
drive.mount('/content/drive')

file_path = '/content/drive/My Drive/ECGR 4105/Assignment 3/cancer.csv'
cancer_dataset = pd.DataFrame(pd.read_csv(file_path))
cancer_dataset.head()

'''

Data Preprocessing

'''

# Cleaning data
# Drop the 'Unnamed: 32' column
cancer_dataset.drop(['id', 'Unnamed: 32'], axis=1, inplace=True)

# Mapping M and B values of the diagnosis to 1 and 0
cancer_dataset['diagnosis'] = cancer_dataset['diagnosis'].map({'M': 1, 'B': 0})

X = cancer_dataset.drop('diagnosis', axis=1)
y = cancer_dataset['diagnosis']

# Performing scaling/normalization on features (x values) to scale the data between 0 and 1 to achieve better accuracy
from sklearn.preprocessing import StandardScaler

X_scaler = StandardScaler()
X_standard = X_scaler.fit_transform(X)

# Performing 80% and 20% split between training and evaluation (test)
from sklearn.model_selection import train_test_split

X_training, X_test, y_training, y_test = train_test_split(X_standard, y, test_size = 0.2, random_state = 0)

'''
Instance Classifier Creation for Naive Bayes
'''
from sklearn.naive_bayes import GaussianNB

classifier = GaussianNB()
classifier.fit(X_training, y_training)

y_prediction = classifier.predict(X_test)

'''

Results

'''
from sklearn import metrics

# Accuracy

accuracy = metrics.accuracy_score(y_test, y_prediction)

# Precision

precision = metrics.precision_score(y_test, y_prediction)

# Recall

recall = metrics.recall_score(y_test, y_prediction)

# F1 Score

f1 = metrics.f1_score(y_test, y_prediction)

print("Accuracy: ", accuracy)
print("Precision: ", precision)
print("Recall: ", recall)
print("F1 Score: ", f1)

'''

Plotting Results

'''

# Confusion Matrix - Representing Binary Classifier

from sklearn.metrics import confusion_matrix

confusion_matrix = confusion_matrix(y_test, y_prediction)

# Visualizing Matrix

import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(14, 6))

fig, ax = plt.subplots()
class_names = ["Negative", "Positive"]
sns.heatmap(pd.DataFrame(confusion_matrix), annot=True, cmap='summer', fmt='g')
plt.title('Confusion Matrix for Problem 3')
ax.xaxis.set_label_position("top")
ax.set_xticklabels(class_names)
ax.set_yticklabels(class_names)
plt.xlabel('Predicted')
plt.ylabel('Actual')

# Bar Graph of Evaluation Metrics
plt.figure(figsize=(14, 6))
metrics = ['Accuracy', 'Precision', 'Recall', 'F1 Score']
evalues = [accuracy, precision, recall, f1]
plt.bar(metrics, evalues)
plt.title('Naive Bayes Classifier Performance Metrics')

"""## **Problem 4:** Using cancer dataset to build a logitisic regression binary classifier to classify type of cancer (Malignant vs. benign). Using PCA feature extraction for training."""

import pandas as pd
from google.colab import drive
drive.mount('/content/drive')

file_path = '/content/drive/My Drive/ECGR 4105/Assignment 3/cancer.csv'
cancer_dataset = pd.DataFrame(pd.read_csv(file_path))
cancer_dataset.head()

'''

Data Preprocessing

'''

# Cleaning data
# Drop the 'Unnamed: 32' column
cancer_dataset.drop(['id', 'Unnamed: 32'], axis=1, inplace=True)

# Mapping M and B values of the diagnosis to 1 and 0
cancer_dataset['diagnosis'] = cancer_dataset['diagnosis'].map({'M': 1, 'B': 0})

X = cancer_dataset.drop('diagnosis', axis=1)
y = cancer_dataset['diagnosis']

# Performing scaling/normalization on features (x values) to scale the data between 0 and 1 to achieve better accuracy
from sklearn.preprocessing import StandardScaler

X_scaler = StandardScaler()
X_standard = X_scaler.fit_transform(X)

# Performing 80% and 20% split between training and evaluation (test)
from sklearn.model_selection import train_test_split

X_training, X_test, y_training, y_test = train_test_split(X_standard, y, test_size = 0.2, random_state = 0)

'''
Instance Classifier Creation for Logitistic Regression
'''

from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn import metrics


N_iterations = range(1, 15)

accuracy_list = []
precision_list = []
recall_list = []
f1_list = []

accuracy = 0
precision = 0
recall = 0
f1 = 0

for k in N_iterations:
  pca = PCA(n_components = k)
  X_pca_training = pca.fit_transform(X_training)
  X_pca_test = pca.transform(X_test)
  classifier = LogisticRegression(random_state = 0)
  classifier.fit(X_pca_training, y_training)
  y_prediction = classifier.predict(X_pca_test)

  accuracy = metrics.accuracy_score(y_test, y_prediction)
  precision = metrics.precision_score(y_test, y_prediction)
  recall = metrics.recall_score(y_test, y_prediction)
  f1 = metrics.f1_score(y_test, y_prediction)

  accuracy_list.append(accuracy)
  precision_list.append(precision)
  recall_list.append(recall)
  f1_list.append(f1)
  print("Number of Principal Components (K): ", k)
  print("Accuracy: ", accuracy)
  print("Precision: ", precision)
  print("Recall: ", recall)
  print("F1 Score: ", f1)
  print("")

'''

Plotting Results

'''

plt.plot(N_iterations, accuracy_list, label = 'Accuracy')
plt.plot(N_iterations, precision_list, label = 'Precision')
plt.plot(N_iterations, recall_list, label = 'Recall')
plt.plot(N_iterations, f1_list, label = 'F1 Score')
plt.xlabel('Number of Principal Components (K)')
plt.ylabel('Score')
plt.title('Evaluation Metrics vs. Number of Principal Components (K)')

"""## **Problem 5:** Using cancer dataset to build a Naive Bayes classifier regression classifier to classify type of cancer (Malignant vs. benign). Using PCA feature extraction for training."""

import pandas as pd
from google.colab import drive
drive.mount('/content/drive')

file_path = '/content/drive/My Drive/ECGR 4105/Assignment 3/cancer.csv'
cancer_dataset = pd.DataFrame(pd.read_csv(file_path))
cancer_dataset.head()

'''

Data Preprocessing

'''

# Cleaning data
# Drop the 'Unnamed: 32' column
cancer_dataset.drop(['id', 'Unnamed: 32'], axis=1, inplace=True)

# Mapping M and B values of the diagnosis to 1 and 0
cancer_dataset['diagnosis'] = cancer_dataset['diagnosis'].map({'M': 1, 'B': 0})

X = cancer_dataset.drop('diagnosis', axis=1)
y = cancer_dataset['diagnosis']

# Performing scaling/normalization on features (x values) to scale the data between 0 and 1 to achieve better accuracy
from sklearn.preprocessing import StandardScaler

X_scaler = StandardScaler()
X_standard = X_scaler.fit_transform(X)

# Performing 80% and 20% split between training and evaluation (test)
from sklearn.model_selection import train_test_split

X_training, X_test, y_training, y_test = train_test_split(X_standard, y, test_size = 0.2, random_state = 0)

'''
Instance Classifier Creation for Logitistic Regression
'''

from sklearn.decomposition import PCA
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics


N_iterations = range(1, 15)

accuracy_list = []
precision_list = []
recall_list = []
f1_list = []

accuracy = 0
precision = 0
recall = 0
f1 = 0

for k in N_iterations:
  pca = PCA(n_components = k)
  X_pca_training = pca.fit_transform(X_training)
  X_pca_test = pca.transform(X_test)
  classifier = GaussianNB()
  classifier.fit(X_pca_training, y_training)
  y_prediction = classifier.predict(X_pca_test)

  accuracy = metrics.accuracy_score(y_test, y_prediction)
  precision = metrics.precision_score(y_test, y_prediction)
  recall = metrics.recall_score(y_test, y_prediction)
  f1 = metrics.f1_score(y_test, y_prediction)

  accuracy_list.append(accuracy)
  precision_list.append(precision)
  recall_list.append(recall)
  f1_list.append(f1)
  print("Number of Principal Components (K): ", k)
  print("Accuracy: ", accuracy)
  print("Precision: ", precision)
  print("Recall: ", recall)
  print("F1 Score: ", f1)
  print("")

'''

Plotting Results

'''

plt.plot(N_iterations, accuracy_list, label = 'Accuracy')
plt.plot(N_iterations, precision_list, label = 'Precision')
plt.plot(N_iterations, recall_list, label = 'Recall')
plt.plot(N_iterations, f1_list, label = 'F1 Score')
plt.xlabel('Number of Principal Components (K)')
plt.ylabel('Score')
plt.title('Evaluation Metrics vs. Number of Principal Components (K)')