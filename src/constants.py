import os
from pymongo import MongoClient


DB_URL = 'mongodb+srv://J4DGISH:J4gubhai@cluster0.ztfkzyi.mongodb.net/test'

JWT_SECRET_KEY = "aGVsbG93b3JsZA=="

MONGO_CLIENT = MongoClient(DB_URL)

SCHEDULER_JOB = os.getenv('SCHEDULER_JOB', False)

ADMINS = ['josephkevin04@gmail.com']
