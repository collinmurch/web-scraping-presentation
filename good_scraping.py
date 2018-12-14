import urllib.request as req
from bs4 import BeautifulSoup

page = req.urlopen('https://collinmurch.com')
soup = BeautifulSoup(page, 'html.parser')

for item in soup.find_all('a', href=True):
    print(item['href'])
