import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://realpython.com/'

response = requests.get(BASE_URL)
response_content = response.content 

print(response_content)