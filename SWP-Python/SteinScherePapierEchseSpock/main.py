import json
import random
from colorama import Fore, Back, Style
from classes import player, commandManager, stone, scissor, paper, spock, lizard

def initPlayer(val):
    return player.Player(val)

def initCM():
    c = commandManager.CommandManager()
    c.addCommand("-h",
                 "from colorama import Fore\nprint(Fore.LIGHTGREEN_EX + 'All commands:')\nfor cmd in self.commands:print(cmd+'\t-\t'+self.info[cmd])",
                 "Shows all available commands")
    c.addCommand("-s",
                "from colorama import Fore\nprint(Fore.LIGHTGREEN_EX + 'Game Statistic:')\nprint(Fore.LIGHTGREEN_EX + '----------')\nevents = json.load(open('SWP-Python\SteinScherePapierEchseSpock\saves.txt'))\ntotal = sum(list(events[0].values())[0:3])\n"
                + "print(Fore.LIGHTGREEN_EX + 'Wins: ' + str(events[0]['win']) + ' - ' + str(round(events[0]['win']/total*100, 2)) + '%')\nprint(Fore.LIGHTGREEN_EX + 'Draws: ' + str(events[0]['draw']) + ' - ' + str(round(events[0]['draw']/total*100, 2)) + '%')\nprint(Fore.LIGHTGREEN_EX + 'Loses: ' + str(events[0]['lose']) + ' - ' + str(round(events[0]['lose']/total*100, 2)) + '%')\nprint('----------')\n"
                + "print(Fore.LIGHTGREEN_EX + 'Number of items picked:')\nprint(Fore.LIGHTGREEN_EX + 'Stone: ' + str(events[0]['stone']) + ' - ' + str(round(events[0]['stone']/total*100, 2)) + '%')\nprint(Fore.LIGHTGREEN_EX + 'Scissor: ' + str(events[0]['scissor']) + ' - ' + str(round(events[0]['scissor']/total*100, 2)) + '%')\nprint(Fore.LIGHTGREEN_EX + 'Paper: ' + str(events[0]['paper']) + ' - ' + str(round(events[0]['paper']/total*100, 2)) + '%')\nprint(Fore.LIGHTGREEN_EX + 'Spock: ' + str(events[0]['spock']) + ' - ' + str(round(events[0]['spock']/total*100, 2)) + '%')\nprint(Fore.LIGHTGREEN_EX + 'Lizard: ' + str(events[0]['lizard']) + ' - ' + str(round(events[0]['lizard']/total*100, 2)) + '%')",
                "Shows a statistic of your played games")
    c.addCommand("-e",
                 "exit()",
                 "Ends the game")
    c.addCommand("-c",
                 "from colorama import Fore\nprint(Fore.LIGHTGREEN_EX + 'Available Colors:')\nconf = json.load(open('SWP-Python\SteinScherePapierEchseSpock\config.txt'))\nprint(Fore.LIGHTYELLOW_EX + conf[0][0] + Fore.LIGHTGREEN_EX + ' | ' + Fore.LIGHTMAGENTA_EX + conf[0][1] + Fore.LIGHTGREEN_EX + ' | ' + Fore.LIGHTCYAN_EX + conf[0][2] + Fore.LIGHTGREEN_EX + ' | ' + Fore.LIGHTWHITE_EX + conf[0][3])\ncol=input(Fore.LIGHTGREEN_EX + 'Enter a color: ')\nif col in conf[0]: conf[1]=col\nopen('SWP-Python\SteinScherePapierEchseSpock\config.txt', 'w').write(json.dumps(conf))\nif col not in conf[0]:print(Fore.LIGHTGREEN_EX + col + ' is not one of the available colors!')",
                 "Change the color off the output")
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
    print(Fore.WHITE + msg)
    commands = cm.commands
    if len(i) == 1:
        if ord(i) > 48 and ord(i) < 54:
            return initItem(int(i), "", p)
        else:
            print()
            return processInput(input(colorOfOutput() + "Options:\nStone = 1, Scissor = 2, Paper = 3, Spock = 4, Lizard = 5\nFor further commands enter -h\n\nChoose your Item: "),p,cm, "Hey you! Enter a valid number!")
    elif i in commands:
        cm.executeCommand(i)
        print()
        return processInput(input(colorOfOutput() + "Options:\nStone = 1, Scissor = 2, Paper = 3, Spock = 4, Lizard = 5\nFor further commands enter -h\n\nChoose your Item: "),p,cm, "")
    else:
        print()
        return processInput(input(colorOfOutput() + "Options:\nStone = 1, Scissor = 2, Paper = 3, Spock = 4, Lizard = 5\nFor further commands enter -h\n\nChoose your Item: "),p,cm, "Hey you! Enter a valid command!")
    
def checkMatch(nr, p):
    match nr:
        case -1:
            logEvent(p.getID(), "lose")
            return Fore.LIGHTRED_EX + "You lost!"
        case 0:
            logEvent(p.getID(), "draw")
            return Fore.LIGHTBLACK_EX + "It's a draw!"
        case 1:
            logEvent(p.getID(), "win")
            return Fore.LIGHTGREEN_EX + "You won!"
        case other:
            return "Something went wrong!"
        
def logEvent(user_id, event):    
    with open("SWP-Python\SteinScherePapierEchseSpock\saves.txt", "r") as e:
        events = json.load(e)
    
    events[user_id][event] += 1
    
    with open("SWP-Python\SteinScherePapierEchseSpock\saves.txt", "w") as e:
        e.write(json.dumps(events))
    return "Updated " + event + " to " + str(events[user_id][event])

def colorOfOutput():
    with open("SWP-Python\SteinScherePapierEchseSpock\config.txt", "r") as e:
        conf = json.load(e)
    match conf[1]:
        case "Yellow":
            return Fore.LIGHTYELLOW_EX
        case "Magenta":
            return Fore.LIGHTMAGENTA_EX
        case "Cyan":
            return Fore.LIGHTCYAN_EX
        case "White":
            return Fore.LIGHTWHITE_EX
        
def runGame():
    p = initPlayer(0)
    cM = initCM()
    computer = initItem(random.randint(1,5), "")
    player = processInput(input(colorOfOutput() + "Options:\nStone = 1, Scissor = 2, Paper = 3, Spock = 4, Lizard = 5\nFor further commands enter -h\n\nChoose your Item: "),p,cM)
    print(colorOfOutput() + player.itemName() + " vs " + computer.itemName())
    print(checkMatch(player.checkStats(computer.itemName()), p))
    runGame()

if __name__ == "__main__":
    runGame()