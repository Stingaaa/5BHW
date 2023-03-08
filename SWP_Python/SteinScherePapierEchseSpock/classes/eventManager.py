import json
import os

def patternFile(create):
    if create:
        with open("SWP-Python\SteinScherePapierEchseSpock/temp.txt", "w") as e:
            e.write(json.dumps({"lastPick": "0", "doublePattern": "0-0"}))
    else:
        os.remove("SWP-Python\SteinScherePapierEchseSpock/temp.txt")

def getPatterns():
    with open("SWP-Python\SteinScherePapierEchseSpock/temp.txt", "r") as e:
        return json.load(e)

def savePatterns(patterns):
    with open("SWP-Python\SteinScherePapierEchseSpock/temp.txt", "w") as e:
        e.write(json.dumps(patterns))

def getEvents():
    with open("SWP-Python\SteinScherePapierEchseSpock\saves.txt", "r") as e:
        return json.load(e)

def logEvent(user_id, event, pattern=False):
    events = getEvents()
    events[user_id][event] += 1
    
    if pattern:
        patterns = getPatterns()
        dP = patterns["doublePattern"].split("-")
        dP = [int(dP[1]), list(events[user_id].keys()).index(event)-2]
        patterns["lastPick"] = str(dP[0])
        patterns["doublePattern"] = str(dP[0])+"-"+str(dP[1])
        savePatterns(patterns)
        if 0 in dP:
            None
        else:
            p = events[user_id]["patterns"]
            if str(dP[0])+"-"+str(dP[1]) in p:
                p[str(dP[0])+"-"+str(dP[1])] += 1
            else:
                p[str(dP[0])+"-"+str(dP[1])] = 1

    with open("SWP-Python\SteinScherePapierEchseSpock\saves.txt", "w") as e:
        e.write(json.dumps(events))
    return "Updated " + event + " to " + str(events[user_id][event])