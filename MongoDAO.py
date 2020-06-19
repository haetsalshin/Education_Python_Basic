from pymongo import MongoClient


class MongoDAO:

    def __init__(self): # 생성자
        self.client = MongoClient('127.0.0.1', 27017)
        self.db = self.client['local']
        self.collection = self.db.get_collection('naver')

    def mongo_wirte(self, data):
        print('>> mongoDB WRITE DATA:')
        self.collection.insert(data)

    def mongo_select_all(self):
        for one in self.collection.find({}, {'_id':0, 'content':1, 'score':1}):
            self.reply_list.append([one['title'], one['content'], one['score']])
        return self.reply_list