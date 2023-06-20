import pymongo
import requests

# Connect to MongoDB
client = pymongo.MongoClient("mongodb+srv://UaroslavH:BV9caZNzBmBPiNYQ@csgoskinexplorer.patitvp.mongodb.net/test")
db = client["Users_info"]
users = db["Users"]

# Get user ID and username from MongoDB
user = users.find_one({"username": "IMJK"})
steam_id = user["user_id"]
username = user["username"]

# Get user profile information from Steam API
profile_url = f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=8386C327632B71BB13E0B9BD699E96BD&steamids={steam_id}"
response = requests.get(profile_url)
profile_data = response.json()["response"]["players"][0]
avatar_url = profile_data["avatarfull"]

# Get user CS:GO inventory from Steam API
inventory_url = f"https://steamcommunity.com/profiles/{steam_id}/inventory/json/730/2"
response = requests.get(inventory_url)
inventory_data = response.json()["rgDescriptions"]
csgo_items = []
for item in inventory_data.values():
    if item["appid"] == 730:
        csgo_items.append(item["name"])

# Display user information on a web page
html = f"""
<html>
<head>
    <title>{username}'s Steam Profile</title>
</head>
<body>
    <h1>{username}'s Steam Profile</h1>
    <img src="{avatar_url}">
    <h2>CS:GO Skins</h2>
    <ul>
"""
for item in csgo_items:
    html += f"<li>{item}</li>"
html += """
    </ul>
</body>
</html>
"""

print(html)