# 다음에서 뉴스 한건의 기사와 내용을 수집

import requests
from bs4 import BeautifulSoup

# url은 내가 수집하고 싶은 데이터가 위치한 웹사이트 주소를 가리킴!
url = 'https://news.v.daum.net/v/20200616030529745'
resp = requests.get(url)

if resp.status_code == 200:
    print('Success')
else:
    print('Wrong URL')

# requests는 소스코드만 전부 가져오는 거고 거기서 우리는 기사 본문만 추출하고 싶음.
# 원하는 내용마다 추출하려면 Beautifulsoup을 사용해야함
# beaufifulsoup에  input으로 resp값(웹사이트의 소스코드 전체)을 전달
# html.parser : html 해석기. 아무리 requests가 값을 input했다 하더라도 이게 어떤 텍스트인지 모르기 때문에 웹사이트에서 긁어온 정보다 라는것을 알려주기 위하여
#               해당 해석기를 달아주는 것.
# soup에 웹사이트의 소스코드 전체가 저장
# soup.select()을 이용하여 원하는 정보만 추출
soup = BeautifulSoup(resp.text,'html.parser')

# print(soup)  soup에 긁어온 소스가 있는 것을 확인 할 수 있다.


# soup.find('tag명','선택자' ) 불편...
title=soup.select('h3.tit_view')   # 그래서 select사용.  결과 h3를 리스트로 불러 온 것을 알 수 있다.

print(title) # 아래와 비교해보기
print(title[0].text) # 리스트로 불러 왔기 때문에 0번지 값을 불러오라고 해줘야 온전히 글자만 불러들이는 것을 알 수 있다.

#기사 본문 가져오기
content=soup.select('div.news_view') # class 선택자 : 원래는 div, class="news_view" -> div.news_view
#print(contents[0].text.strip()) # strip은 사이사이에 있는 공백을 제거 할 수 없다. 앞 뒤에 있는 공백만 제거 가능.

contents=soup.select('div#harmonyContainer p') #harmonyContainer와 자손 관계인 p를 모두 읽어라.
# soup.select 은 1건이든 여러건이든 뭐든지 list 로 값을 저장을 한다.
print(contents) # p태그해서 list로 여러개 이루어져 있는 것을 알 수 있다.
print(' ▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩ ')

# 따라서 list 에 있는 값들을 for문으로 각 각 꺼내준다.
text=''
for i in contents:
    text += i.text

print(text)