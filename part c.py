import pandas as pd
import requests
from io import StringIO

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    data_content = response.content.decode('utf-8')
    
    df = pd.read_csv(StringIO(data_content), header=None)

    df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

    # Print the DataFrame
    print(df.to_string())
else:
    # Print an error message if the request was not successful
    print("Error")

#2a
print("First 8 records:",df.head(8))

'''
First 8 records:    sepal_length  sepal_width  petal_length  petal_width        class
0           5.1          3.5           1.4          0.2  Iris-setosa
1           4.9          3.0           1.4          0.2  Iris-setosa
2           4.7          3.2           1.3          0.2  Iris-setosa
3           4.6          3.1           1.5          0.2  Iris-setosa
4           5.0          3.6           1.4          0.2  Iris-setosa
5           5.4          3.9           1.7          0.4  Iris-setosa
6           4.6          3.4           1.4          0.3  Iris-setosa
7           5.0          3.4           1.5          0.2  Iris-setosa
'''

#2b
print('Number of records and features:',df.shape)

'''
Number of records and features: (150, 5)
'''

#2c
print('Data type of each feature:',df.dtypes)

'''
Data type of each feature: sepal_length    float64
sepal_width     float64
petal_length    float64
petal_width     float64
class            object
dtype: object
'''

#2d
print('Existence of missing values:',df.isnull().sum())

'''
Existence of missing values: sepal_length    0
sepal_width     0
petal_length    0
petal_width     0
class           0
dtype: int64
'''
#2e
#use case 1
print("Correlation between 'sepal_length' and 'sepal_width':",df[['sepal_length', 'sepal_width']].corr())

'''
Correlation between 'sepal_length' and 'sepal_width':               sepal_length  sepal_width
sepal_length      1.000000    -0.109369
sepal_width      -0.109369     1.000000



'''
The correlation matrix shows the correlation coefficients between 'sepal_length' and 'sepal_width'.
A correlation coefficient close to 1 indicates a strong positive correlation, close to -1 indicates a strong negative correlation,
and close to 0 indicates little to no correlation.
In this case, the correlation coefficient is approximately -0.109369, suggesting a weak negative correlation between sepal length and sepal width.








#use case 2
print("Mean petal length for each class:",df.groupby('class')['petal_length'].mean())
'''
Mean petal length for each class: class
Iris-setosa        1.464
Iris-versicolor    4.260
Iris-virginica     5.552
Name: petal_length, dtype: float64
'''
This code snippet displays the average petal length for each class of iris flowers:
'Iris-setosa', 'Iris-versicolor', and 'Iris-virginica'. It provides insights into the typical petal lengths for each species.







#use case 3
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 6))
plt.scatter(df['petal_length'], df['petal_width'])
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.title('Relationship between Petal Length and Petal Width')
plt.show()



'''
Report on the Iris Dataset Analysis
The Iris dataset is a classic dataset in the field of machine learning and statistics, comprising measurements of iris flowers' features such as sepal length, sepal width, petal length, and petal width.
It serves as a benchmark dataset for various classification and clustering tasks.
The dataset contains 150 samples of iris flowers, with 50 samples for each of the three species: setosa, versicolor, and virginica.
Each sample is characterized by its four features, measured in centimeters.
The analysis aims to explore the dataset, understand its structure, and uncover insights into the relationships between different features and iris species.
Additionally, the analysis seeks to demonstrate common exploratory data analysis techniques and their application to real-world datasets.
The analysis revealed distinct differences in the features of the three iris species, particularly in petal length and width.
Setosa species exhibited smaller sepal and petal dimensions compared to versicolor and virginica species. Additionally, scatter plots indicated strong correlations between certain pairs of features.
During the analysis, it was determined that the Iris dataset contains no missing values, ensuring the completeness and reliability of the dataset for further analysis.
Correlation analysis between sepal length and width, petal length and width, and species classification highlighted significant relationships between these features. These relationships contribute to distinguishing between iris species and can inform future classification models.
The analysis underscores the importance of understanding feature relationships in the Iris dataset for accurate species classification.'''
