import json
import requests
from pymongo import MongoClient
from DBWK import get_database

url = "https://steamcommunity.com/market/search/render/?query=&start=0&count=10000&search_descriptions=0&appid=730&norender=1"
response = requests.get(url)
data2 = json.loads(response.text)

# записати оновлені дані у файл data.json
with open('data2.json', 'w') as outfile:
    json.dump(data2, outfile)

# оновити дані в колекції MongoDB
db = get_database()
collection_name = db["user_1_items"]

for result in data2['results']:
    collection_name.update_many(
        {"name": result['name']}, 
        {"$set": result}, 
        upsert=True
    )