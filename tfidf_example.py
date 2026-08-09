import numpy as np
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "example_data.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

df = pd.read_csv(DATA_FILE)

# Team size N_p
team_size = df.groupby("team")["author"].nunique().rename("team_size")
df = df.merge(team_size, on="team", how="left")

# Number of authors n_rp reporting each role
role_frequency = (
    df.groupby(["team", "role"])["contribution"]
      .sum()
      .rename("role_frequency")
      .reset_index()
)
df = df.merge(role_frequency, on=["team", "role"], how="left")

# Raw role count for author i
author_role_count = (
    df.groupby(["team", "author"])["contribution"]
      .sum()
      .rename("raw_role_count")
      .reset_index()
)
df = df.merge(author_role_count, on=["team", "author"], how="left")

# TF and locally defined IDF (base 10)
df["tf"] = np.where(
    df["raw_role_count"] > 0,
    df["contribution"] / df["raw_role_count"],
    0.0
)
df["idf"] = np.log10(df["team_size"] / df["role_frequency"])
df["tfidf_score"] = df["tf"] * df["idf"]

# Overall TF-IDF-based contribution score
author_scores = (
    df.groupby(["team", "author"], as_index=False)
      .agg(
          raw_role_count=("contribution", "sum"),
          total_tfidf_score=("tfidf_score", "sum")
      )
)

df.to_csv(os.path.join(OUTPUT_DIR, "example_tfidf_detailed.csv"), index=False)
author_scores.to_csv(os.path.join(OUTPUT_DIR, "example_author_scores.csv"), index=False)

for team in df["team"].drop_duplicates():
    x = df[df["team"] == team].copy()
    role_order = x["role"].drop_duplicates().tolist()
    author_order = x["author"].drop_duplicates().tolist()

    raw = x.pivot(index="role", columns="author", values="contribution").reindex(role_order, columns=author_order)
    idf = x[["role", "idf"]].drop_duplicates().set_index("role").reindex(role_order)
    tfidf = x.pivot(index="role", columns="author", values="tfidf_score").reindex(role_order, columns=author_order)
    totals = author_scores[author_scores["team"] == team].set_index("author").reindex(author_order)

    print("\n" + "=" * 60)
    print(team)
    print("=" * 60)
    print("\nRaw role count:")
    print(raw.to_string())
    print("\nIDF weight:")
    print(idf.round(4).to_string())
    print("\nTF-IDF-based score:")
    print(tfidf.round(4).to_string())
    print("\nTotal count/score:")
    print(totals.round(4).to_string())

print("\nOutput files saved in:", OUTPUT_DIR)
