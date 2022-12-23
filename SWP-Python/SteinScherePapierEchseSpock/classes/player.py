import json

class Player:
    
    def __init__(self, name):
        with open("SWP-Python\SteinScherePapierEchseSpock\saves.txt", "r") as e:
            events = json.load(e)
    
        if name in events[0]:
            self.ID = events[0].index(name)+1
        else:
            self.ID = len(events[0])+1
            events[0].append(name)
            events.append({"win": 0, "draw": 0, "lose": 0, "stone": 0, "scissor": 0, "paper": 0, "lizard": 0, "spock": 0})
            with open("SWP-Python\SteinScherePapierEchseSpock\saves.txt", "w") as e:
                e.write(json.dumps(events))
        
    def getID(self):
        return self.ID