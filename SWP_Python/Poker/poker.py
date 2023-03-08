import random

def generateStatistic():
    s = {"Royal Flush":0, "Straight Flush":0, "Four of a kind":0, "Full House":0, "Flush":0, "Straight":0, "Three of a kind":0, "Two Pair":0, "Pair":0, "Highest Number":0}
    return s

def generateCards():
    cards = []
    for i in range(0,52):
        cards.append(i)
    return cards

def pickCards(cards):
    for i in range(1,6):
        rand = random.randint(0, len(cards)-1)
        cards[len(cards)-i], cards[rand] = cards[rand], cards[len(cards)-i]
    return cards[len(cards)-5:len(cards)]

def sortToLowest(cards):
    for i in range(len(cards)):
        for j in range(len(cards)-1):
            if (cards[i]%13<cards[j]%13):
                cards[i], cards[j] = cards[j], cards[i]
    return cards

def checkHand(cardsUsed, showCards, statistic):
    if showCards == True:
        print(cardsUsed)
     
    cardsSorted = sortToLowest(cardsUsed)
    straight = False
    
    if(cardsSorted[0]%13+4 == cardsSorted[1]%13+3 == cardsSorted[2]%13+2 == cardsSorted[3]%13+1 and cardsSorted[0]%13+4 == cardsSorted[4]%13 or cardsSorted[0]%13 == cardsSorted[4]%13-12 and cardsSorted[0]%13):
        if(int(cardsUsed[0]/13) == int(cardsUsed[1]/13) == int(cardsUsed[2]/13) == int(cardsUsed[3]/13) == int(cardsUsed[4]/13) and cardsSorted[4]-cardsSorted[0]<13):
            if(cardsSorted[0]%13 == 8):
                statistic["Royal Flush"] += 1
                return #"Royal Flush"
            statistic["Straight Flush"] += 1
            return #"Straight Flush"
        straight = True
            
    for i in range(0,2):
        if(cardsSorted[i]%13 == cardsSorted[i+1]%13 == cardsSorted[i+2]%13 == cardsSorted[i+3]%13):
            statistic["Four of a kind"] += 1
            return #"There are four " + splitCard(cardsToNumbers[i])[0] + "s in your hand!"
    
    threeOfAKind = 0
    toak = False
    for i in range(0,3):
        if(cardsSorted[i]%13 == cardsSorted[i+1]%13 == cardsSorted[i+2]%13):
            threeOfAKind = cardsSorted[i]
            valsUnused = [0, 1, 2, 3, 4]
            valsUnused.remove(i), valsUnused.remove(i+1), valsUnused.remove(i+2)
            toak = True
            if(cardsSorted[valsUnused[0]]%13 == cardsSorted[valsUnused[1]]%13 and not cardsSorted[valsUnused[0]]%13 == threeOfAKind):
                statistic["Full House"] += 1
                return "Full House"#You have a full house of " + splitCard(cardsToNumbers[i])[0] + "s in " + str(threeOfAKind) + "s in your hand!"

    if toak == True:
        statistic["Three of a kind"] += 1
        return #"There are three " + threeOfAKind + "s in your hand!"

    if(int(cardsUsed[0]/13) == int(cardsUsed[1]/13) == int(cardsUsed[2]/13) == int(cardsUsed[3]/13) == int(cardsUsed[4]/13) and cardsSorted[4]-cardsSorted[0]<13):
        statistic["Flush"] += 1
        return #"You have a flush in your hand!"
                
    if(straight == True):
        statistic["Straight"] += 1
        return #"You have a straight in your hand!"
    
    for i in range(0,4):
        if(cardsSorted[i]%13 == cardsSorted[i+1]%13):
            for j in range(i+2,4):
                if(cardsSorted[j]%13 == cardsSorted[j+1]%13):
                    statistic["Two Pair"] += 1
                    return #"Two Pairs"
            statistic["Pair"] += 1 
            return #"Pair" 
    
    statistic["Highest Number"] += 1
    return #"Highest Card in your hand is a " +  cardsUsed[highest]

def pokerStatistic(count):
    statistic = generateStatistic()
    statisticP = generateStatistic()
    keys = list(statistic)
    for i in range(int(count)):
        checkHand(pickCards(generateCards()), False, statistic)
    for i in range(len(statistic)):
        statisticP[keys[i]] = statistic[keys[i]]/int(count)*100
    return str(statistic) + "\n\n" + str(statisticP)

def main():
    print("---------------------------------------------------------")
    print(checkHand(pickCards(generateCards()), True, generateStatistic()))
    print("---------------------------------------------------------")
    print(pokerStatistic(input("Ziehungen: ")))

if __name__ == '__main__':
    main()