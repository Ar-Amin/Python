# 1st step install and import modules
# -- pip/pip3 install lxml
# -- pip/pip3 install requests
# -- pip/pip3 install beautifulsoup4

import requests
from bs4 import Beaurifulsoup
import csv
from itertools import zip_longest

# 2nd step use requestes to fetch the url
result = requests.get(
    "https://wuzzuf.net/search/jobs/?a=hpb%7Cspbg&q=network%20administration")


# 3rd step save page content/markup
src = result.content
print(src)

# 4th step create soup object to parse content
