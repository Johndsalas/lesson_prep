from requests import get
from bs4 import BeautifulSoup
import os
import pandas as pd

github_tag = 'Johndsalas'

from_date = '2019-08'

to_date = '2019-08'

next_year_month =

url = f'https://github.com/{github_tag}?tab=overview&from={from_date}-01&to={to_date}-30'
headers = {'User-Agent': 'Codeup Data Science'} # Some websites don't accept the pyhon-requests default user-agent
response = get(url, headers=headers)

#print(response.text[:400])

# Make a soup variable holding the response content
soup = BeautifulSoup(response.content, 'html.parser')

soup = soup.find_all('rect')

for thing in soup:

    if thing.has_attr('data-date'):

        if thing['data-date'] in :




