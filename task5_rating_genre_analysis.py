import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

netflix_data = pd.read_csv(
    "cleaned_data/netflix_cleaned.csv"
)

# Rating Analysis
rating_distribution = (
    netflix_data["rating"]
    .value_counts()
)

plt.figure(figsize=(12,6))

sns.countplot(
    data=netflix_data,
    y="rating",
    order=rating_distribution.index
)

plt.title("Netflix Rating Analysis")

plt.tight_layout()

plt.savefig(
    "charts/rating_analysis.png"
)

plt.show()

# Genre Analysis
genre_series = (
    netflix_data["listed_in"]
    .str.split(",")
    .explode()
    .str.strip()
)

top_genres = genre_series.value_counts().head(15)

plt.figure(figsize=(12,7))

top_genres.plot(kind="barh")

plt.title("Top Netflix Genres")

plt.tight_layout()

plt.savefig(
    "charts/genre_analysis.png"
)

plt.show()

# Rating vs Type
rating_vs_type = pd.crosstab(
    netflix_data["type"],
    netflix_data["rating"]
)

rating_vs_type.plot(
    kind="bar",
    figsize=(14,6)
)

plt.title("Ratings Across Content Types")

plt.tight_layout()

plt.savefig(
    "charts/rating_vs_type.png"
)

plt.show()

print("\nAudience Insights")
print("-------------------")
print(
    "Most Common Rating:",
    rating_distribution.idxmax()
)
print(
    "Most Popular Genre:",
    top_genres.idxmax()
)