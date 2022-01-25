import pymongo
from pprint import pprint
import urllib
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_USERNAME = os.getenv("MONGO_USER")
MONGO_PASSWORD = os.getenv("MONGO_PASS")
MONGO_URI = os.getenv("MONGO_URI")



client = pymongo.MongoClient("mongodb+srv://" + MONGO_USERNAME + ":" + urllib.parse.quote(MONGO_PASSWORD) + MONGO_URI)

db = client.ScoreMap

def addUser(userId):
        db.ScoreMap.insert_one(
                {"discord_id": userId, "score": 0}
        )

def getCurrentScores():
        return list(db.ScoreMap.find({}))

def createNewImage(message):
        db.MessageIDtoUserID.insert_one(
                {"message_id" : message.id, "user_id" : message.author.id}
        )

def addScore(message_id):
        row = list(db.MessageIDtoUserID.find({'message_id' : message_id}))
        
        db.ScoreMap.update_one( {'discord_id': row[0]['user_id']},
                {
                        '$inc': {'score': 1}
                })
        

def removeScore(message_id):
        row = list(db.MessageIDtoUserID.find({'message_id' : message_id}))

        
        db.ScoreMap.update_one( {'discord_id': row[0]['user_id']},
                {
                        '$inc': {'score': -1}
                })


        


