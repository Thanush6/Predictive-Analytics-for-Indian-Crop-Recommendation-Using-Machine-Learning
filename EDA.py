
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("indiancrop_dataset.csv")

print("Dataset Shape:", data.shape)
print("\nFirst 5 Rows:")
print(data.head())

print("\nDataset Information:")
data.info()

print("\nStatistical Summary:")
print(data.describe())

print("\nCrop Distribution:")
print(data["CROP"].value_counts())

print("\nMissing Values:")
print(data.isnull().sum())

print("\nDuplicate Rows:", data.duplicated().sum())

print("\nUnique Values:")
print(data.nunique())

plt.figure(figsize=(12, 6))
sns.countplot(data=data, x="CROP", order=data["CROP"].value_counts().index)
plt.title("Distribution of Crops")
plt.xlabel("Crop")
plt.ylabel("Number of Records")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

numeric_columns = [
    "N_SOIL", "P_SOIL", "K_SOIL", "TEMPERATURE",
    "HUMIDITY", "ph", "RAINFALL", "CROP_PRICE"
]

data[numeric_columns].hist(figsize=(14, 10), bins=20)
plt.suptitle("Distribution of Agricultural Features")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 7))
correlation = data[numeric_columns].corr()
sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

features = [
    "N_SOIL", "P_SOIL", "K_SOIL", "TEMPERATURE",
    "HUMIDITY", "ph", "RAINFALL"
]

for feature in features:
    plt.figure(figsize=(12, 5))
    sns.boxplot(data=data, x="CROP", y=feature)
    plt.title(f"{feature} Across Different Crops")
    plt.xlabel("Crop")
    plt.ylabel(feature)
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

state_crop = pd.crosstab(data["STATE"], data["CROP"])

plt.figure(figsize=(14, 8))
sns.heatmap(state_crop, cmap="YlGnBu")
plt.title("Crop Distribution Across States")
plt.xlabel("Crop")
plt.ylabel("State")
plt.tight_layout()
plt.show()
