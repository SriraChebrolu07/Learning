# import requests
# from bs4 import BeautifulSoup

# url = 'https://www.facebook.com/#google_vignette'

# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')

# # Find all the <a> tags which contain links
# links = soup.find_all('a')

# for link in links:
#     print(link.text)









# import requests
# from bs4 import BeautifulSoup
# import csv

# url = 'https://www.facebook.com/#google_vignette'

# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')

# links = soup.find_all('a')

# # Open a CSV file in write mode with UTF-8 encoding
# with open('extracted_links.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     # Create a CSV writer object
#     csv_writer = csv.writer(csvfile)
    
#     # Write header row
#     csv_writer.writerow(['Link Text', 'Link URL'])
    
#     # Iterate through links and write them to the CSV file
#     for link in links:
#         link_text = link.text
#         link_url = link.get('href')
#         csv_writer.writerow([link_text, link_url])

# print("Data has been extracted and stored in extracted_links.csv")






# 1.Chat with websites using Groq and streamlit by using Rag langchain.
# 2.CrewAi an open LLM using the Groq API.  AI Agents for Analysis with customs tools.