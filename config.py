import os
from pymongo import MongoClient


p_key='542338e910129a6ee7bd9628af5c17038726eab86dddf944f648ed9df4362304'
dm_key="81a0af973a224f7361cf1454abecbc40fde3a65b8f022dbb0d874fe7a2c44e4c542338e910129a6ee7bd9628af5c17038726eab86dddf944f648ed9df4362304"
class Config:
    # ...
    STEAM_OAUTH_CLIENT_ID = os.environ.get('STEAM_OAUTH_CLIENT_ID')
    STEAM_OAUTH_CLIENT_SECRET = os.environ.get('STEAM_OAUTH_CLIENT_SECRET')
    STEAM_OAUTH_REDIRECT_URI = 'http://localhost:5000/login/steam/authorized'
    API_KEY='8386C327632B71BB13E0B9BD699E96BD'

def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   #"mongodb+srv://UaroslavH:BV9caZNzBmBPiNYQ@csgoskinexplorer.patitvp.mongodb.net/test"
   CONNECTION_STRING = 'mongodb+srv://UaroslavH:BV9caZNzBmBPiNYQ@csgoskinexplorer.patitvp.mongodb.net/test'
   client = MongoClient(CONNECTION_STRING)
   return client['CS_SE']



   """'mongodb://azure-web-project:M73MVy790iHsITudPP4Q1xOeGjKLLeDueOKDM3h9hzZm0zmU8t1Ffc0uhTBFGQ74wz43RE8Shc6oACDbPizDQw==@azure-web-project.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@azure-web-project@'"""
