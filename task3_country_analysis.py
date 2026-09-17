import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_data/netflix_cleaned.csv")

country_data = (
    df["country"]
    .str.split(",")
    .explode()
    .str.strip()
)

top_countries = country_data.value_counts().head(10)

print(top_countries)

plt.figure(figsize=(10,6))

top_countries.plot(
    kind="bar"
)

plt.title("Top 10 Countries Producing Netflix Content")
plt.xlabel("Country")
plt.ylabel("Content Count")

plt.tight_layout()

plt.savefig("charts/country_analysis.png")
plt.show()