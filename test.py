import inspect
import json
from pandas import DataFrame
from pymongo import MongoClient
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import requests
from flask import request
from flask_oauthlib.client import OAuth
from json import dumps
from urllib.parse import urlencode
from config import get_database, get_database2

app = Flask(__name__)
app.secret_key = 'your secret key here'
oauth = OAuth(app)
steam_openid_url = 'https://steamcommunity.com/openid/login'

dbname=get_database()
collection_name = dbname["user_1_items"]
collection_name2 = dbname["market_items"]
collection_name4= dbname["allskinslist"]
dbname2=get_database2()
collection_name3 = dbname2["Users"]
user_id='76561198851176036'

user_data = collection_name3.find_one({"user_id": user_id})

if user_data:
    username = user_data["username"]
    user_id=user_data["user_id"]
    api_code = user_data.get("api_code", "")  

    uitems = collection_name3.find({"user_id": user_id})
item=user_data['processed_items']
print(item)

    
