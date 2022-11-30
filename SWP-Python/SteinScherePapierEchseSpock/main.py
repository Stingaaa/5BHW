import json
import random
from classes import player, commandManager, stone, scissor, paper, spock, lizard

def initPlayer(val):
    return player.Player(val)

def initCM():
    c = commandManager.CommandManager()
    c.addCommand("-h",
                 "print('All commands:')\nfor cmd in self.commands:print(cmd+'\t-\t'+self.info[cmd])",
                 "Shows all available commands")
    c.addCommand("-s",
                "print('Game Statistic:')\nprint('----------')\nevents = json.load(open('SWP-Python\SteinScherePapierEchseSpock\saves.txt'))\ntotal = sum(list(events[0].values())[0:3])\n"
                + "print('Wins: ' + str(events[0]['win']) + ' - ' + str(round(events[0]['win']/total*100, 2)) + '%')\nprint('Draws: ' + str(events[0]['draw']) + ' - ' + str(round(events[0]['draw']/total*100, 2)) + '%')\nprint('Loses: ' + str(events[0]['lose']) + ' - ' + str(round(events[0]['lose']/total*100, 2)) + '%')\nprint('----------')\n"
                + "print('Number of items picked:')\nprint('Stone: ' + str(events[0]['stone']) + ' - ' + str(round(events[0]['stone']/total*100, 2)) + '%')\nprint('Scissor: ' + str(events[0]['scissor']) + ' - ' + str(round(events[0]['scissor']/total*100, 2)) + '%')\nprint('Paper: ' + str(events[0]['paper']) + ' - ' + str(round(events[0]['paper']/total*100, 2)) + '%')\nprint('Spock: ' + str(events[0]['spock']) + ' - ' + str(round(events[0]['spock']/total*100, 2)) + '%')\nprint('Lizard: ' + str(events[0]['lizard']) + ' - ' + str(round(events[0]['lizard']/total*100, 2)) + '%')",
                "Shows a statistic of your played games")
    c.addCommand("-e",
                 "exit()",
                 "Ends the game")
    return c

def initItem(nr, msg="", p=None):
    print(msg + "\n")
    match nr:
        case 1:
            if p != None: 
                id = p.getID()
                logEvent(id, "stone")
            return stone.Stone()
        case 2:
            if p != None:
                id = p.getID()
                logEvent(id, "scissor")
            return scissor.Scissor()
        case 3:
            if p != None:
                id = p.getID()
                logEvent(id, "paper")
            return paper.Paper()
        case 4:
            if p != None:
                id = p.getID()
                logEvent(id, "spock")
            return spock.Spock()
        case 5:
            if p != None: 
                id = p.getID()
                logEvent(id, "lizard")
            return lizard.Lizard()

def processInput(i, p, cm, msg=""):
    print(msg)
    commands = cm.commands
    if len(i) == 1:
        if ord(i) > 48 and ord(i) < 54:
            return initItem(int(i), "", p)
        else:
            print()
            return processInput(input("Options:\nStone = 1, Scissor = 2, Paper = 3, Spock = 4, Lizard = 5\nFor further commands enter '-h'\n\nChoose your Item: "),p,cm, "Hey you! Enter a valid number!")
    elif i in commands:
        cm.executeCommand(i)
        print()
        return processInput(input("Options:\nStone = 1, Scissor = 2, Paper = 3, Spock = 4, Lizard = 5\nFor further commands enter '-h'\n\nChoose your Item: "),p,cm, "")
    else:
        print()
        return processInput(input("Options:\nStone = 1, Scissor = 2, Paper = 3, Spock = 4, Lizard = 5\nFor further commands enter '-h'\n\nChoose your Item: "),p,cm, "Hey you! Enter a valid command!")
    
def checkMatch(nr, p):
    match nr:
        case -1:
            logEvent(p.getID(), "lose")
            return "You lost!"
        case 0:
            logEvent(p.getID(), "draw")
            return "It's a draw!"
        case 1:
            logEvent(p.getID(), "win")
            return "You won!"
        case other:
            return "Something went wrong!"
        
def logEvent(user_id, event):    
    with open("SWP-Python\SteinScherePapierEchseSpock\saves.txt", "r") as e:
        events = json.load(e)
    
    events[user_id][event] += 1
    
    with open("SWP-Python\SteinScherePapierEchseSpock\saves.txt", "w") as e:
        e.write(json.dumps(events))
    return "Updated " + event + " to " + str(events[user_id][event])
        
def runGame():
    p = initPlayer(0)
    cM = initCM()
    computer = initItem(random.randint(1,5), "")
    player = processInput(input("Options:\nStone = 1, Scissor = 2, Paper = 3, Spock = 4, Lizard = 5\nFor further commands enter '-h'\n\nChoose your Item: "),p,cM)
    print(player.itemName() + " vs " + computer.itemName())
    print(checkMatch(player.checkStats(computer.itemName()), p))
    runGame()

if __name__ == "__main__":
    runGame()