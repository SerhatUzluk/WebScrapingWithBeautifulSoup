import requests
from bs4 import BeautifulSoup

html = 'https://www.sikayetvar.com/mcdonalds'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/118.0.0.0 Safari/537.36'}
sayfa = requests.get(html, headers=headers)
bs = BeautifulSoup(sayfa.content, 'html.parser')
"""for comment in bs.findAll('p', {'class': 'complaint-description'}):
    if comment == bs.findAll('p', {'class': 'complaint-description'})[10]:
        break
    print(comment)"""
count = 0
for comment in bs.findAll('div', {'class': 'post-time'}):
    print(bs.findAll('p', {'class': 'complaint-description'})[count].getText(), comment.getText()[1:11], sep='\n')
    count += 1
    if comment.getText()[1:6] == '4 gün':
        break