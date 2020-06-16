# 제목
# 내용
# 작성일자
# 작성자


import requests
from bs4 import BeautifulSoup


url = 'http://news.sarangbang.com/talk/bbs/free/163717?url=%2F%2Fnews.sarangbang.com%2Fbbs.html%3Ftab%3Dfree%26p%3D2'

resp = requests.get(url)

if resp.status_code == 200:
    print('Success')
else:
    print('Wrong URL')


soup = BeautifulSoup(resp.text, 'html.parser')
print(url)

title = soup.select('h3.tit_view')[0].text
print('TITLE ▶▶▶▶▶▶▶▶▶▶▶', title)
print('==================================================')
contents = soup.select('div.bbs_view')
print('CONTENTS ▶▶▶▶▶▶▶▶▶▶▶▶', contents[0].text.strip())

print('==================================================')
date = soup.select('span.tit_cat')[1].text.strip()[:10] # 작성일자가 세개의 tit_cat 중 두번째에 항상 와야 이런식으로 가능. 구조가 항상 똑같아야한다.
                                                        # 연월일만 하고 싶으면 [:10]
                                                        # 만약에 다른 페이지 갔는데 이런 구조가 아니라면 어쩔수 없이 다른 형식으로 해야한다.
print('DATE ▶▶▶▶▶▶▶▶▶▶▶', date)
print('==================================================')
id = soup.select('a.name_more')
print('WRITER ▶▶▶▶▶▶▶▶▶▶▶', id[0].text)
print('==================================================')