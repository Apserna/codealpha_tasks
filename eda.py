#importing the file
import pandas as pd
df = pd.read_csv("books_data.csv")
print(df.head())
print("\nDataset Shape:")
print(df.shape)
print("\nDataset Information:")
print(df.info())
#finding missing values
print("\nMissing Values:")
print(df.isnull().sum())
#finding duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Convert Price to numeric
df["Price"] = (
    df["Price"]
    .str.replace("Â", "", regex=False)
    .str.replace("£", "", regex=False)
    .str.strip()
    .astype(float)
)

print("\nPrice Data Type:")
print(df["Price"].dtype)

# Price statistics
print("\nPrice Statistics:")
print(df["Price"].describe())

# Rating distribution
print("\nRating Distribution:")
print(df["Rating"].value_counts())

#finding most cheapest book and expensive book
cheapest_book = df.loc[df["Price"].idxmin()]
most_expensive_book = df.loc[df["Price"].idxmax()]

print("\nCheapest Book:")
print(cheapest_book[["Title", "Price", "Rating"]])

print("\nMost Expensive Book:")
print(most_expensive_book[["Title", "Price", "Rating"]])

#average price for higher rating
print("\nAverage Price by Rating:")
print(df.groupby("Rating")["Price"].mean().sort_values(ascending=False))
rating_counts = df["Rating"].value_counts()

# Rating counts
print("\nNumber of Books by Rating:")
print(rating_counts)