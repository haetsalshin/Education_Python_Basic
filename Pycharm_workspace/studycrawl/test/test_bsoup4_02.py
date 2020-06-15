import requests
from bs4 import BeautifulSoup

url = 'https://news.v.daum.net/v/20200615150127042'

resp = requests.get(url)

if resp.status_code == 200:
    resp.headers
else:
    print('잘못된 url 입니다. 다시 입력해주세요.')

soup = BeautifulSoup(resp.text,'html.parser')
title = soup.find('h3',id="cSub")
contents = soup.find('div',id="harmonyContainer")
print(title)
print('===================================================')
print(contents.text.strip())