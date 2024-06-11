import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#load the data

retail = pd.read_csv('retailsales.csv')

print(retail.to_string()) 


#data inspection
print(retail.columns)
print(retail.info())
print(retail.head())



print(retail.describe())

numeric_data = retail.select_dtypes(include=[np.number])
correlation_matrix = numeric_data.corr()
print("\nCorrelation Matrix:")
print(correlation_matrix)



# Convert the data into a DataFrame
df = pd.DataFrame(retail)

# Plot age against product category
sns.catplot(x="Product Category", y="Age", kind="box", data=df)
plt.title('Age vs Product Category')
plt.show()

# Plot gender against product category
sns.catplot(x="Product Category", hue="Gender", kind="count", data=df)
plt.title('Gender vs Product Category')
plt.show()

# Plot total amount against gender
sns.boxplot(x="Gender", y="Total Amount", data=df)
plt.title('Total Amount vs Gender')
plt.show()

# Alternatively, you can use a violin plot for a different perspective
sns.violinplot(x="Gender", y="Total Amount", data=df)
plt.title('Total Amount vs Gender')
plt.show()



plt.figure(figsize=(8, 6))
sns.barplot(x='Gender', y='Total Amount', data=df, estimator=sum)
plt.title('Total Amount Spent by Gender')
plt.xlabel('Gender')
plt.ylabel('Total Amount')
plt.show()


plt.figure(figsize=(8, 6))
sns.barplot(x='Age', y='Total Amount', data=df, estimator=sum)
plt.title('Total Amount Spent by Gender')
plt.xlabel('Gender')
plt.ylabel('Total Amount')
plt.show()


