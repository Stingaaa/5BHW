import random
import main
from classes import eventManager as em

class Computer:
    
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def calcMove(self, player):
        match self.difficulty:
            case 0:
                return random.randint(1,5)

            case 1:
                e = em.getEvents()
                print(list(e[player.getID()].values())[3:8])
                print(list(e[player.getID()].values())[3:8].index(max(list(e[player.getID()].values())[3:8])))
                chosen = main.initItem(list(e[player.getID()].values())[3:].index(max(list(e[player.getID()].values())[3:8]))+1)
                counters = list(chosen.getStats().values())
                indices = [i for i, x in enumerate(counters) if x == -1]
                return indices[random.randint(0,1)]+1

            case 2:
                e = em.getEvents()
                pick = em.getPatterns()
                p = e[player.getID()]["patterns"]

                if pick["lastPick"] == "0":
                    return random.randint(1,5)

                evaluations = {"stone": 0, "scissor": 0, "paper": 0, "lizard": 0, "spock": 0}
                keys = list(evaluations.keys())
                for i in range(len(p)):
                    picks = list(p.keys())[i].split("-")
                    if picks[0] == pick["lastPick"]:
                        tempItem = main.initItem(int(picks[1]))
                        stats = tempItem.getStats()
                        for j in range(5):
                            if stats[keys[j]] == -1:
                                evaluations[keys[j]] += p[list(p.keys())[i]]
                bestItem = 0
                for i in range(1, len(evaluations)):
                    if evaluations[keys[bestItem]] < evaluations[keys[i]]:
                        bestItem = i
                return bestItem+1