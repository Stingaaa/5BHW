class Item:

    def __init__(self):
        self.name = "item"
        self.stats = {None: None}

    def itemName(self):
        return self.name

    def getStats(self):
        return self.stats

    def checkStats(self, item2_name):
        return self.stats[item2_name]