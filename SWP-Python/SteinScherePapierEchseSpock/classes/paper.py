from classes.item import Item

class Paper(Item):

    def __init__(self):
        self.name = "paper"
        self.stats = {"scissor":-1,"stone":1,"paper":0,"lizard":-1,"spock":1}

    def itemName(self):
        return self.name

    def checkStats(self, item2_name):
        return self.stats[item2_name]