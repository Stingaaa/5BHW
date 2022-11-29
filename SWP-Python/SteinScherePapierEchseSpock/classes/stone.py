from classes.item import Item

class Stone(Item):

    def __init__(self):
        self.name = "stone"
        self.stats = {"scissor":1,"stone":0,"paper":-1,"lizard":1,"spock":-1}

    def itemName(self):
        return super().itemName()

    def checkStats(self, item2_name):
        return self.stats[item2_name]