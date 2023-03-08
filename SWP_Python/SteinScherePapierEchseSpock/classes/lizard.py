from classes.item import Item

class Lizard(Item):

    def __init__(self):
        self.name = "lizard"
        self.stats = {"stone":-1,"scissor":-1,"paper":1,"lizard":0,"spock":1}

    def itemName(self):
        return super().itemName()

    def getStats(self):
        return self.stats

    def checkStats(self, item2_name):
        return self.stats[item2_name]