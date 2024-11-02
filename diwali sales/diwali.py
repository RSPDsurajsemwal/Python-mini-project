# Import libraries
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

# Load CSV file
df = pd.read_csv('Diwali Sales Data.csv', encoding='unicode_escape')

# Drop unrelated/blank columns
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)

# Check for null values
df.dropna(inplace=True)

# Change data type
df['Amount'] = df['Amount'].astype(int)

# Rename column
df.rename(columns={'Marital_Status': 'Shaadi'}, inplace=True)

# Set up the plotting style
sns.set(style="whitegrid")

# Plotting subplots for Gender count and Total Amount by Gender
fig, axs = plt.subplots(1, 2, figsize=(16, 6))

# Countplot for Gender
ax1 = sns.countplot(x='Gender', data=df, ax=axs[0])
for bars in ax1.containers:
    ax1.bar_label(bars, label_type='edge', fontsize=10, padding=3)
ax1.set_title('Count of Sales by Gender')

# Pie chart for Total Amount by Gender
sales_gen = df.groupby('Gender')['Amount'].sum()
axs[1].pie(sales_gen, labels=sales_gen.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
axs[1].set_title('Total Amount by Gender')
axs[1].axis('equal')

plt.tight_layout()
plt.show()

# Subplots for Age Group and Total Amount by Age Group
fig, axs = plt.subplots(1, 2, figsize=(16, 6))

# Countplot for Age Group and Gender
ax1 = sns.countplot(data=df, x='Age Group', hue='Gender', ax=axs[0])
for bars in ax1.containers:
    ax1.bar_label(bars, label_type='edge', fontsize=10, padding=3)
ax1.set_title('Count of Sales by Age Group and Gender')

# Total Amount vs Age Group
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x='Age Group', y='Amount', data=sales_age, ax=axs[1])
axs[1].set_title('Total Amount by Age Group')

plt.tight_layout()
plt.show()

# Subplots for Top 10 States by Orders and Amount
fig, axs = plt.subplots(1, 2, figsize=(16, 6))

# Total number of orders from top 10 states
sales_state_orders = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
sns.barplot(data=sales_state_orders, x='State', y='Orders', ax=axs[0])
axs[0].set_title('Top 10 States by Number of Orders')
axs[0].set_xticklabels(axs[0].get_xticklabels(), rotation=90)

# Total amount from top 10 states
sales_state_amount = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
sns.barplot(data=sales_state_amount, x='State', y='Amount', ax=axs[1])
axs[1].set_title('Top 10 States by Total Amount')
axs[1].set_xticklabels(axs[1].get_xticklabels(), rotation=90)

plt.tight_layout()
plt.show()

# Subplots for Marital Status and Amount by Marital Status and Gender
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Countplot for Marital Status
ax1 = sns.countplot(data=df, x='Shaadi', ax=axs[0])
for bars in ax1.containers:
    ax1.bar_label(bars, label_type='edge', fontsize=10, padding=3)
ax1.set_title('Count of Sales by Marital Status')

# Amount by Marital Status and Gender
sales_marital_gender = df.groupby(['Shaadi', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(data=sales_marital_gender, x='Shaadi', y='Amount', hue='Gender', ax=axs[1])
axs[1].set_title('Total Amount by Marital Status and Gender')

plt.tight_layout()
plt.show()

# Subplots for Occupation and Amount by Occupation
fig, axs = plt.subplots(1, 2, figsize=(20, 6))

# Countplot for Occupation
ax1 = sns.countplot(data=df, x='Occupation', ax=axs[0])
for bars in ax1.containers:
    ax1.bar_label(bars, label_type='edge', fontsize=10, padding=3)
ax1.set_title('Count of Sales by Occupation')
axs[0].set_xticklabels(axs[0].get_xticklabels(), rotation=90)

# Total Amount by Occupation
sales_occupation = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(data=sales_occupation, x='Occupation', y='Amount', ax=axs[1])
axs[1].set_title('Total Amount by Occupation')
axs[1].set_xticklabels(axs[1].get_xticklabels(), rotation=90)

plt.tight_layout()
plt.show()

# Subplots for Product Category and Amount by Product Category
fig, axs = plt.subplots(1, 2, figsize=(20, 6))

# Countplot for Product Category
ax1 = sns.countplot(data=df, x='Product_Category', ax=axs[0])
for bars in ax1.containers:
    ax1.bar_label(bars, label_type='edge', fontsize=10, padding=3)
ax1.set_title('Count of Sales by Product Category')
axs[0].set_xticklabels(axs[0].get_xticklabels(), rotation=90)

# Total Amount by Product Category
sales_product = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
sns.barplot(data=sales_product, x='Product_Category', y='Amount', ax=axs[1])
axs[1].set_title('Total Amount by Product Category')
axs[1].set_xticklabels(axs[1].get_xticklabels(), rotation=90)

plt.tight_layout()
plt.show()

# Subplots for Top 10 Most Sold Products
fig, axs = plt.subplots(1, 1, figsize=(20, 6))

# Top 10 most sold products
sales_top_products = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
sns.barplot(data=sales_top_products, x='Product_ID', y='Orders', ax=axs)
axs.set_title('Top 10 Most Sold Products')
axs.set_xticklabels(axs.get_xticklabels(), rotation=90)

plt.tight_layout()
plt.show()
