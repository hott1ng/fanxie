from pymongo import MongoClient

class MongoMoudle:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client['fanxie']
        self.table = self.db['feed_record']
    def inser(self,data):
        self.table.insert_one(data)

    def search(self,data):
        self.table.find_one(data)

    def update(self,data):
        self.table.update_one(data)