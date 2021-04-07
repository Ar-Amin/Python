# 1st step install and import modules
# -- pip/pip3 install lxml
# -- pip/pip3 install requests
# -- pip/pip3 install beautifulsoup4

import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

job_title = []
comany_name = []
location_name = []
skills = []

# 2nd step use requestes to fetch the url
result = requests.get(
    "https://wuzzuf.net/search/jobs/?a=hpb%7Cspbg&q=network%20administration")


# 3rd step save page content/markup
src = result.content
print(src)

# 4th Step create soup object to parse content
soup = BeautifulSoup(src, "lxml")
# 5th Step the elements containing info we need
# -- job titles, jop skills, company names, location names

job_titles = soup.find_all("h2", {"class": "css-m604qf"})
# print(job_titles)
comany_names = soup.find_all("a", {"class": "css-17s97q8"})
location_names = soup.find_all("span", {"class": "css-5wys0k"})
job_skills = soup.find_all("div", {"class": "css-y4udm8"})

# 6th step loop over returned lists to extract needed info into other lists
for i in range(len(job_titles)):
    job_title.append(job_titles[i].text)
    comany_name.append(comany_names[i].text)
    location_name.append(location_names[i].text)
    skills.append(job_skills[i].text)


#  7 th Step creat csv file and fill it with values
file_list = [job_title, comany_name, location_name, skills]
exported = zip_longest(*file_list)
with open("/home/neo/Documents/Python/CodzelaPython/test.csv", "w") as myFile:
    wr = csv.writer(myFile)
    wr.writerow([" Job title", "Company name", "Location", "Skills"])
    wr.writerows(exported)
