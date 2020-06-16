# 제목
# 내용
# 작성일자
# 작성자


import requests
from bs4 import BeautifulSoup

cnt = 0

for page in range(1, 5):

    list_url = 'http://news.sarangbang.com/bbs.html?tab=story&p={}'. format(page)
    resp = requests.get(list_url)

    if resp.status_code != 200:
        'Waring: Wrong URL'

    soup = BeautifulSoup(resp.text, 'html.parser')

    board_list = soup.select('tbody#bbsResult > tr > td a:not(.name_more') # 여러가지 a태그 중에 name_more클래스는 포함시키지 않기 위하여 not 을 붙여준다. 작성자는 불러주지 않음.

    for i, href in enumerate(board_list):
              cnt += 1


         # 1건의 게시글의 제목, 내용, 작성자, 작성일자 수집하는 코드

        url = 'http://news.sarangbang.com/'+href['href']
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, 'html.parser')

        title = soup.select('h3.tit_view')[0].text
        print('TITLE ▶▶▶▶▶▶▶▶▶▶▶', title)
        contents = soup.select('div.bbs_view')
        print('CONTENTS ▶▶▶▶▶▶▶▶▶▶▶▶', contents[0].text.strip())

        date = soup.select('span.tit_cat')[1].text.strip()[:10]
        print('DATE ▶▶▶▶▶▶▶▶▶▶▶', date)
        id = soup.select('a.name_more')
        print('WRITER ▶▶▶▶▶▶▶▶▶▶▶', id[0].text)

print('사랑방 부동산에서 {}건의 게시글을 수집하였습니다.'. format(cnt))