import random

def generateStatistic():
    s = {"Royal Flush":0, "Straight Flush":0, "Four of a kind":0, "Full House":0, "Flush":0, "Straight":0, "Three of a kind":0, "Two Pair":0, "Pair":0, "Highest Number":0}
    return s
def generateCards():
    cards = []
    cardType = ["Clubs", "Diamonds", "Hearts", "Spades"]
    higherRanking = ["Jack", "Queen","King", "Ace"]
    for i in range(0,4):
        for j in range (2,15):
            if j > 10:
                cards.append(higherRanking[j-11] + " of " + cardType[i])
            else:
                cards.append(str(j) + " of " + cardType[i])
    return cards

def pickCards(cards):
    for i in range(1,6):
        rand = random.randint(0, len(cards)-1)
        cards[len(cards)-i], cards[rand] = cards[rand], cards[len(cards)-i]
    return cards[len(cards)-5:len(cards)]

def splitCard(card):
    return card.split(" of ")

def splitCardsToVals(card):
    cards = []
    for i in range(len(card)):
        cards.append(card[i].split(" of ")[0])
    return cards

def checkHand(cardsUsed, showCards):
    if showCards == True:
        print(cardsUsed)
    cardsToNumbers = []
    higherRanking = ["Jack", "Queen", "King", "Ace"]
    for i in range(len(cardsUsed)):
        val = cardsUsed[i].split(" of ")
        for j in range(len(higherRanking)):
            if(higherRanking[j] in str(val[0])):
                val[0] = j+11
        cardsToNumbers.append(str(val[0]) + " of " + val[1])
    
    types = ["Clubs", "Diamonds", "Hearts", "Spades"]
    for i in range(0,4):
        count = 0
        for j in range(0,5):
            if(splitCardsToVals(cardsToNumbers).__contains__(str(j+10)) and splitCard(cardsToNumbers[j])[1] == types[i]):
                count += 1
        if count == 5:
            statistic["Royal Flush"] += 1
            return #"You have a royal flush in your hand!"
    
    for i in range(0,4):
        for j in range(2,11):
            count1 = 0
            count2 = 0
            for k in range(0,5):
                if(splitCardsToVals(cardsToNumbers).__contains__(str(j+k)) and splitCard(cardsToNumbers[k])[1] == types[i]):
                    count1 += 1
                    count2 += 1
            if count1 == 5 and count2 == 5:
                statistic["Straight Flush"] += 1
                return #"You have a straight flush in your hand!"
    
    for i in range(0,2):
        for j in range(1+i,3):
            for k in range(1+j,4):
                for l in range(1+k,5):
                    if(int(splitCard(cardsToNumbers[i])[0]) == int(splitCard(cardsToNumbers[j])[0]) == int(splitCard(cardsToNumbers[k])[0]) == int(splitCard(cardsToNumbers[l])[0])):
                        statistic["Four of a kind"] += 1
                        return #"There are four " + splitCard(cardsToNumbers[i])[0] + "s in your hand!"
    
    threeOfAKind = 0
    toak = False
    for i in range(0,3):
        for j in range(1+i,4):
            for k in range(1+j,5):
                if(int(splitCard(cardsToNumbers[i])[0]) == int(splitCard(cardsToNumbers[j])[0]) == int(splitCard(cardsToNumbers[k])[0])):
                    threeOfAKind = int(splitCard(cardsToNumbers[i])[0])
                    toak = True
                    for l in range(len(cardsUsed)):
                        for m in range(l+1, len(cardsUsed)):
                            if(int(splitCard(cardsToNumbers[l])[0]) == int(splitCard(cardsToNumbers[m])[0]) and not int(splitCard(cardsToNumbers[l])[0]) == threeOfAKind):
                                statistic["Full House"] += 1
                                return #"You have a full house of " + splitCard(cardsToNumbers[i])[0] + "s in " + str(threeOfAKind) + "s in your hand!"
                                print("asd")

    if toak == True:
        statistic["Three of a kind"] += 1
        return #"There are three " + threeOfAKind + "s in your hand!"
    
    for i in range(0,4):
        count = 0
        for j in range(0,5):
            if(splitCard(cardsUsed[j])[1] == types[i]):
                count += 1
        if count == 5:
            statistic["Flush"] += 1
            return #"You have a flush in your hand!"
    
    for i in range(2,11):
        count = 0
        for j in range(0,5):
            if(splitCardsToVals(cardsToNumbers).__contains__(str(i+j))):
                count += 1
        if count == 5:
            statistic["Straight"] += 1
            return #"You have a straight in your hand!"
    
    pairs = []
    for i in range(len(cardsUsed)):
        for j in range(i+1, len(cardsUsed)):
            if(int(splitCard(cardsToNumbers[i])[0]) == int(splitCard(cardsToNumbers[j])[0])):
                pairs.append(splitCard(cardsUsed[i])[0])
    if len(pairs) == 1:
        statistic["Pair"] += 1
        return #"There is a pair of " + pairs[0] + "'s in your hand!"
    if len(pairs) == 2:
        statistic["Two Pair"] += 1
        return #"There are pairs of " + pairs[0] + "'s and " + pairs[1] + "'s in your hand!"
    
    highest = 0
    for i in range(1, len(cardsUsed)):
        vals = splitCard(cardsToNumbers[i])
        if(int(splitCard(cardsToNumbers[highest])[0]) < int(vals[0])):
            highest = i
    statistic["Highest Number"] += 1
    return #"Highest Card in your hand is a " +  cardsUsed[highest]

if __name__ == '__main__':
    statistic = generateStatistic()
    #print(generateCards())
    #print("---------------------------------------------------------")
    #print(pickCards(generateCards()))
    #print("---------------------------------------------------------")
    print(checkHand(pickCards(generateCards()), True))
    print("---------------------------------------------------------")
    for i in range(100000):
        checkHand(pickCards(generateCards()), False)
    print(statistic)