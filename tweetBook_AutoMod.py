import certifi
from pymongo import MongoClient
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
load_dotenv()

ConnectString = os.getenv('CONNECTION_STRING')
cluster = MongoClient(ConnectString, tlsCAFile=certifi.where())
db = cluster["socialMedia"]["messages"]
all = db.find({})
today = datetime.now()
day = timedelta(days=30)
lastMonth = today - day

count = db.count_documents({})

print("Now: ", today.strftime("%x"))
print("Last Month: ", lastMonth.strftime("%x"))

for messages in all:
    try:
        if lastMonth.strftime("%x") >= messages["date"]:
            db.delete_one(messages)
    except:
        pass



query = db.find({"date": lastMonth.strftime("%x")})
