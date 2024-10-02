# database.py
from pymongo import MongoClient
import datetime

def get_database(db_name="project1"):
    client = MongoClient(host="localhost", port=27017)
    db = client[db_name]
    return db

def save_to_mongodb(db, data, collection_name="NewsAnalysis"):
    collection = db[collection_name]
    data["date"] = datetime.datetime.now()
    insert_id = collection.insert_one(data).inserted_id
    return insert_id
