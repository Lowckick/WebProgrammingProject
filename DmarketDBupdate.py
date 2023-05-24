import json
import requests
from pandas import DataFrame
from pymongo import MongoClient
from DBWK import get_database
import pymongo


dbname = get_database()
collection = dbname["user_1_items"]

# Задаємо URL-адресу, з якої потрібно отримати дані
url = 'https://api.dmarket.com/exchange/v1/market/items?gameId=a8db&limit=150&offset=0&orderBy=title&orderDir=desc&currency=USD&priceFrom=0&priceTo=0'
get_url=''
# Відправляємо запит і отримуємо дані з URL-адреси
response = requests.get(url)
data = response.json()

# Задаємо ім'я файлу для збереження даних у вигляді JSON-файлу
filename = 'data.json'

try:
    # Відкриваємо файл для читання
    with open(filename, 'r') as file:
        # Завантажуємо збережені дані з JSON-файлу
        saved_data = json.load(file)

    # Порівнюємо збережені дані з новими даними з URL-адреси
    if saved_data == data:
        print('Дані не змінилися, оновлення не потрібно')
    else:
        # Зберігаємо нові дані у вигляді JSON-файлу
        with open(filename, 'w') as file:
            json.dump(data, file)
            print('Дані збережено')
except FileNotFoundError:
    # Якщо файл не знайдено, зберігаємо дані у вигляді JSON-файлу
    with open(filename, 'w') as file:
        json.dump(data, file)
       
        for item in data:
            # Задаємо умову для оновлення запису у колекції
            filter = {'_id': item['_id']}

            # Оновлюємо запис у колекції
            collection.replace_one(filter, item, upsert=True)
        print('Дані збережено')

