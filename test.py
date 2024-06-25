import requests
import json
import os

# year = 2021
# month = 12
# day = 13
# url = f'https://api.sportradar.us/nba/trial/v8/en/games/{year}/{month}/{day}/schedule.json'
# query_params = {'api_key': 'Hd2iYBwQMv8SHuOEcLuxC5dZE1eW4XHg4ZC8jxuE'}
# r = requests.get(url, params=query_params)
# print(r.json())

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "dummy.json")

with open(file_path) as fp:
    data = json.load(fp)

for game in data["games"]:
    print(game["away"]["alias"], " @ ", game["home"]["alias"])