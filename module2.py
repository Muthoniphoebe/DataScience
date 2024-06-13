import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score

# Load the dataset
data = pd.read_csv("OnlineRetail.csv", encoding='latin1')

# Initial data checks
print(data.head())
print(data.info())
print(data.columns)
print(data.describe())
print('The null values:', data.isnull().sum())

# Handle missing values
df_null = round(100 * (data.isnull().sum()) / len(data), 2)
print(df_null)

# Convert CustomerID to string
data['CustomerID'] = data['CustomerID'].astype(str)
print(data.info())

# Drop StockCode column
data.drop(['StockCode'], axis=1, inplace=True)
print(data.columns)

# Create the Amount column
data['Amount'] = data['Quantity'] * data['UnitPrice']

# Grouping by Country and calculating total sales
sales_by_country = data.groupby('Country')['Quantity'].sum().sort_values(ascending=False)
print('The countries selling the most are:')
print(sales_by_country.head())

# Grouping by Description and calculating total quantity sold
sales_by_product = data.groupby('Description')['Quantity'].sum().sort_values(ascending=False)
print('The products selling the most are:')
print(sales_by_product.head())

# Grouping by Description and calculating the total quantity sold for each product
frequently_sold_products = data.groupby('Description')['Quantity'].count().sort_values(ascending=False)

# Display the top 10 most frequently sold products
print(frequently_sold_products.head(10))

# Grouping by Description and calculating the total quantity sold for each product
frequently_sold_products = data.groupby('Description')['InvoiceNo'].count().sort_values(ascending=False)

# Display the top 10 most frequently sold products
print(frequently_sold_products.head(10))

# Convert the 'InvoiceDate' column to datetime
data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'], format='%m/%d/%Y %H:%M')

print(data['InvoiceDate'])

# Find the maximum date in the dataset
max_date = max(data['InvoiceDate'])

min_date = min(data['InvoiceDate'])

# Calculate the date 30 days before the maximum date
last_30_days_start = max_date - pd.DateOffset(days=30)
print(f'Last 30 days start date: {last_30_days_start}')

# Filter the data to include only transactions from the last 30 days
last_30_days_data = data[(data['InvoiceDate'] >= last_30_days_start) & (data['InvoiceDate'] <= max_date)]

# Calculate the total sales for the last 30 days for all products combined
total_sales_last_30_days = last_30_days_data['Amount'].sum()

# Print the total sales for the last 30 days
print(f'Total sales for the last 30 days: £{total_sales_last_30_days:.2f}')


rfm_df = rfm[['Amount', 'Frequency', 'Recency']]

# Instantiate
scaler = StandardScaler()

# fit_transform
rfm_df_scaled = scaler.fit_transform(rfm_df)
rfm_df_scaled.shape

rfm_df_scaled = pd.DataFrame(rfm_df_scaled)
rfm_df_scaled.columns = ['Amount', 'Frequency', 'Recency']
rfm_df_scaled.head()

kmeans = KMeans(n_clusters=4, max_iter=50)
kmeans.fit(rfm_df_scaled)
kmeans.labels_
ssd = []
range_n_clusters = [2, 3, 4, 5, 6, 7, 8]
for num_clusters in range_n_clusters:
    kmeans = KMeans(n_clusters=num_clusters, max_iter=50)
    kmeans.fit(rfm_df_scaled)
    
    ssd.append(kmeans.inertia_)
    
# plot the SSDs for each n_clusters
plt.plot(ssd)

# Silhouette analysis
range_n_clusters = [2, 3, 4, 5, 6, 7, 8]

for num_clusters in range_n_clusters:
    
    # intialise kmeans
    kmeans = KMeans(n_clusters=num_clusters, max_iter=50)
    kmeans.fit(rfm_df_scaled)
    
    cluster_labels = kmeans.labels_
    
    # silhouette score
    silhouette_avg = silhouette_score(rfm_df_scaled, cluster_labels)
    print("For n_clusters={0}, the silhouette score is {1}".format(num_clusters, silhouette_avg))

    
kmeans = KMeans(n_clusters=3, max_iter=50)
kmeans.fit(rfm_df_scaled)
kmeans.labels_
# assign the label
rfm['Cluster_Id'] = kmeans.labels_
rfm.head()
# Box plot to visualize Cluster Id vs Frequency

sns.boxplot(x='Cluster_Id', y='Amount', data=rfm)
# Box plot to visualize Cluster Id vs Frequency

sns.boxplot(x='Cluster_Id', y='Frequency', data=rfm)

#Box plot to visualize Cluster Id vs Recency

sns.boxplot(x='Cluster_Id', y='Recency', data=rfm)