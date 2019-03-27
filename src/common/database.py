import pymongo


class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    database = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.database = client["fullstack"]

    @staticmethod
    def insert(collection,data):
        Database.database[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.database[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.database[collection].find_one(query)