import requests
from bs4 import BeautifulSoup
import movie.persistence2.MongoDAO as DAO


mDao =DAO.MongoDAO()

cnt = 0
page = 1

url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=134963&type=' \
      'after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=' \
      'false&isMileageSubscriptionReject=false&page=2'

resp = requests.get(url)

for page in range(1, 6):

    url_list= 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=134963&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}'.format(page)

    resp = requests.get(url_list)
    soup = BeautifulSoup(resp.text, 'html.parser')


    reply_list = soup.select('div.score_result li')

    if resp.status_code != 200:
        print('유효하지 않은 URL입니다.')

    for i, reply in enumerate(reply_list):



        content = reply.select('span#_filtered_ment_{}'.format(i))[0].text.strip()
        writer = reply.select('div.score_reple em')[0].text.strip()

        previous_writer = reply.select('div.score_reple em')[0].text.strip()
        cut_index = previous_writer.find('(')

        if cut_index > 0:
            writer = previous_writer[:cut_index]
        else:
            writer = previous_writer

        score = reply.select('div.star_score em')[0].text
        date = reply.select('div.score_reple em')[1].text[11:]

        print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
        print('내용 :', content)
        print('작성자 :', writer)
        print('점수 :', score)
        print('날짜', date)


        data = {'content': content,
                'writer': writer,
                'score': score,
                'reg_data': date}

        mDao.mongo_wirte((data))

        cnt += 1
print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
print('총 {}건의 영화 댓글을 수집하였습니다.'.format(cnt))