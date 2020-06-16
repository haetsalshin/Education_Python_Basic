# 작성자
# 평점
# 내용
# 날짜

import requests
from bs4 import BeautifulSoup
cnt = 0
url = 'https://movie.daum.net/moviedb/grade?movieId=129134&type=netizen&page=1'

resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')
reply_list = soup.select('div.review_info') # 여기를 보면 특이하게 각 리플마다 div로 묶여 있는 것을 볼 수 있다. 그럼 for문을 통해서 각 div의 작성자, 평점, 내용, 날짜를 넣으면
                                            # 편리하게 입력할 수 있다.
print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
for reply in reply_list:
    writer = reply.select('em.link_profile')[0].text
    content = reply.select('p.desc_review')[0].text.strip()
    rate = reply.select('em.emph_grade')[0].text
    date = reply.select('span.info_append')[0].text.strip()

    print('작성자 :', writer)
    print('평점 :', rate)
    print('내용 :', content)
    index_val=date.index(',') # ,의 인덱스번호를 찾아서
    print('날짜 :', date[:index_val]) # ,(인덱스 번호) 앞까지만 읽어라.
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')


#writer = soup.select('em.link_profile')[0].text
#content = soup.select('p.desc_review')[0].text.strip()
#rate = soup.select('em.emph_grade')[0].text
#date = soup.select('span.info_append')[0].text.strip()[:10]



# print('작성자 :', writer)
#print('평점 :', rate)
#print('내용 :', content)
#print('날짜 :', date)