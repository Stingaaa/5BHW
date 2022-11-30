import json

dict = {"test":1, "test2":3}

with open("SWP-Python\SteinScherePapierEchseSpock\saves.txt", "w") as t:
    t.write(json.dumps(dict))
    
with open("SWP-Python\SteinScherePapierEchseSpock\saves.txt", "r") as t:
    test = json.load(t)
    print(test["test2"])