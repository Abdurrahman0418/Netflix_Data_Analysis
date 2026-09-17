import pandas as pd

# Load dataset
df = pd.read_csv("dataset/netflix_titles.csv")

print("Original Shape:", df.shape)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Handle missing values
df["country"] = df["country"].fillna("Unknown")
df["director"] = df["director"].fillna("Not Available")
df["rating"] = df["rating"].fillna("Not Rated")

# Standardize text columns
df["country"] = df["country"].str.strip().str.title()
df["rating"] = df["rating"].str.strip().str.upper()
df["type"] = df["type"].str.strip().str.title()

# Save cleaned dataset
df.to_csv("cleaned_data/netflix_cleaned.csv", index=False)

print("Cleaning Completed Successfully!")
print("New Shape:", df.shape)