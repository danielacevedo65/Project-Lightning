import pygame
from Player import Player
from Enemy import Enemy, Rage_Enemy, Fearful_Enemy, First_Boss, Second_Boss, Third_Boss
from Platforms import TileM,End,Block,Door,Key
import random
from random import randint


WIN_WIDTH = 800
WIN_HEIGHT = 640
HALF_WIDTH = int(WIN_WIDTH / 2)
HALF_HEIGHT = int(WIN_HEIGHT / 2)

DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
DEPTH = 32
FLAGS = 0
CAMERA_SLACK = 30

PLAYER_X = 64
PLAYER_Y = 704
HAS_KEY = False


def mainMenu():
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)    
    screen.fill((0,0,0))
    
    image = Background('Images/titleMenu2.jpg',[0,0])
    image.image = pygame.transform.scale(image.image,(800,640))
                  
    screen.blit(image.image,image.rect)
    
    returnVal = 100
    running = True
    while running:
        pos = (0,0)
        for e in pygame.event.get():
            if e.type == pygame.QUIT: raise SystemExit
            elif e.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
        #start
        if (pos[0] <= 225 and pos[0] >= 30) and (pos[1] <= 565 and pos[1] >= 500):
            running = False
        #settings
        elif (pos[0] <= 495 and pos[0] >= 305) and (pos[1] <= 565 and pos[1] >= 500):
            running = False
            returnVal = 11
        #quit
        elif (pos[0] <= 765 and pos[0] >= 575) and (pos[1] <= 565 and pos[1] >= 500):
            gameover()
            return 0
            
        pygame.display.update()
    
    return returnVal


def about():
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)    
    screen.fill((0,0,0))
    
    image = Background('Images/howToPlay.jpg',[0,0])
    image.image = pygame.transform.scale(image.image,(800,640))
                  
    screen.blit(image.image,image.rect)
    
    returnVal = 10
    running = True
    while running:
        pos = (0,0)
        for e in pygame.event.get():
            if e.type == pygame.QUIT: raise SystemExit
            elif e.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
        #main menu
        if (pos[0] <= 520 and pos[0] >= 280) and (pos[1] <= 590 and pos[1] >= 530):
            running = False
            
        pygame.display.update()
    
    return returnVal


def endScreen():
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)    
    screen.fill((0,0,0))
    
    image = Background('Images/lose.jpg',[0,0])
    image.image = pygame.transform.scale(image.image,(800,640))
                  
    screen.blit(image.image,image.rect)
    
    returnVal = 10
    running = True
    while running:
        pos = (0,0)
        for e in pygame.event.get():
            if e.type == pygame.QUIT: raise SystemExit
            elif e.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
        #main menu
        if (pos[0] <= 520 and pos[0] >= 280) and (pos[1] <= 590 and pos[1] >= 530):
            running = False
            
        pygame.display.update()
    
    return returnVal


def winScreen():
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)    
    screen.fill((0,0,0))
    
    image = Background('Images/win.jpg',[0,0])
    image.image = pygame.transform.scale(image.image,(800,640))
                  
    screen.blit(image.image,image.rect)
    
    returnVal = 10
    running = True
    while running:
        pos = (0,0)
        for e in pygame.event.get():
            if e.type == pygame.QUIT: raise SystemExit
            elif e.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
        #main menu
        if (pos[0] <= 520 and pos[0] >= 280) and (pos[1] <= 590 and pos[1] >= 530):
            running = False
            
        pygame.display.update()
    
    return returnVal



def levelOnePresent():
    global PLAYER_X,PLAYER_Y,HAS_KEY
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
    pygame.display.set_caption("Project Lightning")
    

    up = down = left = right = attack = running = False

    
    background = Background('Images/present.jpg', [0,0])  
    background.image = pygame.transform.scale(background.image,(800,640))
    
    entities = pygame.sprite.Group()
    player = Player(PLAYER_X, PLAYER_Y)
    num_enemies = randint(10, 50)
    enemies = []
    for i in range(18):
        enemies.append(Enemy(randint(200, 10000), 704))
    for i in range(7):
        enemies.append(Rage_Enemy(randint(200, 10000), 704))
        enemies.append(Fearful_Enemy(randint(200, 10000), 704))
    enemies.append(First_Boss(11650, 704)) #BOSS    
    platforms = []
    end = End(0,0)

    x = y = 0
    level = [
        #"PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "W                                                                                                                                                                                 PPPPPPPPPPPPPPPPPPPPP",
        "W                                                                                                                                                                                                      P",
        "W                                                                                                                                                                                                      P",
        "W                                                                                                        PPPPPPPPPPP                                                                         PPPPPPPPPPP",
        "W                  PPPPPPPPPPPP                                            PPPPPPP                                                                                                 P",
        "W                                                                    PPPPP                                                         PPPPPPPPPP                                       P",
        "W      PPPPPPPPP                             PPPPPPPP                                                                                                                              P",
        "W                                                                P                                                                                                             PPPPPPPPPPPPP",
        "W                PPPPPPPPPPPPP                           PPPPPPPPP                                                                                         PPPPPPPPPP          D            P",
        "W                                                                                             PPPPPPPPP                                                                        D            P",
        "W                                 PP               PPPP                                                      P        P                  PPPPPPPPPPPPP                         D            P",
        "W                                 PPP                           PPPPP                    PPPPPP             PP        PP                                                       D       E    P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP        PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]
    # build the level
    for row in level:
        for col in row:
            if col == "P":
                p = TileM(x, y, "present")
                platforms.append(p)
                entities.add(p)
            elif col == "E":
                end = End(x,y)
                entities.add(end)
            elif col == "W":
                block = Block(x,y)
                platforms.append(block)
            elif col == "D" and not HAS_KEY:
                door = Door(x,y)
                entities.add(door)
                platforms.append(door)
                
            x += 64
        y += 64
        x = 0

    total_level_width  = len(level[0])*64
    total_level_height = len(level)*64
    camera = Camera(total_level_width, total_level_height)
    entities.add(player)
    for enemy in enemies:
        entities.add(enemy)

    while 1:
        for e in pygame.event.get():
            if e.type == pygame.QUIT: raise SystemExit
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                raise SystemExit
            if e.type == pygame.KEYDOWN and e.key == pygame.K_UP:
                up = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_DOWN:
                down = True
                PLAYER_X = player.rect.x
                PLAYER_Y = player.rect.y
                
                if random.randrange(0,2) == 1:
                    return 101
                else:
                    return 102
                
            if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
                left = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
                right = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                attack = True

            if e.type == pygame.KEYUP and e.key == pygame.K_UP:
                up = False
            if e.type == pygame.KEYUP and e.key == pygame.K_DOWN:
                down = False
            if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
                right = False
            if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
                left = False
            if e.type == pygame.KEYUP and e.key == pygame.K_SPACE:
                attack = False

        # draw background
        screen.fill([255, 255, 255])
        screen.blit(background.image, background.rect)

        camera.update(player)

        if (player.rect.left >= end.x - 20 and player.rect.left <= end.x + 20) and player.rect.top == end.y:
            PLAYER_X = 64
            PLAYER_Y = 704
            HAS_KEY = False
            return 200
        elif player.yval == 100 or player.health < 0:
            PLAYER_X = 64
            PLAYER_Y = 704
            HAS_KEY = False
            return 12
        else:
            # update player, draw everything else
            player.update(up, down, left, right, attack, platforms,enemies)
            for enemy in enemies:
                enemy.update(up, down, left, right, running, platforms, player)            
            for e in entities:
                screen.blit(e.image, camera.apply(e))
        
        pygame.display.update()
    
    return 0
    
    
def levelOnePast():
    global PLAYER_X,PLAYER_Y,HAS_KEY
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
    pygame.display.set_caption("Project Lightning")
    

    up = down = left = right = attack = running = False

    
    background = Background('Images/past.jpg', [0,0])  
    background.image = pygame.transform.scale(background.image,(800,640))
    
    entities = pygame.sprite.Group()
    player = Player(PLAYER_X,PLAYER_Y)
    num_enemies = randint(10, 50)
    enemies = []
    for i in range(18):
        enemies.append(Enemy(randint(200, 10000), 704))
    for i in range(7):
        enemies.append(Rage_Enemy(randint(200, 10000), 704))
        enemies.append(Fearful_Enemy(randint(200, 10000), 704))
    platforms = []
    end = End(0,0)

    x = y = 0
    level = [
        #"PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "W                                                                                                                                                                             PPPPPPPPPPPP",
        "W                                                                                                                                                                                        P",
        "W                                                                                                                                                                                        P",
        "W                                                                                                                                                                       PPPPPPPPPPP",
        "W                  PPPPPPPPPPPP                                                                                                                                                        P",
        "W                                                                                                                                   PPPPPPPPPP                                       P",
        "W      PPPPPPPPP                             PPPPPPPP                PPPPPPPPPPPP                                                                                                        P",
        "W                                                                P                                                                                                                   PPPPPP",
        "W                PPPPPPPPPPPPP                           PPPPPPPPP                                                                                                           PPPPPPPPPP   P",
        "W                                                                                             PPPPPPPPP        PPPPPP                                                        P            P",
        "W                                 PP               PPPP                                                      PP      PP                  PPPPPPPPPPPPP                       P            P",
        "W                                 PPP                           PPPPP                    PPPPPPP            PP        PP                                                     P            P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP        PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]
    # build the level
    for row in level:
        for col in row:
            if col == "P":
                p = TileM(x, y, "past")
                platforms.append(p)
                entities.add(p)
            elif col == "E":
                end = End(x,y)
                entities.add(end)
            elif col == "W":
                block = Block(x,y)
                platforms.append(block)
                
            x += 64
        y += 64
        x = 0

    total_level_width  = len(level[0])*64
    total_level_height = len(level)*64
    camera = Camera(total_level_width, total_level_height)
    entities.add(player)
    for enemy in enemies:
        entities.add(enemy)

    while 1:
        for e in pygame.event.get():
            if e.type == pygame.QUIT: raise SystemExit
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                raise SystemExit
            if e.type == pygame.KEYDOWN and e.key == pygame.K_UP:
                up = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_DOWN:
                down = True
                PLAYER_X = player.rect.x
                PLAYER_Y = player.rect.y
                
                if random.randrange(0,2) == 1:
                    return 100
                else:
                    return 102
            if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
                left = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
                right = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                attack = True

            if e.type == pygame.KEYUP and e.key == pygame.K_UP:
                up = False
            if e.type == pygame.KEYUP and e.key == pygame.K_DOWN:
                down = False
            if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
                right = False
            if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
                left = False
            if e.type == pygame.KEYUP and e.key == pygame.K_SPACE:
                attack = False

        # draw background
        screen.fill([255, 255, 255])
        screen.blit(background.image, background.rect)

        camera.update(player)

        if player.yval == 100 or player.health < 0:
            return 12

        # update player, draw everything else
        player.update(up, down, left, right, attack, platforms,enemies)
        for enemy in enemies:
            enemy.update(up, down, left, right, running, platforms, player)            
        for e in entities:
            screen.blit(e.image, camera.apply(e))
        
        pygame.display.update()
    
    return 0


def levelOneFuture():
    global PLAYER_X,PLAYER_Y,HAS_KEY
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
    pygame.display.set_caption("Project Lightning")
    

    up = down = left = right = attack = running = False

    
    background = Background('Images/future.jpg', [0,0])  
    background.image = pygame.transform.scale(background.image,(800,640))
    
    entities = pygame.sprite.Group()
    player = Player(PLAYER_X,PLAYER_Y)
    num_enemies = randint(10, 50)
    enemies = []
    for i in range(18):
        enemies.append(Enemy(randint(200, 10000), 704,"future"))
    for i in range(7):
        enemies.append(Rage_Enemy(randint(200, 10000), 704,"future"))
        enemies.append(Fearful_Enemy(randint(200, 10000), 704,"future"))
    platforms = []
    end = End(0,0)
    key = Key(0,0)

    x = y = 0
    level = [
        #"PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "W                                                                                                                                                                               PPPPPPP",
        "W                                                                                                                                                                                     P",
        "W                                                                                                                                                                                     P",
        "W                                                                                                                                                                   PPPPPPPPPP       P",
        "W                  PPPPPPPPPPPP                                                                                                                                                      P",
        "W                                                                                   PPPPPPPPPP                                                         PPPPPPPPPP                    P",
        "W      PPPPPPPPP                             PPPPPPPP                PPPPPPPPPPPP                                                                                                     P",
        "W                                                                P                                                                                                            PPPPPPPPPP",
        "W                PPPPPPPPPPPPP                           PPPPPPPPP                                                                                                           PPPPPPPPPPP",
        "W                                                                                             PPPPPPPPP                                                                                 P",
        "W                                 PP               PPPP                                                    P        P                  PPPPPPPPPPPPP                                     P",
        "W                                 PPP                           PPPPP                    PPPPPPPPP        PP        PP                                                                K   P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP        PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]
    # build the level
    for row in level:
        for col in row:
            if col == "P":
                p = TileM(x, y, "future")
                platforms.append(p)
                entities.add(p)
            elif col == "E":
                end = End(x,y)
                entities.add(end)
            elif col == "W":
                block = Block(x,y)
                platforms.append(block)
            elif col == "K":
                key = Key(x,y)
                entities.add(key)
                
            x += 64
        y += 64
        x = 0

    total_level_width  = len(level[0])*64
    total_level_height = len(level)*64
    camera = Camera(total_level_width, total_level_height)
    entities.add(player)
    for enemy in enemies:
        entities.add(enemy)

    while 1:
        for e in pygame.event.get():
            if e.type == pygame.QUIT: raise SystemExit
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                raise SystemExit
            if e.type == pygame.KEYDOWN and e.key == pygame.K_UP:
                up = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_DOWN:
                down = True
                PLAYER_X = player.rect.x
                PLAYER_Y = player.rect.y
                
                if random.randrange(0,2) == 1:
                    return 100
                else:
                    return 101
            if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
                left = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
                right = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                attack = True

            if e.type == pygame.KEYUP and e.key == pygame.K_UP:
                up = False
            if e.type == pygame.KEYUP and e.key == pygame.K_DOWN:
                down = False
            if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
                right = False
            if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
                left = False
            if e.type == pygame.KEYUP and e.key == pygame.K_SPACE:
                attack = False

        # draw background
        screen.fill([255, 255, 255])
        screen.blit(background.image, background.rect)

        camera.update(player)
        
        if (player.rect.left >= key.x - 20 and player.rect.left <= key.x + 20) and player.rect.top == key.y:
            HAS_KEY = True
            entities.remove(key)
        
        if player.yval == 100 or player.health < 0:
            return 12        
        
        # update player, draw everything else
        player.update(up, down, left, right, attack, platforms,enemies)
        for enemy in enemies:
            enemy.update(up, down, left, right, running, platforms, player)            
        for e in entities:
            screen.blit(e.image, camera.apply(e))
        
        pygame.display.update()
    
    return 0    


def levelTwoPresent():
    global PLAYER_X,PLAYER_Y,HAS_KEY    
    
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
    pygame.display.set_caption("Project Lightning")
    

    up = down = left = right = attack = running = False

    
    background = Background('Images/present.jpg', [0,0])  
    background.image = pygame.transform.scale(background.image,(800,640))
    
    entities = pygame.sprite.Group()
    player = Player(PLAYER_X,PLAYER_Y)
    num_enemies = randint(10, 50)
    enemies = []
    for i in range(15):
        enemies.append(Enemy(randint(200, 7500), 704,"present"))
    for i in range(3):
        enemies.append(Rage_Enemy(randint(200, 7500), 704,"present"))
        enemies.append(Fearful_Enemy(randint(200, 7500), 704,"present"))
        
    enemies.append(Second_Boss(8500, 500))
    platforms = []
    end = End(0,0)

    x = y = 0
    level = [
        #"PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "W                                                                                                                                                   PPPPPP",
        "W                         DD                                                                                                                             P",
        "W                         DD                                                                                                                             P",
        "W                         DD                                                                               PPPPPPPPPPP                         PPPPPPPPPPP",
        "W                         DD                                                         PPPPPPP                                                   D          P",
        "W                         DD                                                          PPPPPPPPPP                                               D          P",
        "W                         DD                          PPPPPPPPPPPP                                                                             D         EP",
        "W                      PPPPPPPPP                                          P                                                             PPP PPPPPPPP PPPPPP",
        "W                     PPPPPPPPPPP                PPPPPPPPP                                                            PPPPPPPPPPPPPPPPPPP                P",
        "W                    PPPPPPPPPPPPPPPPPP                                                           PPPPPPPPP                                              P",
        "W                   PPPPPPPPPPPPPPPPPPPPPP               PPPP                                                  PPPPP                                     P",
        "W                  PPPPPPPPPPPPPPPPPPPPPPPP                                                 PP        PP                                                 P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP  PPP  PPP  PPP  PPP  PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]
    # build the level
    for row in level:
        for col in row:
            if col == "P":
                p = TileM(x, y, "present")
                platforms.append(p)
                entities.add(p)
            elif col == "E":
                end = End(x,y)
                entities.add(end)
            elif col == "W":
                block = Block(x,y)
                platforms.append(block)
            elif col == "D" and not HAS_KEY:
                door = Door(x,y)
                entities.add(door)
                platforms.append(door)
                
            x += 64
        y += 64
        x = 0

    total_level_width  = len(level[0])*64
    total_level_height = len(level)*64
    camera = Camera(total_level_width, total_level_height)
    entities.add(player)
    for enemy in enemies:
        entities.add(enemy)

    while 1:
        for e in pygame.event.get():
            if e.type == pygame.QUIT: raise SystemExit
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                raise SystemExit
            if e.type == pygame.KEYDOWN and e.key == pygame.K_UP:
                up = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_DOWN:
                down = True
                PLAYER_X = player.rect.x
                PLAYER_Y = player.rect.y
                
                if random.randrange(0,2) == 1:
                    return 201
                else:
                    return 202
            if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
                left = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
                right = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                attack = True

            if e.type == pygame.KEYUP and e.key == pygame.K_UP:
                up = False
            if e.type == pygame.KEYUP and e.key == pygame.K_DOWN:
                down = False
            if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
                right = False
            if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
                left = False
            if e.type == pygame.KEYUP and e.key == pygame.K_SPACE:
                attack = False

        # draw background
        screen.fill([255, 255, 255])
        screen.blit(background.image, background.rect)

        camera.update(player)

        if player.rect.left == end.x and player.rect.top == end.y:
            PLAYER_X = 64
            PLAYER_Y = 704
            HAS_KEY = False
            return 300
        elif player.yval == 100 or player.health < 0:
            return 12
        else:
            # update player, draw everything else
            player.update(up, down, left, right, attack, platforms,enemies)
            for enemy in enemies:
                enemy.update(up, down, left, right, running, platforms, player)            
            for e in entities:
                screen.blit(e.image, camera.apply(e))
        
        pygame.display.update()
    
    return 0


def levelTwoPast():
    global PLAYER_X,PLAYER_Y,HAS_KEY    
    
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
    pygame.display.set_caption("Project Lightning")
    

    up = down = left = right = attack = running = False

    
    background = Background('Images/past.jpg', [0,0])  
    background.image = pygame.transform.scale(background.image,(800,640))
    
    entities = pygame.sprite.Group()
    player = Player(PLAYER_X, PLAYER_Y)
    enemies = []
    for i in range(15):
        enemies.append(Enemy(randint(200, 10000), 704))
    for i in range(3):
        enemies.append(Rage_Enemy(randint(200, 10000), 704))
        enemies.append(Fearful_Enemy(randint(200, 10000), 704))
    platforms = []
    end = End(0,0)

    x = y = 0
    level = [
        #"PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "W                                                                                                                                                   PPPPPP",
        "W                                                                                                                                                      P",
        "W                                                                                                                                                      P",
        "W                                                                                                        PPPPPPPPPPP                         PPPPPPPPPPP",
        "W                                                                                  PPPPPPP                                                   D          P",
        "W                                                                                  PPPPPPPPPP                                                D          P",
        "W                                                   PPPPPPPPPPPP                                                                             D         P",
        "W                      PPPPPPPPP                                          P                                                             PPP PPPPPPPP PPPPPP",
        "W                     PPPPPPPPPPP                PPPPPPPPP                                                            PPPPPPPPPPPPPPPPPPP                P",
        "W                    PPPPPPPPPPPPPPPPPP                                                           PPPPPPPPP                                              P",
        "W                   PPPPPPPPPPPPPPPPPPPPPP               PPPP                                                  PPPPP                                     P",
        "W                  PPPPPPPPPPPPPPPPPPPPPPPP                                                 PP        PP                                                 P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP  PPP  PPP  PPP  PPP  PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]
    # build the level
    for row in level:
        for col in row:
            if col == "P":
                p = TileM(x, y, "past")
                platforms.append(p)
                entities.add(p)
            elif col == "E":
                end = End(x,y)
                entities.add(end)
            elif col == "W":
                block = Block(x,y)
                platforms.append(block)
            elif col == "D" and not HAS_KEY:
                door = Door(x,y)
                entities.add(door)
                platforms.append(door)
                
            x += 64
        y += 64
        x = 0

    total_level_width  = len(level[0])*64
    total_level_height = len(level)*64
    camera = Camera(total_level_width, total_level_height)
    entities.add(player)
    for enemy in enemies:
        entities.add(enemy)

    while 1:
        for e in pygame.event.get():
            if e.type == pygame.QUIT: raise SystemExit
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                raise SystemExit
            if e.type == pygame.KEYDOWN and e.key == pygame.K_UP:
                up = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_DOWN:
                down = True
                PLAYER_X = player.rect.x
                PLAYER_Y = player.rect.y
                
                if random.randrange(0,2) == 1:
                    return 200
                else:
                    return 202
            if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
                left = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
                right = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                attack = True

            if e.type == pygame.KEYUP and e.key == pygame.K_UP:
                up = False
            if e.type == pygame.KEYUP and e.key == pygame.K_DOWN:
                down = False
            if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
                right = False
            if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
                left = False
            if e.type == pygame.KEYUP and e.key == pygame.K_SPACE:
                attack = False

        # draw background
        screen.fill([255, 255, 255])
        screen.blit(background.image, background.rect)

        camera.update(player)

        if player.rect.left == end.x and player.rect.top == end.y:
            return 12
        elif player.yval == 100 or player.health < 0:
            return 12
        else:
            # update player, draw everything else
            player.update(up, down, left, right, attack, platforms,enemies)
            for enemy in enemies:
                enemy.update(up, down, left, right, running, platforms, player)            
            for e in entities:
                screen.blit(e.image, camera.apply(e))
        
        pygame.display.update()
    
    return 0
    
    
def levelTwoFuture():
    global PLAYER_X,PLAYER_Y,HAS_KEY    
    
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
    pygame.display.set_caption("Project Lightning")
    

    up = down = left = right = attack = running = False

    
    background = Background('Images/future.jpg', [0,0])  
    background.image = pygame.transform.scale(background.image,(800,640))
    
    entities = pygame.sprite.Group()
    player = Player(PLAYER_X, PLAYER_Y)
    enemies = []
    for i in range(15):
        enemies.append(Enemy(randint(200, 10000), 704,"future"))
    for i in range(3):
        enemies.append(Rage_Enemy(randint(200, 10000), 704,"future"))
        enemies.append(Fearful_Enemy(randint(200, 10000), 704,"future"))
    platforms = []
    end = End(0,0)
    key = Key(0,0)

    x = y = 0
    level = [
        #"PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "W                                                                                                                                                   PPPPPP",
        "W                         DD                                                                                                                             P",
        "W                         DD                                                                                                                             P",
        "W                         DD                                                                               PPPPPPPPPPP                         PPPPPPPPPPP",
        "W                         DD                                                         PPPPPPP                                                             P",
        "W                         DD                                                          PPPPPPPPPP                                                         P",
        "W                         DD                          PPPPPPPPPPPP                                                                              K        P",
        "W                      PPPPPPPPP                                          P                                                             PPP PPPPPPPP PPPPPP",
        "W                     PPPPPPPPPPP                PPPPPPPPP                                                            PPPPPPPPPPPPPPPPPPP                P",
        "W                    PPPPPPPPPPPPPPPPPP                                                           PPPPPPPPP                                              P",
        "W                   PPPPPPPPPPPPPPPPPPPPPP               PPPP                                                  PPPPP                                     P",
        "W                  PPPPPPPPPPPPPPPPPPPPPPPP                                                 PP        PP                                                 P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP  PPP  PPP  PPP  PPP  PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]
    # build the level
    for row in level:
        for col in row:
            if col == "P":
                p = TileM(x, y, "future")
                platforms.append(p)
                entities.add(p)
            elif col == "E":
                end = End(x,y)
                entities.add(end)
            elif col == "W":
                block = Block(x,y)
                platforms.append(block)
            elif col == "D" and not HAS_KEY:
                door = Door(x,y)
                entities.add(door)
                platforms.append(door)
            elif col == "K":
                key = Key(x,y)
                entities.add(key)
                
            x += 64
        y += 64
        x = 0

    total_level_width  = len(level[0])*64
    total_level_height = len(level)*64
    camera = Camera(total_level_width, total_level_height)
    entities.add(player)
    for enemy in enemies:
        entities.add(enemy)

    while 1:
        for e in pygame.event.get():
            if e.type == pygame.QUIT: raise SystemExit
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                raise SystemExit
            if e.type == pygame.KEYDOWN and e.key == pygame.K_UP:
                up = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_DOWN:
                down = True
                PLAYER_X = player.rect.x
                PLAYER_Y = player.rect.y
                
                if random.randrange(0,2) == 1:
                    return 200
                else:
                    return 201
            if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
                left = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
                right = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                attack = True

            if e.type == pygame.KEYUP and e.key == pygame.K_UP:
                up = False
            if e.type == pygame.KEYUP and e.key == pygame.K_DOWN:
                down = False
            if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
                right = False
            if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
                left = False
            if e.type == pygame.KEYUP and e.key == pygame.K_SPACE:
                attack = False

        # draw background
        screen.fill([255, 255, 255])
        screen.blit(background.image, background.rect)

        camera.update(player)
        
        if (player.rect.left >= key.x - 20 and player.rect.left <= key.x + 20) and player.rect.top == key.y:
            HAS_KEY = True
            entities.remove(key)

        if player.rect.left == end.x and player.rect.top == end.y:
            return 12
        elif player.yval == 100 or player.health < 0:
            return 12
        else:
            # update player, draw everything else
            player.update(up, down, left, right, attack, platforms,enemies)
            for enemy in enemies:
                enemy.update(up, down, left, right, running, platforms, player)            
            for e in entities:
                screen.blit(e.image, camera.apply(e))
        
        pygame.display.update()
    
    return 0


def levelThreePresent():
    global PLAYER_X,PLAYER_Y,HAS_KEY
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
    pygame.display.set_caption("Project Lightning")
    

    up = down = left = right = attack = running = False

    
    background = Background('Images/present.jpg', [0,0])  
    background.image = pygame.transform.scale(background.image,(800,640))
    
    entities = pygame.sprite.Group()
    player = Player(PLAYER_X, PLAYER_Y)
    num_enemies = randint(10, 50)
    enemies = []
    for i in range(15):
        enemies.append(Enemy(randint(200, 10000), 704))
    for i in range(4):
        enemies.append(Rage_Enemy(randint(200, 10000), 704))
        enemies.append(Fearful_Enemy(randint(200, 10000), 704))
        
    enemies.append(Third_Boss(1000, 500)) #BOSS    
    platforms = []
    end = End(0,0)

    x = y = 0
    level = [
        "W                                                                                                             W",    
        "W                                                                                                             W",
        "W                                                                                                             W",
        "W              D                                                                                              W",
        "W              D                                                                   PPPPPPPPPPPPPPPPP          W",
        "W         E    D                                                             PPPPP                            W",
        "W      PPPPPPPPP                                                     PPPPPP        PPPPP                      W",
        "W                P                                                P                                           W",
        "W                PPPPPPPPPPPP                                  P                                              W",
        "W                        PPPPPP                          PPPPPPPPP            PPPPPP                          W",
        "W                                 PP               PPPP                 PPPP                                  W",
        "W                                 PPP                           PPPPP                    PPPPPP               W",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]
    # build the level
    for row in level:
        for col in row:
            if col == "P":
                p = TileM(x, y, "present")
                platforms.append(p)
                entities.add(p)
            elif col == "E":
                end = End(x,y)
                entities.add(end)
            elif col == "W":
                block = Block(x,y)
                platforms.append(block)
            elif col == "D" and not HAS_KEY:
                door = Door(x,y)
                entities.add(door)
                platforms.append(door)
                
            x += 64
        y += 64
        x = 0

    total_level_width  = len(level[0])*64
    total_level_height = len(level)*64
    camera = Camera(total_level_width, total_level_height)
    entities.add(player)
    for enemy in enemies:
        entities.add(enemy)

    while 1:
        for e in pygame.event.get():
            if e.type == pygame.QUIT: raise SystemExit
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                raise SystemExit
            if e.type == pygame.KEYDOWN and e.key == pygame.K_UP:
                up = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_DOWN:
                down = True
                PLAYER_X = player.rect.x
                PLAYER_Y = player.rect.y
                
                if random.randrange(0,2) == 1:
                    return 301
                else:
                    return 302
                
            if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
                left = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
                right = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                attack = True

            if e.type == pygame.KEYUP and e.key == pygame.K_UP:
                up = False
            if e.type == pygame.KEYUP and e.key == pygame.K_DOWN:
                down = False
            if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
                right = False
            if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
                left = False
            if e.type == pygame.KEYUP and e.key == pygame.K_SPACE:
                attack = False

        # draw background
        screen.fill([255, 255, 255])
        screen.blit(background.image, background.rect)

        camera.update(player)

        if (player.rect.left >= end.x - 20 and player.rect.left <= end.x + 20) and player.rect.top == end.y:
            PLAYER_X = 64
            PLAYER_Y = 704
            HAS_KEY = False
            return 13
        elif player.yval == 100 or player.health < 0:
            return 12
        else:
            # update player, draw everything else
            player.update(up, down, left, right, attack, platforms,enemies)
            for enemy in enemies:
                enemy.update(up, down, left, right, running, platforms, player)            
            for e in entities:
                screen.blit(e.image, camera.apply(e))
        
        pygame.display.update()
    
    return 0
    
    
def levelThreePast():
    global PLAYER_X,PLAYER_Y,HAS_KEY
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
    pygame.display.set_caption("Project Lightning")
    

    up = down = left = right = attack = running = False

    
    background = Background('Images/past.jpg', [0,0])  
    background.image = pygame.transform.scale(background.image,(800,640))
    
    entities = pygame.sprite.Group()
    player = Player(PLAYER_X,PLAYER_Y)
    num_enemies = randint(10, 50)
    enemies = []
    for i in range(15):
        enemies.append(Enemy(randint(200, 10000), 704))
    for i in range(4):
        enemies.append(Rage_Enemy(randint(200, 10000), 704))
        enemies.append(Fearful_Enemy(randint(200, 10000), 704))
    platforms = []
    end = End(0,0)
    key = Key(0,0)

    x = y = 0
    level = [
        "W                                                                                                             W",    
        "W                                                                                                             W",
        "W                                                                                                           K W",
        "W              D                                                                                           PPPW",
        "W              D                                                                         PPPPPPPPPPPPPPPPP    W",
        "W              D                                                                                              W",
        "W      PPPPPPPPP                                                     PPPPPP        PPPPPPPPP                      W",
        "W                P                                                P                           P                 W",
        "W                PPPPPPPPPPPP                                  P                      PPPPPPPP                W",
        "W                        PPPPPP                          PPPPPPPPP            PPPPPPP                          W",
        "W                                 PP               PPPP                 PPPPPP                                  W",
        "W                                 PPP                           PPPPP                    PPPPPP               W",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]    # build the level
    for row in level:
        for col in row:
            if col == "P":
                p = TileM(x, y, "past")
                platforms.append(p)
                entities.add(p)
            elif col == "E":
                end = End(x,y)
                entities.add(end)
            elif col == "W":
                block = Block(x,y)
                platforms.append(block)
            elif col == "K":
                key = Key(x,y)
                entities.add(key)
                
            x += 64
        y += 64
        x = 0

    total_level_width  = len(level[0])*64
    total_level_height = len(level)*64
    camera = Camera(total_level_width, total_level_height)
    entities.add(player)
    for enemy in enemies:
        entities.add(enemy)

    while 1:
        for e in pygame.event.get():
            if e.type == pygame.QUIT: raise SystemExit
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                raise SystemExit
            if e.type == pygame.KEYDOWN and e.key == pygame.K_UP:
                up = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_DOWN:
                down = True
                PLAYER_X = player.rect.x
                PLAYER_Y = player.rect.y
                
                if random.randrange(0,2) == 1:
                    return 300
                else:
                    return 302
            if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
                left = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
                right = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                attack = True

            if e.type == pygame.KEYUP and e.key == pygame.K_UP:
                up = False
            if e.type == pygame.KEYUP and e.key == pygame.K_DOWN:
                down = False
            if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
                right = False
            if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
                left = False
            if e.type == pygame.KEYUP and e.key == pygame.K_SPACE:
                attack = False

        # draw background
        screen.fill([255, 255, 255])
        screen.blit(background.image, background.rect)

        camera.update(player)

        if (player.rect.left >= key.x - 20 and player.rect.left <= key.x + 20) and player.rect.top == key.y:
            HAS_KEY = True
            entities.remove(key)

        if player.yval == 100 or player.health < 0:
            return 12

        # update player, draw everything else
        player.update(up, down, left, right, attack, platforms,enemies)
        for enemy in enemies:
            enemy.update(up, down, left, right, running, platforms, player)            
        for e in entities:
            screen.blit(e.image, camera.apply(e))
        
        pygame.display.update()
    
    return 0


def levelThreeFuture():
    global PLAYER_X,PLAYER_Y,HAS_KEY
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
    pygame.display.set_caption("Project Lightning")
    

    up = down = left = right = attack = running = False

    
    background = Background('Images/future.jpg', [0,0])  
    background.image = pygame.transform.scale(background.image,(800,640))
    
    entities = pygame.sprite.Group()
    player = Player(PLAYER_X,PLAYER_Y)
    num_enemies = randint(10, 50)
    enemies = []
    for i in range(15):
        enemies.append(Enemy(randint(200, 10000), 704,"future"))
    for i in range(4):
        enemies.append(Rage_Enemy(randint(200, 10000), 704,"future"))
        enemies.append(Fearful_Enemy(randint(200, 10000), 704,"future"))
    platforms = []
    end = End(0,0)
    

    x = y = 0
    level = [
        "W                                                                                                             W",    
        "W                                                                                                             W",
        "W                                                                                                             W",
        "W              D                                                                                              W",
        "W              D                                                                                              W",
        "W              D                                                                                              W",
        "W      PPPPPPPPP                                                                                              W",
        "W                P                                                                                            W",
        "W                PPPPPPPPPPPP                                                                                 W",
        "W                        PPPPPP                          PPPPPPPPP            PPPPPP                          W",
        "W                                 PP               PPPP                 PPPP                                  W",
        "W                                 PPP                           PPPPP                    PPPPPP               W",
        "PPPPPPPPPPPPPPPPPPPPPPPPPP   PPPPPPPPPPP   PPPPPPPPPPPPPPPP   PPPPPPP   PPPPPP   PPPPPPPPP   PPPPPPP   PPPPPPPP",]    # build the level
    for row in level:
        for col in row:
            if col == "P":
                p = TileM(x, y, "future")
                platforms.append(p)
                entities.add(p)
            elif col == "E":
                end = End(x,y)
                entities.add(end)
            elif col == "W":
                block = Block(x,y)
                platforms.append(block)
            elif col == "K":
                key = Key(x,y)
                entities.add(key)
                
            x += 64
        y += 64
        x = 0

    total_level_width  = len(level[0])*64
    total_level_height = len(level)*64
    camera = Camera(total_level_width, total_level_height)
    entities.add(player)
    for enemy in enemies:
        entities.add(enemy)

    while 1:
        for e in pygame.event.get():
            if e.type == pygame.QUIT: raise SystemExit
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                raise SystemExit
            if e.type == pygame.KEYDOWN and e.key == pygame.K_UP:
                up = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_DOWN:
                down = True
                PLAYER_X = player.rect.x
                PLAYER_Y = player.rect.y
                
                if random.randrange(0,2) == 1:
                    return 300
                else:
                    return 301
            if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
                left = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
                right = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                attack = True

            if e.type == pygame.KEYUP and e.key == pygame.K_UP:
                up = False
            if e.type == pygame.KEYUP and e.key == pygame.K_DOWN:
                down = False
            if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
                right = False
            if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
                left = False
            if e.type == pygame.KEYUP and e.key == pygame.K_SPACE:
                attack = False

        # draw background
        screen.fill([255, 255, 255])
        screen.blit(background.image, background.rect)

        camera.update(player)
        
        if player.yval == 100 or player.health < 0:
            return 12        
        
        # update player, draw everything else
        player.update(up, down, left, right, attack, platforms,enemies)
        for enemy in enemies:
            enemy.update(up, down, left, right, running, platforms, player)            
        for e in entities:
            screen.blit(e.image, camera.apply(e))
        
        pygame.display.update()
    
    return 0    


def main():
    global cameraX, cameraY
    pygame.init()
    
    screenCounter = 0
    
    screenCounter = mainMenu() 
    
    while screenCounter >= 0:
        if screenCounter == 10:
            screenCounter = mainMenu()
        elif screenCounter == 11:
            screenCounter = about()
        elif screenCounter == 12:
            screenCounter = endScreen()
        elif screenCounter == 13:
            screenCounter = winScreen()
        elif screenCounter == 100:
            screenCounter = levelOnePresent()
        elif screenCounter == 101:
            screenCounter = levelOnePast()
        elif screenCounter == 102:
            screenCounter = levelOneFuture()
        elif screenCounter == 200:
            screenCounter = levelTwoPresent()
        elif screenCounter == 201:
            screenCounter = levelTwoPast()
        elif screenCounter == 202:
            screenCounter = levelTwoFuture()
        elif screenCounter == 300:
            screenCounter = levelThreePresent()
        elif screenCounter == 301:
            screenCounter = levelThreePast()
        elif screenCounter == 302:
            screenCounter = levelThreeFuture()
    

def gameover():
    pygame.quit()

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file).convert()
        #self.image = pygame.transform.scale(self.image,(800,640))                
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


class Camera(object):
    def __init__(self, width, height):
        self.state = pygame.Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.complex_camera(self.state, target.rect)

    def complex_camera(self, camera, target_rect):
        l, t, _, _ = target_rect
        _, _, w, h = camera
        l, t = -l+HALF_WIDTH, -t+HALF_HEIGHT
    
        t = max(-(camera.height-WIN_HEIGHT), t) # stop scrolling at the bottom
    
        return pygame.Rect(l, t, w, h)

'''
class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
'''


if __name__ == "__main__":
    main()
