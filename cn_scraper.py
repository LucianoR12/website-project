from bs4 import BeautifulSoup
import requests
import pandas as pd

html_text = requests.get("https://wearecodenation.com/2024/01/23/data-course-playground/").text
# print(html_text)

souped_html = BeautifulSoup(html_text, "lxml")
# print(souped_html)

h5s = souped_html.find_all("h5", class_="elementor-heading-title elementor-size-default")
# print(h5s)

# for h5 in h5s:
#     if ":" in h5.text:
        # print(h5.text)

h6s = souped_html.find_all("h6")
# print(h6s)

# months = ["January","February","March","April","May","June","July","August","September","October","November","December"] 

# for h6 in h6s:
#     if any(month in h6.text for month in months):
        # print(h6.text)

courses = {}

for h5 in h5s:
    if ":" in h5.text:
        # print(h5.text)
        titles = h5.text
        h6_match = h5.find_next("h6")
        dates_list = []
        for date in h6_match.strings:
            # print(date)
            dates_list.append(date)
    courses[titles] = dates_list

# print(courses)

# other way to do it for UNEVEN DICTIONARY
# df = pd.DataFrame.from_dict(courses, orient="index").T 

courses_df = pd.DataFrame({key:pd.Series(value) for key, value in courses.items()})
print(courses_df)

courses_df.to_excel("scraped_data.xlsx", index_label="Courses")