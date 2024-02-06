from pymongo import MongoClient


class MongoMoudle:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['yys']

    def insert(self, table, data):
        self.db[table].insert_one(data)
        return {"code": 0, "msg": "ok"}

    def search(self, table, select, inneed_data=None):
        return {"code": 0, "msg": self.db[table].find_one(select,inneed_data)}

    def update(self, table, select, data):
        self.db[table].update_one(select, data)
        return {"code": 0, "msg": "ok"}


if __name__ == '__main__':
    print(MongoMoudle().search('feed_time', {"phone": "18576265815"},{"last_time":1,"_id":0}))