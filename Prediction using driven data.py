import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# Load the dataset
data = pd.read_csv(r"C:\Users\K H U S H B O O\OneDrive\Desktop\Istudioproject\Latest Covid-19 India Status.csv")

# Data exploration and cleaning
print("\nData Exploration and Cleaning:\n")
print(f"Data Shape: {data.shape}")
print(f"Data Types:\n{data.dtypes}")
print(f"Missing Values:\n{data.isnull().sum()}")

# Display summary statistics
print("\nSummary Statistics:\n")
print(data.describe().round(2))

# Group data by state/UT and calculate various metrics
print("\nGrouped Data Metrics:\n")
data_grouped = data.groupby("State/UTs").agg(
    Total_Cases=('Total Cases', 'sum'),
    Active_Cases=('Active', 'sum'),
    Discharged_Cases=('Discharged', 'sum'),
    Death_Cases=('Deaths', 'sum'),
    Population=('Population', 'sum')
).reset_index()

# Calculate proportions
data_grouped['Total_Cases_to_Discharged'] = data_grouped['Total_Cases'] / data_grouped['Discharged_Cases']
data_grouped['Total_Cases_to_Population'] = data_grouped['Total_Cases'] / data_grouped['Population']

# Display grouped data
print(data_grouped)

# Create visualizations
print("\nVisualizations:\n")

# Distribution of population
plt.figure(figsize=(10, 6))
sns.histplot(data['Population'], kde=True)
plt.title("Distribution of Population")
plt.show()

# Pair plot of grouped data
plt.figure(figsize=(10, 6))
sns.pairplot(data_grouped)
plt.suptitle("Pair Plot of Grouped Data", y=1.02)
plt.show()

# Bar chart of total cases by state/UT
plt.figure(figsize=(12, 6))
sns.catplot(data=data_grouped, x='State/UTs', y='Total_Cases', kind='bar', height=5, aspect=2)
plt.title("Total Cases by State/UT")
plt.xticks(rotation=45)
plt.show()

# Bar chart of total cases to population by state/UT (with percentage formatting)
plt.figure(figsize=(12, 6))
sns.catplot(data=data_grouped, x='State/UTs', y='Total_Cases_to_Population', kind='bar', height=5, aspect=2)
plt.title("Total Cases to population by state/UT")
plt.show() 