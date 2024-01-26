from bs4 import BeautifulSoup
import pandas as pd

with open("index.html", "r") as file :
    html_text = file.read()
# print(html_text)

souped_html = BeautifulSoup(html_text, "lxml")
# print(souped_html)

h4s = souped_html.find_all("h4")
# print(h4s)

fav_things = {}

for h4 in h4s:
    category = h4.text
    # print(category)
    things = []

    gold_match = h4.find_next(class_="gold")
    for thing in gold_match:
        # print(thing)
        things.append(thing)

    silver_match = h4.find_next(class_="silver")
    for thing in silver_match:
        # print(thing)
        things.append(thing)

    bronze_match = h4.find_next(class_="bronze")
    for thing in bronze_match:
        # print(thing)
        things.append(thing)

    fav_things[category] = things
# print(fav_things)

df = pd.DataFrame({key:pd.Series(value) for key, value in fav_things.items()})
df.index = ["gold", "silver", "bronze"]
# print(df)

# df = pd.DataFrame.from_dict(fav_things, orient="index").T

df.to_excel("1st_website.xlsx", index_label="1st_website")