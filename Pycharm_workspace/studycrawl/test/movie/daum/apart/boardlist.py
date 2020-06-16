# 제목
# 내용
# 작성일자
# 작성자


import requests
from bs4 import BeautifulSoup

cnt = 0
list_url = 'http://news.sarangbang.com/bbs.html?tab=story&p=2'
resp = requests.get(list_url)

if resp.status_code != 200:
    'Waring: Wrong URL'

soup = BeautifulSoup(resp.text, 'html.parser')

board_list = soup.select('tbody#bbsResult > tr > td a')
# print(board_list) # 제목뿐만 아니라... id같은 것도 지금 같이 출력되는 것을 확인 할 수 있다.

for i, href in enumerate(board_list):
    # print(i, href) # 홀수는 필요 없는 정보임을 알 수있다. 떼어내
    if(i % 2 ==0):
        cnt += 1
        # print(href['href']) # 현재 주소에 http://news.sarangbang.com/ 가 짤린 걸 확인할 수 있다.
        # print('http://news.sarangbang.com/'+href['href']) # 이렇게 하면 해결이 된다.

# 이제 아까 만든 한개의 페이지 호출을 각자 for 문 안의 if 절에서 써야 하기 때문에 나머지를 if 문 안에 넣어준다.

        # 1건의 게시글의 제목, 내용, 작성자, 작성일자 수집하는 코드

        url = 'http://news.sarangbang.com/'+href['href']
        resp = requests.get(url)

        soup = BeautifulSoup(resp.text, 'html.parser')
        #print(url)

        title = soup.select('h3.tit_view')[0].text
        print('TITLE ▶▶▶▶▶▶▶▶▶▶▶', title)
        contents = soup.select('div.bbs_view')
        print('CONTENTS ▶▶▶▶▶▶▶▶▶▶▶▶', contents[0].text.strip())

        date = soup.select('span.tit_cat')[1].text.strip()[:10] # 작성일자가 세개의 tit_cat 중 두번째에 항상 와야 이런식으로 가능. 구조가 항상 똑같아야한다.
                                                                # 연월일만 하고 싶으면 [:10]
                                                                # 만약에 다른 페이지 갔는데 이런 구조가 아니라면 어쩔수 없이 다른 형식으로 해야한다.
        print('DATE ▶▶▶▶▶▶▶▶▶▶▶', date)
        id = soup.select('a.name_more')
        print('WRITER ▶▶▶▶▶▶▶▶▶▶▶', id[0].text)

print('사랑방 부동산에서 {}건의 게시글을 수집하였습니다.'. format(cnt))