from classes.item import Item

class Spock(Item):

    def __init__(self):
        self.name = "spock"
        self.stats = {"stone":1,"scissor":1,"paper":-1,"lizard":-1,"spock":0}

    def itemName(self):
        return super().itemName()

    def getStats(self):
        return self.stats
        
    def checkStats(self, item2_name):
        return self.stats[item2_name]