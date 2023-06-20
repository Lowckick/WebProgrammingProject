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

@app.route("/profile/<user_id>")
def profile(user_id):
    user_data = collection_name3.find_one({"user_id": user_id})


    if user_data:
        username = user_data["username"]
        user_id=user_data["user_id"]
        api_code = user_data.get("api_code", "")  

        uitems = collection_name3.find({"user_id": user_id})

        steam_api_url = f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={api_code}&format=json&steamids={username}"
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
    
        
                
        return render_template("profile.html", username=username, api_code=api_code, uitems=uitems, user_id=user_id)
    else:
        return "User not found."



@app.route("/profile/<user_id>", methods=["POST"])
def update_profile(user_id):
    api_code = request.form.get("api_code")
    collection_name3.update_one({"user_id": user_id}, {"$set": {"api_code": api_code}}, upsert=True)

    

    
    return "API code updated successfully!"





@app.route("/update_inventory/<user_id>", methods=["POST"])
def update_inventory(user_id):
    url = f"http://steamcommunity.com/inventory/{user_id}/730/2?l=english&count=5000"
    back=f"/profile/{user_id}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        items = data["descriptions"]

        parsed_items = []
        tc=[]
        total_countdata=data["total_inventory_count"]
        tc.append(total_countdata)

        for item in items:
            if item["type"]!="Base Grade Container":
                inspect_link=data['actions']['link']
            else:
                inspect_link='Impossible for a case'
            item_data = {

                "market_name": item["market_name"],   
                "tradable": item['tradable'],  
                "icon_url": item["icon_url"],
                "link": inspect_link,
                "type": item['type']
             }
            parsed_items.append(item_data)
            output_data = {
                'processed_items': parsed_items
            }
        collection_name3.update_one(
            {'user_id': user_id},
            {'$push': {'total_items_count': {'$each': tc}}}
        )
        collection_name3.update_one(
            {'user_id': user_id},
            {'$push': {'processed_items': {'$each': parsed_items}}})

        return redirect(back)
    
    else:
        return redirect(back)



@app.route("/store/<user_id>")
def store(user_id):
    items = collection_name.find()

    user = collection_name3.find_one({'user_id': user_id})
    balance = user['balance']

    return render_template('store.html', items=items, balance=balance)

@app.route('/buy/<name>/<user_id>')
def buy_item(name, user_id):
    # Fetching item details from the database
    back2=f'/store/{user_id}'
    item = collection_name.find_one({'name': name})

  
    # Fetching user details from the database
    user = collection_name3.find_one({'user_id': user_id})
    balance = user['balance']
    sell_price = item.get('sell_price')  # Use .get() to handle potential missing key

    if sell_price is None:
        return 'Sell price not available for the item.'

    user_items = user['processed_items']

    if balance >= (sell_price / 100):
        new_balance = balance - (sell_price / 100)
        collection_name3.update_one({'user_id': user_id}, {'$set': {'balance': new_balance}})

        # Adding the item to the user's items collection
        user_items.append(item)
        collection_name.delete_one({'name': name})
        collection_name3.update_one({'user_id': user_id}, {'$set': {'processed_items': user_items}})

        return redirect(back2)
    else:
        return 'Insufficient balance to purchase the item.'



if __name__ == '__main__':
    app.run(debug=True)
