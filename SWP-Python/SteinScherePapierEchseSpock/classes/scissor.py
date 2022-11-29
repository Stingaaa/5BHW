from classes.item import Item

class Scissor(Item):

    def __init__(self):
        self.name = "scissor"
        self.stats = {"scissor":0,"stone":-1,"paper":1,"lizard":1,"spock":-1}

    def itemName(self):
        return self.name

    def checkStats(self, item2_name):
        return self.stats[item2_name]