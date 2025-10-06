from pymongo import MongoClient
from os import environ
MONGO_URI = environ.get('MONGO_URI','localhost')
client = MongoClient(MONGO_URI)
db = client["user_db"]
collection = db["test_user"]