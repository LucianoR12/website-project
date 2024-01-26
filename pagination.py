from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

title_collection = []
price_collection = []
rating_collection = []

rating_to_int = {
    "One" : 1,
    "Two" : 2,
    "Three" : 3,
    "Four" : 4,
    "Five" : 5,
}

for page in range(1,51):
    html_text = requests.get(f"https://books.toscrape.com/catalogue/page-{page}.html").text
    soup = BeautifulSoup(html_text, 'lxml')

    titles = soup.find_all('h3')

    for book_title in titles:
        # print("Title : ", book_title.find('a').get('title').strip())
        title_collection.append(book_title.find('a').get('title').strip())
        price = book_title.find_next('p', class_="price_color")
        # print("Price: ", price.text.strip('Â'))
        price_collection.append(float(price.text.strip('Â£')))
        rating = book_title.find_previous('p', class_='star-rating').get('class')[1]
        # print(rating_to_int.get(rating))
        rating_collection.append(rating_to_int.get(rating))

    # time.sleep(2)

df = pd.DataFrame({
    "Title" : title_collection,
    "Price": price_collection,
    "Rating / 5" : rating_collection
})

print(df)

# df.to_excel("Books.xlsx", index=False)

max_price = df["Price"].max()
print(f"The maximum price of a book is: £{max_price:.2f}")

rate_4 = df[df["Rating / 5"] == 4].shape[0]
print(f"The number of books rated 4* is: {rate_4}")

average_price = df["Price"].mean()
print(f"The average price of a book is: £{average_price:.2f}")

