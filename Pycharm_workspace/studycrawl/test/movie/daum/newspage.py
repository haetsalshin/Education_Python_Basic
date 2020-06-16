# 다음뉴스  1~2페이지의 각각의 기사들의 내용을 수집

import requests
from bs4 import BeautifulSoup

url = 'https://news.daum.net/breakingnews/digital?page=10' # 10페이지 고정

cnt = 0
for i in range(1, 3):
    url = 'https://news.daum.net/breakingnews/digital?page={}'. format(i)

    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    url_list = soup.select('ul.list_allnews a.link_txt')
    print(len(url_list))
    print(url_list)

    for j in url_list:
        cnt += 1
        print(j['href'])
        url = j['href']
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, 'html.parser')
        title = soup.select('h3.tit_view')
        contents = soup.select('div#harmonyContainer p')

        text = ''
        for k in contents:

            text += k.text
        print("============================================================")
        print(title[0].text)
        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
        print(text)
print("▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶")
print('{}건의 뉴스기사를 수집하였습니다'. format(cnt))
print("▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶")