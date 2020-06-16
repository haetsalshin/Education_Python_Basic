 # alt + shift + ^10 : console run
import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=104&oid=025&aid=0003009113'
# url사이트에 get방식으로 request를 하면
# return으로 사이트의 html code를 전달
resp = requests.get(url) # 해당 페이지에 가서 모든 소스 가져오기

if resp.status_code == 200: # 만약 위 url이 삭제된다던가 할 경우에. resp.status_code( 상태코드 ): respose 할 때 200번대 가 오면 정상. 나머지는 잘못된 것. 이를 표시해라
    resp.headers
else:
    print('잘못된 url입니다. 다시 입력해주세요')


soup = BeautifulSoup(resp.text,'html.parser') # 내가 원하는 기사 제목만 긁어오고 싶을 때. BeaufifulSoup 을 통해서.
title = soup.find('h3', id= 'articleTitle') # soup아 h3태그 중에서 id가 articleTilte을 찾아라 title에 담아줘~~
contents = soup.find('div', id="articleBodyContents")
print(title)
print(' ▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩ ')
print(contents.text.strip()) # strip() : 좌우 여백 없애기
print(title.text) # 코드 말고 text만 뽑고 싶을 때 .text를 붙여준다.



