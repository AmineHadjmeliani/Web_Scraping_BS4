import requests 
from bs4 import BeautifulSoup 
    
job_title = []
recruter=[]
experience= []
skills=[]
location=[]
links = []
## use requests to fetch the url 
for i in range(9):
    
        url = f'https://wuzzuf.net/search/jobs/?a=hpb&q=python&start={i}'
        src = requests.get(url).content

        ## create a soup object to parse the content 
        soup = BeautifulSoup(src, 'html.parser')

        ## find the elements containing the info we need 
        ## job title, job skills, company name, location 
        for article in soup.find_all('div', class_='css-1gatmva e1v1l3u10'):
                        job_title.append(article.find('a', class_='css-o171kl').text)
                        recruter.append(article.find('a', class_='css-17s97q8').text.split(' -')[0])
                        experience.append(article.find('div', {'class':'css-y4udm8'}).text.split('·')[1])
                        skills.append(','.join(article.find('div', {'class':'css-y4udm8'}).text.split('·')[2:]).strip(" ' "))
                        location.append(article.find('span', class_='css-5wys0k').text)
                        # links.append(article.find('a').attrs['href'])
import pandas as pd
search = {
    'job_title':job_title,
    'recruter':recruter,
    'experience':experience,
    'skills':skills,
    'location':location
    # 'links':links
    }

df = pd.DataFrame(search)
df.to_csv('Python_jobs.csv', index=False)

