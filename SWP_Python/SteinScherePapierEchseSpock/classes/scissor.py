from classes.item import Item

class Scissor(Item):

    def __init__(self):
        self.name = "scissor"
        self.stats = {"stone":-1,"scissor":0,"paper":1,"lizard":1,"spock":-1}

    def itemName(self):
        return super().itemName()

    def getStats(self):
        return self.stats
        
    def checkStats(self, item2_name):
        return self.stats[item2_name]