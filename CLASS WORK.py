import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('retail_sales_dataset.csv')

print("head",data.head())
#dataset shape
print ("shape of data\n",data.shape)
 #features of the dataset      
print("Variables in the dataset:\n")
print(data.columns)
#information about the dataset
print("Data types of the features:\n")
print(data.info())

#the null values in the dataset
print("Null values in this data\n",data.isnull().sum())

#description od the datasets 
print("\nDescription of variables:\n b")
print(data.describe())
# identifying correlated values

numeric_data = data.select_dtypes(include=[np.number])
correlation_matrix = numeric_data.corr()
print("\nCorrelation Matrix:")
print(correlation_matrix)

#visualization of the datasets 

product_categories = data['Product Category'].unique()

# Plot histograms for each product category
plt.figure(figsize=(12, 8))
for category in product_categories:
    sns.histplot(data[data['Product Category'] == category]['Age'], bins=20, kde=True, label=category)

plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Age by Product Category')
plt.legend(title='Product Category')
plt.show()

#Data visualization (sales trends over time)
data['Date'] = pd.to_datetime(data['Date'])

# Set 'Date' column as index
data.set_index('Date', inplace=True)

# Resample monthly and plot total amount spent
data['Total Amount'].resample('M').sum().plot()  # Resample monthly and plot total sales
plt.title('Monthly Total Sales')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.show()
# Convert the data into a DataFrame

df = pd.DataFrame(data)

plt.figure(figsize=(12, 8))
sns.boxplot(x='Product Category', y='Age', data=data)
plt.xlabel('Product Category')
plt.ylabel('Age')
plt.title('Distribution of Age by Product Category')
plt.show()

# Plot gender against product category
sns.catplot(x="Product Category", hue="Gender", kind="count", data=df)
plt.title('Gender vs Product Category')
plt.show()

plt.figure(figsize=(12, 8))
for idx, category in enumerate(data['Product Category'].unique(), start=1):
    plt.subplot(2, 2, idx)
    sns.histplot(data=data[data['Product Category'] == category], x='Gender', hue='Gender', multiple='stack')
    plt.title(f'Gender Distribution in {category}')
    plt.xlabel('Gender')
    plt.ylabel('Count')

plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
sns.barplot(x='Gender', y='Total Amount', data=data, estimator=sum)
plt.title('Total Amount Spent by Gender')
plt.xlabel('Gender')
plt.ylabel('Total Amount')
plt.show()

plt.figure(figsize=(8, 6))
sns.barplot(x='Age', y='Total Amount', data=data, estimator=sum)
plt.title('Total Amount Spent by Age')
plt.xlabel('Age')
plt.ylabel('Total Amount')
plt.show()
