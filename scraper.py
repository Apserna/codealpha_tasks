import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://books.toscrape.com/catalogue/"

data = []

for page in range(1, 51):

    if page == 1:
        url = "https://books.toscrape.com/"
    else:
        url = base_url + f"page-{page}.html"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    print(f"Page {page}: {len(books)} books")

    for book in books:

        title = book.h3.a["title"]

        price = book.find(
            "p", class_="price_color"
        ).text.strip()

        rating = book.find(
            "p", class_="star-rating"
        )["class"][1]

        availability = book.find(
            "p", class_="availability"
        ).get_text(strip=True)

        book_url = book.h3.a["href"]

        book_data = {
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability,
            "URL": book_url
        }

        data.append(book_data)


df = pd.DataFrame(data)

print("Total books:", len(df))
print(df.shape)

print(df.head())

df.to_csv("books_data.csv", index=False)

print("Dataset saved successfully!")
#pandas to save it in csv file
df = pd.DataFrame(data)
print(df)
print(df.head())
print(df.shape)