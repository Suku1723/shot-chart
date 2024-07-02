import requests
import json
import os
from key import query_params

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "dummy.json")

with open(file_path) as fp:
    data = json.load(fp)

class DailyGames:
    def __init__(self, year, month, day) -> None:
        self.year = year
        self.month = month
        self.day = day
    
    def get_games(self):
        url = f'https://api.sportradar.us/nba/trial/v8/en/games/{self.year}/{self.month}/{self.day}/schedule.json'
        r = requests.get(url, params=query_params)
        data2 = r.json()
        list = []
        for game in data2["games"]:
            list.append(f"{game['away']['alias']} @ {game['home']['alias']}")
        return list

    def get_dummy_data(self):
        games_list = []
        for game in data["games"]:
            games_list.append(f"{game['away']['alias']} @ {game['home']['alias']}")
        return games_list