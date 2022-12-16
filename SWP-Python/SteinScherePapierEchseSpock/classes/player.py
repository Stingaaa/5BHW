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
            with open("SWP-Python\SteinScherePapierEchseSpock\saves.txt", "w") as e:
                e.write(json.dumps(events))
        
    def getID(self):
        return self.ID