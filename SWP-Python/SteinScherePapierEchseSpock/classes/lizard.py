from classes.item import Item

class Lizard(Item):

    def __init__(self):
        self.name = "lizard"
        self.stats = {"scissor":-1,"stone":-1,"paper":1,"lizard":0,"spock":1}

    def itemName(self):
        return super().itemName()

    def checkStats(self, item2_name):
        return self.stats[item2_name]