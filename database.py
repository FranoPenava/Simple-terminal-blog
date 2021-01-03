import pymongo

class Database(object):
    # Default URI!
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None
    
    # Initializing our client. 
    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['fullstack']
    
    # Adding some useful methods: insert, remove, find, find_one. 
    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)
    
    @staticmethod
    def remove(collection, query):
        Database.DATABASE[collection].remove(query)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)
    
