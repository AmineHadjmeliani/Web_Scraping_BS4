## Load libraries
from bs4 import BeautifulSoup 
import requests 
import pandas as pd 

## get the website
url_pages = 'https://coreyms.com/page/'

df = {}
headline = []
links= []
description = []
### Pagination 
for i in range(1,18):
    url = f'{url_pages}{i}'
    
    content = requests.get(url)
    
    soup = BeautifulSoup(content.text, 'lxml')
    for article in soup.find_all('article'):
        try:
            headline.append(article.find('h2').text)
            description = article.find('div', class_='entry-content').p.text
            vid = article.find('iframe', class_='youtube-player')['src'].split('/')[4].split('?')[0]
            links.append(f'http://www.youtube.com/watch?{vid}')
        except Exception as e:
            links.append(None)

df = {
    "title":headline,
    'description':description,
    'youtube links':links}

df = pd.DataFrame(df)