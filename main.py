from bs4 import BeautifulSoup as bs
import requests
import time

def print_banner():
    print("JobberBot")


def fetch_html(url):
    response = requests.get(url)
    return response.text


def parse_jobs(html_body):
    soup = bs(html_body, 'lxml')
    jobs = soup.find_all('div', class_='job_seen_beacon')
    return jobs


def extract_job_details(job):
    company_name = job.find('span', class_='companyName').text
    location = job.find('div', class_='companyLocation').text
    date_posted = job.find('span', class_='date').text
    job_title = job.find('h2', class_='jobTitle').text
    job_desc = job.find('div', class_='job-snippet').text
    job_url = job.find('a', class_='jcs-JobTitle css-jspxzf eu4oa1w0').get('href')
    job_url_link = f'{base_url}{job_url}'
    return company_name, location, date_posted, job_title, job_desc, job_url_link


def print_job_details(details):
    company_name, location, date_posted, job_title, job_desc, job_url_link = details
    print(f'Posted: {date_posted[6:]}')
    print(f'Job Title: {job_title}')
    print(f'Company Name: {company_name}')
    print(f'Location: {location}')
    print(f'More Info: {job_url_link}')
    print(f'Description: {job_desc}')
    print('\n')


def query_jobs():
    html_body = fetch_html(URL)
    jobs = parse_jobs(html_body)
    for job in jobs:
        details = extract_job_details(job)
        print_job_details(details)


# Constants
base_url = 'https://uk.indeed.com'
URL = 'https://uk.indeed.com/jobs?q=software+developer&l=london&sc=0kf%3Aattr%28DSQF7%29%3B&fromage=14'

def main():
    print_banner()
    while True:
        query_jobs()
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


# Call the main function to execute the code
main()