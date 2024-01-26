from bs4 import BeautifulSoup
import requests
import pandas as pd

with open("index.html", "r") as file :
    html_text = file.read()

souped_html = BeautifulSoup(html_text, "lxml")
print(souped_html)
