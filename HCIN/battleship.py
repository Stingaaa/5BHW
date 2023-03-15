import random
from ships import small_ship, medium_ship, big_ship, huge_ship, Positions
import pygame

def initField():
    f = []
    for i in range(10):
        f.append([])
        for j in range(10):
            f[i].append("o")
    return f

def displayField(field):
    for i in range(10):
        line = ""
        for j in range(10):
            line += field[i][j]
        print(line)

def checkCollision(field, ship):
    for i in range(ship.length):
        match ship.positioning:
            case Positions.vertical:
                if ship.pos[1]+i > len(field)-1:
                    return True
                if field[ship.pos[0]][ship.pos[1]+i] == "x":
                    return True
            case Positions.horizontal:
                if ship.pos[0]+i > len(field[0])-1:
                    return True
                if field[ship.pos[0]+i][ship.pos[1]] == "x":
                    return True
    return False

def drawGrid(screen):
    blockSize = 50 #Set the size of the grid block
    for x in range(50, 550, blockSize):
        for y in range(50, 550, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, (255,255,255), rect, 1)
    for i in range(10):
        rect = pygame.Rect(70+50*i, 20, 20, 20)
        c = chr(65+i)
        screen.blit(pygame.font.Font(None, 24).render(c, True, (0,0,0)), (rect.x, rect.y))
    for i in range(10):
        rect = pygame.Rect(20, 70+50*i, 20, 20)
        screen.blit(pygame.font.Font(None, 24).render(str(i), True, (0,0,0)), (rect.x, rect.y))

def addToField(screen, field, ship, type=None, botOn=False, cnt=None):
    if checkCollision(field, ship):
        print("Cant place ship like that!")
        setShips(screen, field, type, botOn, cnt)
        return
    for i in range(ship.length):
        match ship.positioning:
            case Positions.vertical:
                field[ship.pos[0]][ship.pos[1]+i] = "x"
                pygame.draw.rect(screen, (200,100,150), pygame.Rect(ship.pos[0]*50+50, (ship.pos[1]+i)*50+50, 50, 50))
            case Positions.horizontal:
                field[ship.pos[0]+i][ship.pos[1]] = "x"
                pygame.draw.rect(screen, (200,100,150), pygame.Rect((ship.pos[0]+i)*50+50, ship.pos[1]*50+50, 50, 50))
        drawGrid(screen)
        if botOn == False:
            pygame.display.update()

def setShips(screen, playingField, shipType, botOn, cnt=2):
    if botOn:
        match shipType:
            case "small":
                for i in range(cnt):
                    pos = random.randint(0,9), random.randint(0,9)
                    direction = Positions.vertical if random.randint(0,1) == 0 else Positions.horizontal
                    s = small_ship(pos, direction)
                    addToField(screen, playingField, s, cnt-i)
                setShips(screen, playingField, "medium", botOn, 1)
            case "medium":
                for i in range(cnt):
                    pos = random.randint(0,9), random.randint(0,9)
                    direction = Positions.vertical if random.randint(0,1) == 0 else Positions.horizontal
                    s = medium_ship(pos, direction)
                    addToField(screen, playingField, s, cnt-i)
                setShips(screen, playingField, "big", botOn, 2)
            case "big":
                for i in range(cnt):
                    pos = random.randint(0,9), random.randint(0,9)
                    direction = Positions.vertical if random.randint(0,1) == 0 else Positions.horizontal
                    s = big_ship(pos, direction)
                    addToField(screen, playingField, s, cnt-i)
                setShips(screen, playingField, "huge", botOn, 1)
            case "huge":
                for i in range(cnt):
                    pos = random.randint(0,9), random.randint(0,9)
                    direction = Positions.vertical if random.randint(0,1) == 0 else Positions.horizontal
                    s = huge_ship(pos, direction)
                    addToField(screen, playingField, s, cnt-i)
        return    
    
    match shipType:
        case "small":
            for i in range(cnt):
                pygame.event.get()
                p = input("Position (x-y): ").split("-")
                pos = ord(p[0])-65, int(p[1])
                direction = Positions.vertical if int(input("Direction (vert. = 0; hor. = 1): ")) == 0 else Positions.horizontal
                s = small_ship(pos, direction)
                addToField(screen, playingField, s, cnt-i)
            setShips(screen, playingField, "medium", botOn, 1)
        case "medium":
            for i in range(cnt):
                pygame.event.get()
                p = input("Position (x-y): ").split("-")
                pos = ord(p[0])-65, int(p[1])
                direction = Positions.vertical if int(input("Direction (vert. = 0; hor. = 1): "))  == 0 else Positions.horizontal
                s = medium_ship(pos, direction)
                addToField(screen, playingField, s, cnt-i)
            setShips(screen, playingField, "big", botOn, 2)
        case "big":
            for i in range(cnt):
                pygame.event.get()
                p = input("Position (x-y): ").split("-")
                pos = ord(p[0])-65, int(p[1])
                direction = Positions.vertical if int(input("Direction (vert. = 0; hor. = 1): "))  == 0 else Positions.horizontal
                s = big_ship(pos, direction)
                addToField(screen, playingField, s, cnt-i)
            setShips(screen, playingField, "huge", botOn, 1)
        case "huge":
            for i in range(cnt):
                pygame.event.get()
                p = input("Position (x-y): ").split("-")
                pos = ord(p[0])-65, int(p[1])
                direction = Positions.vertical if int(input("Direction (vert. = 0; hor. = 1): "))  == 0 else Positions.horizontal
                s = huge_ship(pos, direction)
                addToField(screen, playingField, s, cnt-i)

def main():
    playingField = initField()
    enemyField = initField()
    pygame.init()
    size = 550, 550
    screen = pygame.display.set_mode(size)
    screen2 = pygame.display.set_mode(size)
    screen.fill((100,50,250))
    drawGrid(screen)
    pygame.display.update()
    setShips(screen2, enemyField, "small", True)
    displayField(enemyField)
    setShips(screen, playingField, "small", False)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
        drawGrid(screen)
        pygame.display.update()
    
if __name__ == "__main__":
    main()