import random
from classes import stone, scissor, paper, spock, lizard

def initItem(nr, msg):
    print(msg + "\n")
    match nr:
        case 1:
            return stone.Stone()
        case 2:
            return scissor.Scissor()
        case 3:
            return paper.Paper()
        case 4:
            return spock.Spock()
        case 5:
            return lizard.Lizard()
        case other:
            return initItem(int(input("Options:\nStone = 1, Scissor = 2, Paper = 3, Spock = 4, Lizard = 5\n\nChoose your Item: ")), "Hey you! Enter a fitting number!")

def checkMatch(nr):
    match nr:
        case -1:
            return "You lost!"
        case 0:
            return "It's a draw!"
        case 1:
            return "You won!"
        case other:
            return "Something went wrong!"

if __name__ == "__main__":
    computer = initItem(random.randint(1,5), "")
    player = initItem(int(input("Options:\nStone = 1, Scissor = 2, Paper = 3, Spock = 4, Lizard = 5\n\nChoose your Item: ")),"")
    print(player.itemName() + " vs " + computer.itemName())
    print(checkMatch(player.checkStats(computer.itemName())))