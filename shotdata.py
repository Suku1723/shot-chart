import json
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "pbyp.json")

with open(file_path) as fp:
    data = json.load(fp)


# Lists for missed and made shots
missed_list = ["twopointmiss", "threepointmiss"]
made_list = ["twopointmade", "threepointmade"]


# Dictionaries to store player missed and made data
# made_dict = {}
# missed_dict = {}


# Fills up the dictionaries
class MadeShots():

    made_dict = {}

    def __init__(self, periods) -> None:
        self.periods = periods

    def make(self):
        for i in range(len(self.periods)):
            for x in range(len(self.periods[i]["events"])):
                if self.periods[i]["events"][x]["event_type"] in made_list:
                    if self.periods[i]["events"][x]["location"]["coord_x"] > 564:
                        coord_x = 1128 - self.periods[i]["events"][x]["location"]["coord_x"]
                        coord_y = 600 - self.periods[i]["events"][x]["location"]["coord_y"]
                        if self.periods[i]["events"][x]["statistics"][0]["player"]["full_name"] in self.made_dict:
                            self.made_dict[self.periods[i]["events"][x]["statistics"][0]["player"]["full_name"]].append((coord_x/1.2, coord_y/1.2))
                        else:
                            self.made_dict[self.periods[i]["events"][x]["statistics"][0]["player"]["full_name"]] = []
                            self.made_dict[self.periods[i]["events"][x]["statistics"][0]["player"]["full_name"]].append((coord_x/1.2, coord_y/1.2))
                    else:
                        if self.periods[i]["events"][x]["statistics"][0]["player"]["full_name"] in self.made_dict:
                            self.made_dict[self.periods[i]["events"][x]["statistics"][0]["player"]["full_name"]].append((self.periods[i]["events"][x]["location"]["coord_x"]/1.2, self.periods[i]["events"][x]["location"]["coord_y"]/1.2))
                        else:
                            self.made_dict[self.periods[i]["events"][x]["statistics"][0]["player"]["full_name"]] = []
                            self.made_dict[self.periods[i]["events"][x]["statistics"][0]["player"]["full_name"]].append((self.periods[i]["events"][x]["location"]["coord_x"]/1.2, self.periods[i]["events"][x]["location"]["coord_y"]/1.2))
                
        

        return self.made_dict

class MissedShots(MadeShots):

    missed_dict = {}

    def __init__(self, periods) -> None:
        super().__init__(periods)

    def miss(self):
        for i in range(len(self.periods)):
            for x in range(len(self.periods[i]["events"])):
                if self.periods[i]["events"][x]["event_type"] in missed_list:
                    if self.periods[i]["events"][x]["location"]["coord_x"] > 564:
                        coord_x = 1128 - self.periods[i]["events"][x]["location"]["coord_x"]
                        coord_y = 600 - self.periods[i]["events"][x]["location"]["coord_y"]
                        if self.periods[i]["events"][x]["statistics"][0]["player"]["full_name"] in self.missed_dict:
                            self.missed_dict[self.periods[i]["events"][x]["statistics"][0]["player"]["full_name"]].append((coord_x/1.2, coord_y/1.2))
                        else:
                            self.missed_dict[self.periods[i]["events"][x]["statistics"][0]["player"]["full_name"]] = []
                            self.missed_dict[self.periods[i]["events"][x]["statistics"][0]["player"]["full_name"]].append((coord_x/1.2, coord_y/1.2))
                    else:
                        if self.periods[i]["events"][x]["statistics"][0]["player"]["full_name"] in self.missed_dict:
                            self.missed_dict[self.periods[i]["events"][x]["statistics"][0]["player"]["full_name"]].append((self.periods[i]["events"][x]["location"]["coord_x"]/1.2, self.periods[i]["events"][x]["location"]["coord_y"]/1.2))
                        else:
                            self.missed_dict[self.periods[i]["events"][x]["statistics"][0]["player"]["full_name"]] = []
                            self.missed_dict[self.periods[i]["events"][x]["statistics"][0]["player"]["full_name"]].append((self.periods[i]["events"][x]["location"]["coord_x"]/1.2, self.periods[i]["events"][x]["location"]["coord_y"]/1.2))
        
        return self.missed_dict


o = MadeShots(data["periods"])
print(o.make())

x = MissedShots(data["periods"])
print(x.miss())



# dict format

# formatted_dict = {
#     "player name": [
#                       {
#                           "event_type": "3ptmiss",
#                           "x_coord": 343,
#                           "y_coord": 234
#                           }
#                    ]
# }