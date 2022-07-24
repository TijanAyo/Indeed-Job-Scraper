from bs4 import BeautifulSoup as bs
import requests
import time

# SOFTWARE DEVELOPER ROLE
# POSTED - 14 DAYS AGO
# PLATFORM - INDEED
# LOCATION - UK


# DESIGN
print(
    """
        JobberBot
                :                
               ;                
              :                 
              ;                 
             /                  
           o/                   
         ._/\___,                
             \                  
             /                   
             `     
    """ 
)

time.sleep(3)

base_url = 'https://uk.indeed.com'
URL = f'https://uk.indeed.com/jobs?q=software+developer&l=london&sc=0kf%3Aattr%28DSQF7%29%3B&fromage=14'

def Query_Jobs():

    html_body = requests.get(URL).text
    soup = bs(html_body, 'lxml')

    jobs = soup.find_all('div', class_ = 'job_seen_beacon')

    for job in jobs:

        company_name = job.find('span', class_ = 'companyName').text
        location = job.find('div', class_ = 'companyLocation').text
        #rating = job.find('span', class_='ratingsDisplay').text
        date_posted = job.find('span', class_ = 'date').text
        job_title = job.find('h2', class_= 'jobTitle').text
        job_desc = job.find('div', class_ = 'job-snippet').text
        job_url = job.find('a', class_ = 'jcs-JobTitle css-jspxzf eu4oa1w0').get('href')
        job_url_link = f'{base_url}{job_url}'
        

        print(f'Posted:- {date_posted[6:]}')
        print(f'Job Title:- {job_title}')
        print(f'Company Name:- {company_name}')
        print(f'Location:- {location}')
        print(f'More Info:- {job_url_link}')
        print(f'Description:- {job_desc}')
        print('\n')


while True:
    Query_Jobs()
    print(""" \n
                        (
                     (  ) (
                      )    )
         |||||||     (  ( (
        ( O   O )        )
 ____oOO___(_)___OOo____(
(_______________________)

REFRESHING... NEW BATCH COMING
    """)
    time.sleep(600)