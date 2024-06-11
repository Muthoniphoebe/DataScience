import pandas as pd
data = pd.read_csv("OnlineRetail.csv", encoding='latin1')
print(data.head())

print(data.info())
print(data.columns)
print(data.describe)
print('The null values:', data.isnull().sum())
df_null = round(100*(data.isnull().sum())/len(data), 2)
print (df_null)
data['CustomerID'] = data['CustomerID'].astype(str)
print(data.info())
data.drop(['StockCode'], axis=1, inplace=True)
print(data.columns)
data['Amount'] = data['Quantity']*data['UnitPrice']
rfm_m= data.groupby('CustomerID')['Amount'].sum()
rfm_m = rfm_m.reset_index()
print(rfm_m.head())

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

print (data['InvoiceDate'])


# Find the maximum date in the dataset
max_date = max(data['InvoiceDate'])


min_date =min(data['InvoiceDate'])


# Calculate the date 30 days before the maximum date
last_30_days_start = max_date - pd.DateOffset(days=30)
print(f'Last 30 days start date: {last_30_days_start}')

# Filter the data to include only transactions from the last 30 days
last_30_days_data = data[(data['InvoiceDate'] >= last_30_days_start) & (data['InvoiceDate'] <= max_date)]
'''
# Group by 'Description' and calculate the total quantity sold for each product
totalsales = last_30_days_data.groupby('')['total_sales'].sum().sort_values(ascending=False)
# Print the total sales for the top 10 products
print(totalsales.head(10))
'''
if 'Amount' not in data.columns:
    data['Amount'] = data['Quantity'] * data['UnitPrice']

# Calculate the total sales for the last 30 days for all products combined
total_sales_last_30_days = last_30_days_data['Amount'].sum()

# Print the total sales for the last 30 days
print(f'Total sales for the last 30 days: £{total_sales_last_30_days:.2f}')














''''

# Calculate the start of the last month
from pandas.tseries.offsets import MonthEnd

last_month_start = max_date - MonthEnd(1) + pd.DateOffset(days=1)
last_month_end = max_date

print(f'Last month start date: {last_month_start}')
print(f'Last month end date: {last_month_end}')

# Filter the data to include only transactions from the last month
last_month_data = data[(data['InvoiceDate'] >= last_month_start) & (data['InvoiceDate'] <= last_month_end)]

# Calculate the total sales for the last month
total_sales_last_month = last_month_data['Amount'].sum()

print(f'Total sales for the last month: £{total_sales_last_month:.2f}')
'''
