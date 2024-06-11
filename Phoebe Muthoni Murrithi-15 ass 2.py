#PHOEBE MUTHONI MURIITHI-KPSK-DEKUT-15

#ii)
import pandas as pd

df = pd.read_csv('Mall_Customers.csv')

print(df.head()) 
num_records = df.shape[0]

print("\nii)  Number of records :", num_records)


#iii)
print("\niii) Features in the dataset:")
print(df.columns)



# iv) Checking for missing values in the dataset
missing_values = df.isnull().any()

if missing_values.any():
    print("\niv)  The dataset contains missing values.")
else:
    print("\niv)  The dataset does not contain missing values.")
    

#v) Dealing with missing values
#   a) Remove rows with missing values  
df.dropna(inplace=True)

#   b) Replace missing values with new values
df.fillna(12, inplace=True)

#   c) Replace using Mean, Median, or Mode
df.fillna(df["Age"].mean(), inplace = True)


#vii)

# Calculate mean and standard deviation of 'Annual Income' by 'Gender'
mean_income_by_gender = df.groupby('Gender')['Annual Income (k$)'].mean()
std_income_by_gender = df.groupby('Gender')['Annual Income (k$)'].std()

# Calculate mean and standard deviation of 'Age' by 'Gender'
mean_age_by_gender = df.groupby('Gender')['Age'].mean()
std_age_by_gender = df.groupby('Gender')['Age'].std()

# Calculate mean and standard deviation of 'Spending Score' by 'Gender'
mean_spending_by_gender = df.groupby('Gender')['Spending Score (1-100)'].mean()
std_spending_by_gender = df.groupby('Gender')['Spending Score (1-100)'].std()


print("\nvii) Statistics by Gender:")
print("------------------------------------")
print("Mean Annual Income by Gender:")
print(mean_income_by_gender)
print("\nStandard Deviation of Annual Income by Gender:")
print(std_income_by_gender)
print("\nMean Age by Gender:")
print(mean_age_by_gender)
print("\nStandard Deviation of Age by Gender:")
print(std_age_by_gender)
print("\nMean Spending Score by Gender:")
print(mean_spending_by_gender)
print("\nStandard Deviation of Spending Score by Gender:")
print(std_spending_by_gender)

import matplotlib.pyplot as plt

# Mean values
mean_annual_income = [59.25, 62.23]
mean_age = [38.10, 39.81]
mean_spending_score = [51.53, 48.51]

# Standard deviations
std_annual_income = [26.01, 26.64]
std_age = [12.64, 15.51]
std_spending_score = [24.11, 27.90]

# Gender labels
genders = ['Female', 'Male']

fig, ax = plt.subplots(3, 1, figsize=(10, 15))

# Annual Income
ax[0].bar(genders, mean_annual_income, yerr=std_annual_income, capsize=5, color=['skyblue', 'salmon'])
ax[0].set_ylabel('Annual Income (k$)')
ax[0].set_title('Mean Annual Income by Gender')

# Age
ax[1].bar(genders, mean_age, yerr=std_age, capsize=5, color=['skyblue', 'salmon'])
ax[1].set_ylabel('Age')
ax[1].set_title('Mean Age by Gender')

# Spending Score
ax[2].bar(genders, mean_spending_score, yerr=std_spending_score, capsize=5, color=['skyblue', 'salmon'])
ax[2].set_ylabel('Spending Score (1-100)')
ax[2].set_title('Mean Spending Score by Gender')

plt.show()




#viii)
from sklearn.cluster import KMeans
import numpy as np

X = df[['Age', 'Annual Income (k$)']]

# Determine the optimal number of clusters (k)
inertia = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    inertia.append(kmeans.inertia_)

# Plot the elbow curve to determine the optimal k
import matplotlib.pyplot as plt
plt.plot(range(1, 11), inertia, marker='o')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal k')
plt.show()

# Based on the elbow method, let's choose k=4
k = 4

# Perform k-means clustering with selected k
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(X)

df['Cluster'] = kmeans.labels_

print("\nviii)Count of customers in each cluster:")
print(df['Cluster'].value_counts())

print("\nCluster centers:")
print(kmeans.cluster_centers_)



