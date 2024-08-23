import requests
from key import query_params

# Lists for missed and made shots
missed_list = ["twopointmiss", "threepointmiss"]
made_list = ["twopointmade", "threepointmade"]

# Meant for fetching the list of daily games on the calendar date
class DailyGames:
    def __init__(self, year, month, day) -> None:
        self.year = year
        self.month = month
        self.day = day
    
    def get_games(self):
        url = f'https://api.sportradar.us/nba/trial/v8/en/games/{self.year}/{self.month}/{self.day}/schedule.json'
        r = requests.get(url, params=query_params)
        data = r.json()
        list = {}
        for game in data['games']:
            if game['status'] == 'unnecessary':
                continue
            list[f"{game['away']['alias']} @ {game['home']['alias']}"] = game['id']
        return list

"""
Doesn't return the available roster, but the
players that took shots in the game
"""
class Players:

    def __init__(self, id) -> None:
        self.id = id
        url = f'https://api.sportradar.us/nba/trial/v8/en/games/{self.id}/pbp.json'
        r = requests.get(url, params=query_params)
        data = r.json()
        ms = MadeShots(data['periods'])
        mis = MissedShots(data['periods'])
        self.Made = ms.make()
        self.Missed = mis.miss()
        self.players = []
    
    def game_data(self):
        self.players = [player for player in self.Made]
        for player in self.Missed:
            if player not in self.players:
                self.players.append(player)
        return self.players


"""
Returns the dictionary for player
along with list of (x, y)
coordinates for a made shot
"""
class MadeShots():

    def __init__(self, periods) -> None:
        self.periods = periods
        self.made_dict = {}

    def make(self):
        for i in range(len(self.periods)):
            for x in range(len(self.periods[i]["events"])):
                if self.periods[i]["events"][x]["event_type"] in made_list:
                    for y in range(len(self.periods[i]["events"][x]["statistics"])):
                        if self.periods[i]["events"][x]["location"]["coord_x"] > 564:
                            coord_y = 1128 - self.periods[i]["events"][x]["location"]["coord_x"]
                            coord_x = 600 - self.periods[i]["events"][x]["location"]["coord_y"]
                            if self.periods[i]["events"][x]["statistics"][y]["type"] == "fieldgoal":
                                if self.periods[i]["events"][x]["statistics"][y]["player"]["full_name"] in self.made_dict:
                                    self.made_dict[self.periods[i]["events"][x]["statistics"][y]["player"]["full_name"]].append((coord_x, coord_y))
                                else:
                                    self.made_dict[self.periods[i]["events"][x]["statistics"][y]["player"]["full_name"]] = []
                                    self.made_dict[self.periods[i]["events"][x]["statistics"][y]["player"]["full_name"]].append((coord_x, coord_y))
                        else:
                            if self.periods[i]["events"][x]["statistics"][y]["type"] == "fieldgoal":
                                if self.periods[i]["events"][x]["statistics"][y]["player"]["full_name"] in self.made_dict:
                                    self.made_dict[self.periods[i]["events"][x]["statistics"][y]["player"]["full_name"]].append((self.periods[i]["events"][x]["location"]["coord_y"], self.periods[i]["events"][x]["location"]["coord_x"]))
                                else:
                                    self.made_dict[self.periods[i]["events"][x]["statistics"][y]["player"]["full_name"]] = []
                                    self.made_dict[self.periods[i]["events"][x]["statistics"][y]["player"]["full_name"]].append((self.periods[i]["events"][x]["location"]["coord_y"], self.periods[i]["events"][x]["location"]["coord_x"]))
        
        return self.made_dict


"""
Returns the dictionary for player
along with list of (x, y)
coordinates for a missed shot
"""
class MissedShots(MadeShots):

    def __init__(self, periods) -> None:
        super().__init__(periods)
        self.missed_dict = {}

    def miss(self):
        for i in range(len(self.periods)):
            for x in range(len(self.periods[i]["events"])):
                if self.periods[i]["events"][x]["event_type"] in missed_list:
                    for y in range(len(self.periods[i]["events"][x]["statistics"])):
                        if self.periods[i]["events"][x]["location"]["coord_x"] > 564:
                            coord_y = 1128 - self.periods[i]["events"][x]["location"]["coord_x"]
                            coord_x = 600 - self.periods[i]["events"][x]["location"]["coord_y"]
                            if self.periods[i]["events"][x]["statistics"][y]["type"] == "fieldgoal": 
                                if self.periods[i]["events"][x]["statistics"][y]["player"]["full_name"] in self.missed_dict:
                                    self.missed_dict[self.periods[i]["events"][x]["statistics"][y]["player"]["full_name"]].append((coord_x, coord_y))
                                else:
                                    self.missed_dict[self.periods[i]["events"][x]["statistics"][y]["player"]["full_name"]] = []
                                    self.missed_dict[self.periods[i]["events"][x]["statistics"][y]["player"]["full_name"]].append((coord_x, coord_y))
                        else:
                            if self.periods[i]["events"][x]["statistics"][y]["type"] == "fieldgoal":
                                if self.periods[i]["events"][x]["statistics"][y]["player"]["full_name"] in self.missed_dict:
                                    self.missed_dict[self.periods[i]["events"][x]["statistics"][y]["player"]["full_name"]].append((self.periods[i]["events"][x]["location"]["coord_y"], self.periods[i]["events"][x]["location"]["coord_x"]))
                                else:
                                    self.missed_dict[self.periods[i]["events"][x]["statistics"][y]["player"]["full_name"]] = []
                                    self.missed_dict[self.periods[i]["events"][x]["statistics"][y]["player"]["full_name"]].append((self.periods[i]["events"][x]["location"]["coord_y"], self.periods[i]["events"][x]["location"]["coord_x"]))
        
        return self.missed_dict