# 1st step install and import modules
# -- pip/pip3 install lxml
# -- pip/pip3 install requests
# -- pip/pip3 install beautifulsoup4

import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

# 2nd step use requestes to fetch the url
result = requests.get(
    "https://wuzzuf.net/search/jobs/?a=hpb%7Cspbg&q=network%20administration")


# 3rd step save page content/markup
src = result.content
print(src)

# 4th step create soup object to parse content
soup = BeautifulSoup(src, "lxml")
# 5th step the elements containing info we need
# -- job titles, jop skills, company names, location names

job_titles = soup.find_all("h2", {"class": "css-m604qf"})
# print(job_titles)
comany_name = soup.find_all("a", {"class": "css-17s97q8"})
location_name = soup.find_all("span", {"class": "css-5wys0k"})
job_skills = soup.find_all("div", {"class": "css-y4udm8"})

# 6th step loop over returned lists to extract needed info into other lists
