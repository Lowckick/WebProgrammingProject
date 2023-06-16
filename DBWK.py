from pandas import DataFrame
from pymongo import MongoClient
from flask import Flask, render_template, request, redirect, url_for, session
import requests
from flask import request
from flask_oauthlib.client import OAuth
from json import dumps
from urllib.parse import urlencode
from config import get_database

app = Flask(__name__)
app.secret_key = 'your secret key here'
oauth = OAuth(app)
steam_openid_url = 'https://steamcommunity.com/openid/login'
dbname=get_database()
collection_name = dbname["user_1_items"]
collection_name2 = dbname["market_items"]




@app.route('/DB', methods=['GET', 'POST'])
def steam_database():
    if request.method == 'POST':
        name = request.form['name']
        sell_listings = request.form['sell_listings']
        sell_price_text = request.form['sell_price_text']
        sale_price_text = request.form['sale_price_text']
        type = request.form['type']
        icon_url = request.form['icon_url']

        new_item = {
            'name': name,
            'sell_listings': sell_listings,
            'sell_price_text': sell_price_text,
            'sale_price_text': sale_price_text,
            'type': type,
            'icon_url': icon_url,
        }
        

        collection_name.insert_one(new_item)

    data = collection_name.find({})
    return render_template('HTMLPage2_DB.html', data=data)

@app.route('/DMDB', methods=['GET', 'POST'])
def Dmarkt_database():
    if request.method == 'POST':
        i=0
        while i<50:
            name = request.form['objects'][i]['title']
            price = request.form['objects'][i]['price']['USD']
            suggested_price = request.form['objects'][i]['suggestedPrice']['USD']
            quality = request.form['objects'][i]['quality']
            type = request.form['objects'][i]['categoryPath']
            icon_url = request.form['objects'][i]['image']
            i+=1

        new_item = {
            'name': name,
            'price': price,
            'suggested_price': suggested_price,
            'quality': quality,
            'type': type,
            'icon_url': icon_url,
        }
        

        collection_name2.insert_one(new_item)

    data = collection_name2.find({})
    return render_template('HTMLPage2_DMDB.html', data=data)

@app.route('/', methods=['GET'])
def search_engine():
    return render_template('HTMLPage1.html')


@app.route('/About', methods=['GET'])
def about():
    return render_template('About.html')


@app.route('/Calculator', methods=['GET', 'POST'])
def calculator():
    return render_template('Calculator.html')

@app.route("/auth")
def auth_with_steam():

  params = {
    'openid.ns': "http://specs.openid.net/auth/2.0",
    'openid.identity': "http://specs.openid.net/auth/2.0/identifier_select",
    'openid.claimed_id': "http://specs.openid.net/auth/2.0/identifier_select",
    'openid.mode': 'checkid_setup',
    'openid.return_to': 'http://127.0.0.1:5000/authorize',
    'openid.realm': 'http://127.0.0.1:5000'
  }

  query_string = urlencode(params)
  auth_url = steam_openid_url + "?" + query_string

  print(auth_url)
  return redirect(auth_url)

@app.route("/authorize")
def authorize():
  print(request.args)
  steam_id = request.args.get('openid.identity').split('/')[-1]
  return dumps(request.args) + '<br><br><a href="http://localhost:5000/auth">Login with steam</a>'

@app.route("/profile")
def profile():
    return render_template('Profile.html')

if __name__ == '__main__':
    app.run(debug=True)
