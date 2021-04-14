# -*- coding: utf-8 -*-
"""KNN-Pima Indians Diabetes dengan Menggunakan Jupyter.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10veHouBR1zFLEsRRY8r_RxemVhwIzdxQ
"""

# Commented out IPython magic to ensure Python compatibility.
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from pandas.plotting import scatter_matrix
import missingno as msno
import warnings
from mlxtend.plotting import plot_decision_regions
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
warnings.filterwarnings('ignore')
# %matplotlib inline

# Mengambil data set
diabetes_data = pd.read_csv('S:\Learning\MATA KULIAH\DATA MINING\diabetes.csv')

# Print 5 Baris Data
diabetes_data.head()

diabetes_data.info(verbose=True)

diabetes_data.describe()

diabetes_data.describe().T

diabetes_data_copy = diabetes_data.copy(deep=True)
diabetes_data_copy[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']] = diabetes_data_copy[[
    'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']].replace(0, np.NaN)

print(diabetes_data_copy.isnull().sum())

p = diabetes_data.hist(figsize=(20, 20))

diabetes_data_copy['Glucose'].fillna(
    diabetes_data_copy['Glucose'].mean(), inplace=True)
diabetes_data_copy['BloodPressure'].fillna(
    diabetes_data_copy['BloodPressure'].mean(), inplace=True)
diabetes_data_copy['SkinThickness'].fillna(
    diabetes_data_copy['SkinThickness'].median(), inplace=True)
diabetes_data_copy['Insulin'].fillna(
    diabetes_data_copy['Insulin'].median(), inplace=True)
diabetes_data_copy['BMI'].fillna(
    diabetes_data_copy['BMI'].median(), inplace=True)

p = diabetes_data_copy.hist(figsize=(20, 20))

diabetes_data.shape

p = msno.bar(diabetes_data)

color_wheel = {1: "#0392cf",
               2: "#0f0805"}
colors = diabetes_data["Outcome"].map(lambda x: color_wheel.get(x + 1))
print(diabetes_data.Outcome.value_counts())
p = diabetes_data.Outcome.value_counts().plot(kind="bar")

p = scatter_matrix(diabetes_data, figsize=(25, 25))

p = sns.pairplot(diabetes_data_copy, hue='Outcome')

plt.figure(figsize=(12, 10))
p = sns.heatmap(diabetes_data.corr(), annot=True, cmap='RdYlGn')

plt.figure(figsize=(12, 10))
p = sns.heatmap(diabetes_data_copy.corr(), annot=True, cmap='RdYlGn')

sc_X = StandardScaler()
X = pd.DataFrame(sc_X.fit_transform(diabetes_data_copy.drop(["Outcome"], axis=1),),
                 columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
                          'BMI', 'DiabetesPedigreeFunction', 'Age'])

X.head()

y = diabetes_data_copy.Outcome

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=1/3, random_state=42, stratify=y)


test_scores = []
train_scores = []

for i in range(1, 15):

    knn = KNeighborsClassifier(i)
    knn.fit(X_train, y_train)

    train_scores.append(knn.score(X_train, y_train))
    test_scores.append(knn.score(X_test, y_test))

max_train_score = max(train_scores)
train_scores_ind = [i for i, v in enumerate(
    train_scores) if v == max_train_score]
print('Max train score {} % and k = {}'.format(
    max_train_score*100, list(map(lambda x: x+1, train_scores_ind))))

max_test_score = max(test_scores)
test_scores_ind = [i for i, v in enumerate(test_scores) if v == max_test_score]
print('Max test score {} % and k = {}'.format(
    max_test_score*100, list(map(lambda x: x+1, test_scores_ind))))

"""
plt.figure(figsize=(12, 5))
p = sns.lineplot(range(1, 15), train_scores, marker='*', label='Train Score')
p = sns.lineplot(range(1, 15), test_scores, marker='o', label='Test Score')

knn = KNeighborsClassifier(11)

knn.fit(X_train, y_train)
knn.score(X_test, y_test)

value = 20000
width = 20000
plot_decision_regions(X.values, y.values, clf=knn, legend=2,
                    filler_feature_values={
                    2: value, 3: value, 4: value, 5: value, 6: value, 7: value},
                    filler_feature_ranges={
                    2: width, 3: width, 4: width, 5: width, 6: width, 7: width},
                    X_highlight=X_test.values)
plt.title('KNN dengan data Diabetes')
plt.show()
"""
