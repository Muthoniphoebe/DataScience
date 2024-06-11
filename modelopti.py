import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
data=pd.read_csv("breast.csv")
'''print(breast)
print(breast.info())
print(breast.head())
#dataset shape
print("shape of data\n",breast.shape)
#description fo dataset
print(breast.describe())
#null values
print("null values in the data\n",breast.isnull().sum())
'''
# Spliting target variable and independent variables
X = data.drop(['diagnosis'], axis = 1)
y = data['diagnosis']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.3, random_state = 0)
print("Size of training set:", X_train.shape)
print("Size of test set:", X_test.shape)


'''


plt.figure(figsize=(8, 6))
sns.countplot(data=breast, x='diagnosis', palette='viridis')
plt.title('Count of Benign and Malignant Diagnoses')
plt.xlabel('Diagnosis')
plt.ylabel('Count')
plt.show()


# Create a FacetGrid for the 'mean radius' feature
g = sns.FacetGrid(breast, col="diagnosis", height=6, aspect=1)
g.map(sns.histplot, "radius_mean", kde=True, bins=30)

# Add titles and labels
g.set_axis_labels("radius_mean", "Frequency")
g.set_titles("Diagnosis: {col_name}")

plt.show()
'''
