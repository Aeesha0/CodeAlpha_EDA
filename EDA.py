import pandas as pd
import os

# ---- Load the dataset ----
# Using the script's own folder so this works no matter where the terminal is pointed
folder = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(folder, "jumia_skincare.csv")
df = pd.read_csv(csv_path)

# ---- Basic overview: shape, columns, types, missing values ----
print("Shapes:", df.shape)
print("\nColumns:", list(df.columns))
print("\nData types:\n", df.dtypes)
print("\nMissing values:\n", df.isna().sum())
print("\nFirst 5 rows:\n", df.head())

# Note: old_price and discount are blank when a product isn't on sale (not an error)
# rating and review_count are blank for 9 products with no reviews yet

# ---- Q1: Price distribution ----
print("\nPrice summary:\n", df["price"].describe())

# ---- Rating distribution ----
print("\nRating summary:\n", df["rating"].describe())

# ---- Q2: Which brands dominate ----
print("\nTop 10 brands by count:\n", df["brand"].value_counts().head(10))

# ---- Discount check ----
# NOTE: the raw "discount" column mixes real % discounts with "Official Store" badges
# (a seller badge, not a price cut), so we can't just count non-null values here
print("\nNon-null discount values:\n", df["discount"].value_counts().head(10))

# Extract only the real percentage discounts (ignores "Official Store" text)
df["discount_pct"] = (
    df["discount"]
    .str.extract(r"(-?\d+)%")[0]   # pulls the number before the % sign
    .astype(float)
    .abs()                          # some show as -7%, others as 60%, same meaning
)
print("\nProducts with a REAL % discount:", df["discount_pct"].notna().sum(), "out of", len(df))
print(df["discount_pct"].describe())

# ---- Q3: Does price relate to rating? ----
print("\nCorrelation (price vs rating):\n", df[["price", "rating"]].corr())

# group products into rating bands to see if the pattern is clearer than a straight correlation
df["rating_band"] = pd.cut(
    df["rating"], bins=[0, 3, 4, 4.5, 5],
    labels=["Low (<=3)", "Good (3-4)", "Very Good (4-4.5)", "Excellent (4.5-5)"]
)
print("\nHow many products fall in each rating band:\n", df["rating_band"].value_counts())
print("\nAverage price by rating band:\n", df.groupby("rating_band", observed=True)["price"].mean())

# ---- Q4: Do discounted products get better ratings / more reviews? ----
discounted = df[df["discount_pct"].notna()]
not_discounted = df[df["discount_pct"].isna()]

print("\nAvg rating — discounted vs not:")
print("Discounted:", discounted["rating"].mean())
print("Not discounted:", not_discounted["rating"].mean())

print("\nAvg review_count — discounted vs not:")
print("Discounted:", discounted["review_count"].mean())
print("Not discounted:", not_discounted["review_count"].mean())

# ---- Q5: Price tier by top brand ----
top_brands = df["brand"].value_counts().head(5).index
print("\nAvg price by top brand:\n",
      df[df["brand"].isin(top_brands)].groupby("brand")["price"].mean().sort_values(ascending=False))

# ---- Products with no rating yet ----
print("\nProducts with no rating:\n", df[df["rating"].isna()][["name", "brand", "price"]].to_string())