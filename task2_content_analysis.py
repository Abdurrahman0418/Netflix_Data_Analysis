import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("cleaned_data/netflix_cleaned.csv")

content_count = df["type"].value_counts()

print(content_count)

plt.figure(figsize=(8,5))

sns.countplot(
    data=df,
    x="type"
)

plt.title("Netflix Content Distribution")
plt.xlabel("Content Type")
plt.ylabel("Count")

plt.savefig("charts/content_distribution.png")
plt.show()