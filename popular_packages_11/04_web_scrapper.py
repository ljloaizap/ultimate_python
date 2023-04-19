import requests
from bs4 import BeautifulSoup

URL = 'https://stackoverflow.com/questions'
response = requests.get(URL)
text = response.text

soup = BeautifulSoup(text, 'html.parser')
questions = soup.select('.s-post-summary')
for q in questions:
    title = q.select_one('.s-link').get_text()
    username = q.select_one('.s-user-card--link').get_text()
    # print(f'> [{username.strip()}]: {title}\n')

print(questions[0]['data-post-id'])
