import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime


print("=" * 60)
print("NETFLIX BUSINESS INSIGHTS REPORT")
print("=" * 60)

df = pd.read_csv("cleaned_data/netflix_cleaned.csv")

print(f"\nDataset Shape: {df.shape}")


total_titles = len(df)

total_movies = len(
    df[df["type"] == "Movie"]
)

total_tv_shows = len(
    df[df["type"] == "TV Show"]
)

latest_year = df["release_year"].max()

oldest_year = df["release_year"].min()


country_data = (
    df["country"]
    .fillna("Unknown")
    .str.split(",")
    .explode()
    .str.strip()
)

top_countries = country_data.value_counts().head(10)


genre_data = (
    df["listed_in"]
    .str.split(",")
    .explode()
    .str.strip()
)

top_genres = genre_data.value_counts().head(10)


rating_distribution = (
    df["rating"]
    .fillna("Unknown")
    .value_counts()
)


yearly_content = (
    df["release_year"]
    .value_counts()
    .sort_index()
)

peak_year = yearly_content.idxmax()
peak_count = yearly_content.max()

# DASHBOARD 1
plt.figure(figsize=(8,5))

sns.countplot(
    data=df,
    x="type"
)

plt.title("Netflix Content Distribution")
plt.xlabel("Content Type")
plt.ylabel("Total Content")

plt.tight_layout()

plt.savefig(
    "charts/dashboard_content_type.png"
)

plt.close()

# DASHBOARD 2
plt.figure(figsize=(12,6))

top_countries.plot(
    kind="bar"
)

plt.title(
    "Top 10 Content Producing Countries"
)

plt.xlabel("Country")
plt.ylabel("Titles")

plt.tight_layout()

plt.savefig(
    "charts/dashboard_country_analysis.png"
)

plt.close()

# DASHBOARD 3
plt.figure(figsize=(12,6))

top_genres.plot(
    kind="barh"
)

plt.title(
    "Top 10 Netflix Genres"
)

plt.xlabel("Content Count")

plt.tight_layout()

plt.savefig(
    "charts/dashboard_genre_analysis.png"
)

plt.close()

# DASHBOARD 4
plt.figure(figsize=(12,6))

plt.plot(
    yearly_content.index,
    yearly_content.values,
    marker="o"
)

plt.title(
    "Netflix Content Growth Trend"
)

plt.xlabel("Release Year")
plt.ylabel("Number of Titles")

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "charts/dashboard_yearly_trend.png"
)

plt.close()

# DASHBOARD 5
plt.figure(figsize=(12,6))

sns.countplot(
    data=df,
    y="rating",
    order=rating_distribution.index
)

plt.title(
    "Netflix Content Ratings"
)

plt.xlabel("Content Count")
plt.ylabel("Rating")

plt.tight_layout()

plt.savefig(
    "charts/dashboard_rating_analysis.png"
)

plt.close()


most_common_genre = top_genres.idxmax()

most_common_country = top_countries.idxmax()

most_common_rating = rating_distribution.idxmax()

# REPORT CREATION
report_text = f"""
==================================================
NETFLIX BUSINESS INSIGHTS REPORT
==================================================

Generated On:
{datetime.now()}

--------------------------------------------------
DATASET SUMMARY
--------------------------------------------------

Total Titles:
{total_titles}

Movies:
{total_movies}

TV Shows:
{total_tv_shows}

Oldest Release Year:
{oldest_year}

Latest Release Year:
{latest_year}

--------------------------------------------------
TOP 10 COUNTRIES
--------------------------------------------------

{top_countries.to_string()}

--------------------------------------------------
TOP 10 GENRES
--------------------------------------------------

{top_genres.to_string()}

--------------------------------------------------
TOP RATINGS
--------------------------------------------------

{rating_distribution.head(10).to_string()}

--------------------------------------------------
TREND ANALYSIS
--------------------------------------------------

Peak Content Production Year:
{peak_year}

Titles Released:
{peak_count}

--------------------------------------------------
KEY BUSINESS INSIGHTS
--------------------------------------------------

1. Movies dominate the Netflix library.

2. Netflix has experienced strong content
   growth over recent years.

3. {most_common_country} is the leading
   content-producing country.

4. {most_common_genre} is the most
   popular genre category.

5. Most content falls under
   the '{most_common_rating}' rating.

--------------------------------------------------
RECOMMENDATIONS
--------------------------------------------------

1. Increase investment in high-performing
   genres.

2. Expand regional content production.

3. Strengthen international content
   partnerships.

4. Focus on audience-preferred
   content categories.

5. Continue content diversification
   strategies.

==================================================
END OF REPORT
==================================================
"""

with open(
    "reports/netflix_business_report.txt",
    "w",
    encoding="utf-8"
) as report_file:
    report_file.write(report_text)

# OUTPUT
print("\nREPORT GENERATED SUCCESSFULLY")

print("\nTotal Titles:", total_titles)
print("Movies:", total_movies)
print("TV Shows:", total_tv_shows)

print("\nTop Country:", most_common_country)
print("Top Genre:", most_common_genre)
print("Top Rating:", most_common_rating)

print("\nPeak Year:", peak_year)
print("Titles Released:", peak_count)

print("\nFiles Generated:")
print("- dashboard_content_type.png")
print("- dashboard_country_analysis.png")
print("- dashboard_genre_analysis.png")
print("- dashboard_yearly_trend.png")
print("- dashboard_rating_analysis.png")
print("- netflix_business_report.txt")

print("\nProject Completed Successfully")