import pandas as pd

df = pd.read_csv('Mall_Customers.csv')

print(df.to_string()) 
num_records = df.shape[0]

print("Number of records:", num_records)

#The column names of the DataFrame
print("Features in the dataset:")
print(df.columns)

# Check for missing values in the dataset
missing_values = df.isnull().any()

# Check if there are any missing values
if missing_values.any():
    print("The dataset contains missing values.")
else:
    print("The dataset does not contain missing values.")
import seaborn as sns
import matplotlib.pyplot as plt

# Set style for the plots
sns.set_style("whitegrid")

# Create subplots for each variable
fig, axes = plt.subplots(3, 1, figsize=(10, 15))

# Plot 1: Annual Income vs Gender
sns.boxplot(x='Gender', y='Annual Income (k$)', data=df, ax=axes[0])
axes[0].set_title('Annual Income Distribution by Gender')

# Plot 2: Age vs Gender
sns.boxplot(x='Gender', y='Age', data=df, ax=axes[1])
axes[1].set_title('Age Distribution by Gender')

# Plot 3: Spending Score vs Gender
sns.boxplot(x='Gender', y='Spending Score (1-100)', data=df, ax=axes[2])
axes[2].set_title('Spending Score Distribution by Gender')

# Adjust layout
plt.tight_layout()

# Show plots
plt.show()




from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np

# Select features for clustering
X = df[['Age', 'Annual Income (k$)']]

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Determine the optimal number of clusters (k)
# Using the elbow method
inertia = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

# Plot the elbow curve
plt.plot(range(1, 11), inertia, marker='o')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal k')
plt.show()

# From the elbow curve, it looks like the optimal k is around 3 or 4
# Let's use k=3 for demonstration
k = 3

# Perform k-means clustering
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(X_scaled)

# Add cluster labels to the original DataFrame
df['Cluster'] = kmeans.labels_

# Visualize the clustering results
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='Age', y='Annual Income (k$)', hue='Cluster', palette='Set1', legend='full')
plt.title('K-Means Clustering of Customers based on Age and Annual Income')
plt.xlabel('Age')
plt.ylabel('Annual Income (k$)')
plt.show()




