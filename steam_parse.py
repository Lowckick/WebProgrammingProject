import json
from pandas import DataFrame
from pymongo import MongoClient
from flask import Flask, render_template, request, redirect, url_for, session
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

dbname2=get_database2()
collection_name3 = dbname2["Users"]
api_key="8386C327632B71BB13E0B9BD699E96BD"
user_id="76561198851176036"

steam_api_url = f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={api_key}&format=json&steamids={user_id}"
response = requests.get(steam_api_url)
data = response.json()
    
if 'response' in data and 'players' in data['response']:
    players = data['response']['players']
    if len(players) > 0:
        player = players[0]
        if 'avatarfull' in player:
            avatar_url = player['avatarfull']
                
            user_data = {
                'avatar_url': avatar_url
            }
            collection_name3.update_one({'user_id': user_id},
            {'$push': {'avatar_url':  avatar_url}})
                
    
        


