import json
import sys
import time
import pandas
import pygame as pg
import pygame_menu
import numpy as np
from matplotlib import cm
from matplotlib import pyplot as plt
import random
from colorama import Fore, Back, Style
from classes import player, eventManager as em, stone, scissor, paper, spock, lizard, computer
from screeninfo import get_monitors

def initPlayer(val):
    return player.Player(val)

def initItem(nr, msg="", p=None):
    print(msg + "\n")
    match nr:
        case 1:
            if p != None: 
                id = p.getID()
                em.logEvent(id, "stone", True)
            return stone.Stone()
        case 2:
            if p != None:
                id = p.getID()
                em.logEvent(id, "scissor", True)
            return scissor.Scissor()
        case 3:
            if p != None:
                id = p.getID()
                em.logEvent(id, "paper", True)
            return paper.Paper()
        case 4:
            if p != None:
                id = p.getID()
                em.logEvent(id, "lizard", True)
            return lizard.Lizard()
        case 5:
            if p != None: 
                id = p.getID()
                em.logEvent(id, "spock", True)
            return spock.Spock()

def checkMatch(nr, p):
    match nr:
        case -1:
            em.logEvent(p.getID(), "lose")
            return Fore.LIGHTRED_EX + "You lost!"
        case 0:
            em.logEvent(p.getID(), "draw")
            return Fore.LIGHTBLACK_EX + "It's a draw!"
        case 1:
            em.logEvent(p.getID(), "win")
            return Fore.LIGHTGREEN_EX + "You won!"
        case other:
            return "Something went wrong!"
                
def login(screen, clock):
    intro = pg.image.load("SWP-Python\SteinScherePapierEchseSpock\pics_gifs\intro.jpg").convert()
    intro = pg.transform.scale(intro, (screen.get_width(), screen.get_height()))
    input_rect = pg.Rect(screen.get_width()/8*5, screen.get_height()/16, screen.get_width()/4, screen.get_height()/16)
    user_input = ""
    difficulty_input = None
    color_active = pg.Color("lightgrey")
    color_passive = pg.Color("grey")
    color = color_passive
    active = False
    input = True
    screen.fill((0,0,0))
    while True:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
            if input:            
                if event.type == pg.MOUSEBUTTONDOWN:
                    if input_rect.collidepoint(event.pos):
                        active = True
                    else:
                        active = False
            else:
                if event.type == pg.MOUSEBUTTONDOWN:
                    if input_rect.collidepoint(event.pos):
                        active = True
                    else:
                        active = False
        
            if active:
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        if input:
                            active = False
                            input = False
                        else:
                            return user_input, difficulty_input
                    if event.key == pg.K_BACKSPACE:
                        user_input = user_input[:-1]
                    else:
                        user_input += event.unicode
                    
        if active:
            color = color_active
        else:
            color = color_passive
            
        screen.blit(intro, intro.get_rect())
        screen.blit(pg.font.Font(None, 72).render("Enter Username", True, (179,230,255)), (input_rect.x, input_rect.y-50))
        pg.draw.rect(screen, color, input_rect)
        screen.blit(pg.font.Font(None, 72).render(user_input, True, (179,230,255)), (input_rect.x+5, input_rect.y+5))
        input_rect.w = max(100, input_rect.width)
        pg.display.update()
        clock.tick(60)  

def difficulty(p, diff):
    match diff:
        case 0:
            return random.randint(1,5)
        case 1:
            e = em.getEvents()
            print(list(e[p.getID()].values())[3:])
            print(list(e[p.getID()].values())[3:].index(max(list(e[p.getID()].values())[3:])))
            chosen = initItem(list(e[p.getID()].values())[3:].index(max(list(e[p.getID()].values())[3:]))+1)
            counters = list(chosen.getStats().values())
            indices = [i for i, x in enumerate(counters) if x == -1]
            return indices[random.randint(0,1)]+1

def game(screen, clock, p, d):
    intro = pg.image.load("SWP-Python\SteinScherePapierEchseSpock\pics_gifs\intro.jpg").convert()
    intro = pg.transform.scale(intro, (screen.get_width(), screen.get_height()))
    stone_btn = pg.Rect(screen.get_width()/21*13, screen.get_height()/21*16, screen.get_width()/8, screen.get_height()/5)
    scissor_btn = pg.Rect(screen.get_width()/20*9, screen.get_height()/24, screen.get_width()/6, screen.get_height()/5)
    paper_btn = pg.Rect(screen.get_width()/27*20, screen.get_height()/3, screen.get_width()/7, screen.get_height()/4)
    lizard_btn = pg.Rect(screen.get_width()/3, screen.get_height()/17*13, screen.get_width()/9, screen.get_height()/5)
    spock_btn = pg.Rect(screen.get_width()/5, screen.get_height()/3, screen.get_width()/7, screen.get_height()/4)
    stats_btn = pg.Rect(screen.get_width()/8*6, screen.get_height()/16, screen.get_width()/12, screen.get_height()/16)
    screen.fill((0,0,0))
    while True:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        em.patternFile(False)
                        pg.quit()
                        sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if stone_btn.collidepoint(event.pos):
                    return 1
                elif scissor_btn.collidepoint(event.pos):
                    return 2
                elif paper_btn.collidepoint(event.pos):
                    return 3
                elif lizard_btn.collidepoint(event.pos):
                    return 4
                elif spock_btn.collidepoint(event.pos):
                    return 5
                elif stats_btn.collidepoint(event.pos):
                    return stats(screen, clock, p, d)
        pg.draw.rect(screen, pg.color.Color(100,0,0), stone_btn)
        pg.draw.rect(screen, pg.color.Color(100,0,0), scissor_btn)
        pg.draw.rect(screen, pg.color.Color(100,0,0), paper_btn)
        pg.draw.rect(screen, pg.color.Color(100,0,0), lizard_btn)
        pg.draw.rect(screen, pg.color.Color(100,0,0), spock_btn)
        screen.blit(intro, intro.get_rect())
        pg.draw.rect(screen, pg.color.Color(194, 130, 133), stats_btn)
        screen.blit(pg.font.Font(None, 72).render("Stats", True, (179,230,255)), (stats_btn.x+10, stats_btn.y+5))
        pg.display.update()
        clock.tick(60)
 
def gradientbars(bars,ydata,cmap):
    ax = bars[0].axes
    lim = ax.get_xlim()+ax.get_ylim()
    ax.axis(lim)
    for bar in bars:
        bar.set_facecolor("none")
        x,y = bar.get_xy()
        w, h = bar.get_width(), bar.get_height()
        grad = np.atleast_2d(np.linspace(0,1*h/max(ydata),256)).T
        ax.imshow(grad, extent=[x,x+w,y,y+h], origin='lower', aspect="auto", 
                  norm=cm.colors.NoNorm(vmin=0,vmax=1), cmap=plt.get_cmap(cmap)) 
            
def stats(screen, clock, p, d):
    e = em.getEvents()
    pStats = e[p.getID()]
    names = list(pStats.keys())
    values = list(pStats.values())
    fig1, ax1 = plt.subplots()
    gradientbars(ax1.bar(names[:3], values[:3]), values[:3], "cool_r")
    plt.savefig("SWP-Python\SteinScherePapierEchseSpock\pics_gifs/outcomes.png")
    fig2, ax2 = plt.subplots()
    gradientbars(ax2.bar(names[3:8], values[3:8]), values[3:8], "cool_r")
    plt.savefig("SWP-Python\SteinScherePapierEchseSpock\pics_gifs/items.png")
    game_btn = pg.Rect(screen.get_width()/8*6, screen.get_height()/16, screen.get_width()/12, screen.get_height()/16)
    screen.fill((255,255,255))
    while True:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        em.patternFile(False)
                        pg.quit()
                        sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if game_btn.collidepoint(event.pos):
                    return game(screen, clock, p, d)
        pg.draw.rect(screen, pg.color.Color(194, 130, 133), game_btn)
        screen.blit(pg.font.Font(None, 72).render("Game", True, (179,230,255)), (game_btn.x+10, game_btn.y+5))
        outcomes = pg.image.load("SWP-Python\SteinScherePapierEchseSpock\pics_gifs/outcomes.png")
        items = pg.image.load("SWP-Python\SteinScherePapierEchseSpock\pics_gifs/items.png")
        screen.blit(pg.transform.scale(outcomes, (screen.get_width()/9*4, screen.get_height()/7*4)), (screen.get_width()/27*1, screen.get_height()/14*3))
        screen.blit(pg.transform.scale(items, (screen.get_width()/9*4, screen.get_height()/7*4)), (screen.get_width()/27*13, screen.get_height()/14*3))
        pg.display.update()
        clock.tick(60)

def gameResult(screen, clock, pItem, cItem, out, p, d):
    intro = pg.image.load("SWP-Python\SteinScherePapierEchseSpock\pics_gifs\intro.jpg").convert()
    intro = pg.transform.scale(intro, (screen.get_width(), screen.get_height()))
    restart_btn = pg.Rect(screen.get_width()/5*4, screen.get_height()/5*4, screen.get_width()/8, screen.get_height()/16)
    exit_btn = pg.Rect(screen.get_width()/5*4, screen.get_height()/11*10, screen.get_width()/8, screen.get_height()/16)
    stone_btn = pg.Rect(screen.get_width()/21*13, screen.get_height()/21*16, screen.get_width()/8, screen.get_height()/5)
    scissor_btn = pg.Rect(screen.get_width()/20*9, screen.get_height()/24, screen.get_width()/6, screen.get_height()/5)
    paper_btn = pg.Rect(screen.get_width()/27*20, screen.get_height()/3, screen.get_width()/7, screen.get_height()/4)
    lizard_btn = pg.Rect(screen.get_width()/3, screen.get_height()/17*13, screen.get_width()/9, screen.get_height()/5)
    spock_btn = pg.Rect(screen.get_width()/5, screen.get_height()/3, screen.get_width()/7, screen.get_height()/4)
    btns = {"stone": stone_btn, "scissor": scissor_btn, "paper": paper_btn, "lizard": lizard_btn, "spock": spock_btn}
    btnP = btns[pItem]
    btnC = btns[cItem]
        
    screen.fill((0,0,0))
    while True:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        em.patternFile(False)
                        pg.quit()
                        sys.exit()
                    elif event.key == pg.K_r:
                        return runGame(p, d)
            if event.type == pg.MOUSEBUTTONDOWN:
                if exit_btn.collidepoint(event.pos):
                    em.patternFile(False)
                    pg.quit()
                    sys.exit()                
                elif restart_btn.collidepoint(event.pos):
                    return runGame(p, d)
        screen.blit(intro, intro.get_rect())
        pg.draw.rect(screen, pg.color.Color(100,0,100), exit_btn)
        screen.blit(pg.font.Font(None, 72).render("Exit", True, (179,230,255)), (exit_btn.x+65, exit_btn.y+10))
        pg.draw.rect(screen, pg.color.Color(100,0,100), restart_btn)
        screen.blit(pg.font.Font(None, 72).render("Restart", True, (179,230,255)), (restart_btn.x+30, restart_btn.y+10))
        pg.draw.rect(screen, pg.color.Color(100,200,100), btnP, 3)
        pg.draw.rect(screen, pg.color.Color(100,200,100), btnC, 3)
        screen.blit(pg.font.Font(None, 72).render(out, True, (210,130,255)), (screen.get_width()/8*6, screen.get_height()/16))
        pg.display.update()
        clock.tick(60)

def startGame():
    def start():
        runGame(player.get_value(), difficulty.get_value()[1])
    
    em.patternFile(True)
    pg.init()
    size = get_monitors()[0].width, get_monitors()[0].height
    screen = pg.display.set_mode(size)
    size = get_monitors()[0].width, get_monitors()[0].height
    menu = pygame_menu.Menu('Welcome', size[0]/2, size[1]/2,
                       theme=pygame_menu.themes.THEME_BLUE)
    player = menu.add.text_input('Name: ')
    difficulty = menu.add.selector('Difficulty: ', [('Easy', 1), ('Medium', 2), ("Hard", 3)])
    menu.add.button('Play', start)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(screen)

def runGame(p, d):
    clock = pg.time.Clock()
    size = get_monitors()[0].width, get_monitors()[0].height
    screen = pg.display.set_mode(size)
    player = p
    if player is None or isinstance(player, str):
        player = initPlayer(p)
    diff = d
    chosenItem = initItem(game(screen, clock, player, diff), "", player)
    c = computer.Computer(diff)
    print(c.calcMove(player))
    computerItem = initItem(c.calcMove(player))
    print(chosenItem.itemName() + " vs " + computerItem.itemName())
    outcome = (checkMatch(chosenItem.checkStats(computerItem.itemName()), player))
    print(outcome)
    gameResult(screen, clock, chosenItem.itemName(), computerItem.itemName(), outcome.split("m")[1], player, diff)

if __name__ == "__main__":
    startGame()