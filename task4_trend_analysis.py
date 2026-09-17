import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_data/netflix_cleaned.csv")

yearly_content = (
    df["release_year"]
    .value_counts()
    .sort_index()
)

plt.figure(figsize=(12,6))

plt.plot(
    yearly_content.index,
    yearly_content.values,
    marker="o"
)

plt.title("Netflix Content Release Trend")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")

plt.grid(True)

plt.savefig("charts/yearly_trend.png")
plt.show()