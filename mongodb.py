from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from datetime import datetime

DBKey = os.environ['DBKey']
uri = f"mongodb+srv://{DBKey}/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

def adaklara_ekle(id, username, pp, adak, tarih=dt_string):

    mydb = client['Adaklar']

    mycol = mydb["Adak"]

    mydict = { "discord_id": id, "adak": adak, "tarih": dt_string, 'ad' : username, 'avatar' : pp }

    x = mycol.insert_one(mydict)

    print(x.inserted_id)

def get_adaklar():
    mydb = client["Adaklar"]
    mycol = mydb["Adak"]
    List = []
    for x in mycol.find():
        List.append(x)
    return List


