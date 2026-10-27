# import requests
# from bs4 import BeautifulSoup

# query = input("Enter job title: ")
# location = input("Enter location: ")

# url = f"https://www.indeed.com/jobs?q={query}&l={location}"
# response = requests.get(url)

# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, 'html.parser')
#     job_elements = soup.find_all('div', class_='jobsearch-SerpJobCard')

#     for job_element in job_elements:
#         title = job_element.find('h2', class_='title').text.strip()
#         location = job_element.find('span', class_='location').text.strip()
#         print(f"Title: {title}\nLocation: {location}\n")
# else:
#     print("Failed to fetch jobs. Check your connection or URL.")



import requests
from bs4 import BeautifulSoup

url = 'https://in.indeed.com/jobs?q=data+scientist&l=Bangalore%2C+Karnataka&sort=date'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}

response = requests.get(url, headers=headers)
print(response.status_code)

soup = BeautifulSoup(response.text, "lxml")
print(soup)

for jobs in soup.find_all('div', class_='job_seen_beacon'):
    try:
        job_title = jobs.h2.text.strip()
    except AttributeError:
        job_title = None
    print('Job title:', job_title)

    try:
       company_name = jobs.find('span', class_='css-92r8pb eu4oa1w0')
       company=company_name.text.strip() 
    except AttributeError:
       company = None
    print('company_name:', company)

    
    try:
       location_elem = jobs.find('div', class_='css-1p0sjhy eu4oa1w0')
       location_text = location_elem.text.strip()
    except AttributeError:
       location_text = None
    print('location:', location_text)

   
    try:
      summary_tag = jobs.find('div', class_='css-9446fg eu4oa1w0')
      summary=summary_tag.text.strip() 
    except AttributeError:
      summary = None
    print('summary:', summary)

    print('..............')
