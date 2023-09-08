import requests
from bs4 import BeautifulSoup


url = "https://https://www.youtube.com/"
r = requests.get(url)

print(r)

soup = BeautifulSoup(r.content, 'com')
title = soup.find_all('logo', {'class': 'style-scope ytd-logo'})
print(title)
print(title[0].getText())

for t in title:
      print(t.getText())