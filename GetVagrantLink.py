#!/usr/bin/python
from bs4 import BeautifulSoup
import requests

url = "https://www.vagrantup.com/downloads.html"

request = requests.get(url)

data = request.text

soup = BeautifulSoup(data, 'lxml')

for link in soup.find_all('a'):
    linkText = link.get('href')
    if 'deb' in linkText and 'x86_64' in linkText:
        print linkText
