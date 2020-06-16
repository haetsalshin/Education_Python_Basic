# 다음 뉴스 한 페이지에 있는 15건의 뉴스들의 제목와 내용 수집

import requests
from bs4 import BeautifulSoup

url = 'https://news.daum.net/breakingnews/digital'

resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')

# 전체 기사들 중 각각의 기사의 제목과 내용을 긁어오는 걸 해볼 것임.
# a태그가 하이퍼링크 거는 태그

url_list=soup.select('ul.list_allnews a.link_txt') # 처음에 a.link_txt했다가 len가 134개 나오는 걸 보고 우리가 가져오고 싶은 부분 태그인 ul.list_allnews 추가
# soup.select이므로 복수의 값이 리스트로 저장되어 있는 것을 확인 할 수 있다.
print(len(url_list)) # 잘가져왔나 갯수 확인해보기. 왜냐하면 내가 가져오고 싶은 부분만 태그가 걸려 있는게 아니라 그 페이지 전체에 해당 태그가 걸려 있을 수 있음.
print(url_list)


for i in url_list:
    print(i['href']) #우리가 뽑고 싶은 건 해당 하이퍼 링크 주소 뿐이므로 'href'
    url = i['href']
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    title = soup.select('h3.tit_view')
    contents = soup.select('div#harmonyContainer p')

    text = ''
    for i in contents:
        text += i.text
    print("===========================================================")
    print(title[0].text)
    print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
    print(text)
