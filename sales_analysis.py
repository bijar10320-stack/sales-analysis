# 📊 Sales Data Analysis Project
# Author: Bijar khan
# Goal: Analyze and visualize sales trends from the dataset

# Step 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load dataset
df = pd.read_csv("sales_data_sample.csv", encoding='latin1')

# Step 3: Understand the data
print("First 5 rows:")
print(df.head())
print("\nDataset info:")
print(df.info())
print("\nMissing values:")
print(df.isnull().sum())

# Step 4: Basic Cleaning
df.dropna(inplace=True)
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'], errors='coerce')

# Step 5: Exploratory Analysis
print("\nTop 5 Countries by Sales:")
print(df.groupby('COUNTRY')['SALES'].sum().sort_values(ascending=False).head())

# Step 6: Visualization Examples
plt.figure(figsize=(10,5))
sns.barplot(data=df, x='COUNTRY', y='SALES', estimator='sum')
plt.title('Total Sales by Country')
plt.show()

plt.figure(figsize=(10,5))
sns.barplot(data=df, x='PRODUCTLINE', y='SALES', estimator='sum')
plt.xticks(rotation=45)
plt.title('Total Sales by Product Line')
plt.show()

# Step 7: Insights
print("\nKey Insights:")
print("- Highest sales come from Classic Cars.")
print("- USA and France are top performing countries.")



