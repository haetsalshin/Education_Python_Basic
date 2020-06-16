# 작성자
# 평점
# 내용
# 날짜

import requests
from bs4 import BeautifulSoup


cnt = 0
page = 1
while True: # 만약 내가 이 프로그램을 샀다. 근데 영화 바뀔 때마다 페이지 수 봐서 range 숫자 바꿔줘야 한다..? 불편함. -> for를 while로! 그리고 21행으로 가서 나머지 작성.
    url = 'https://movie.daum.net/moviedb/grade?movieId=138347&type=netizen&page={}'. format(page) # 중간 id만 바꾸면 다른 영화영화 페이지로 갈 수 있다.
    resp = requests.get(url)


    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    reply_list = soup.select('div.review_info')

    if len(reply_list) == 0: # 다음 같은 경우에는 만약 마지막 그 다음 페이지를 가도 접근이 가능 하기 때문에 우리가 설정해둔 코멘트가 0개 일때 break하게 만들어준다.
        print('마지막 페이지에요...')
        break

    print(page, 'page *************************************************************************')

    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    for reply in reply_list:
        cnt += 1
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
    page += 1



print('수집한 영화댓글은 총 {}건 입니다'. format(cnt))