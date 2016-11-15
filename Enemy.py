# -*- coding: utf-8 -*-
"""
Created on Sun Nov 08 16:01:27 2015

@author: tpwur
"""

import pygame
import sys
import math
from random import randint
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, period="present"):
        pygame.sprite.Sprite.__init__(self)
        self.xval = 0
        self.yval = 0
        self.onGround = False
        self.onGroundx = True
        self.image = pygame.Surface((64,64))
        
        if period == "present":
            self.sheet = pygame.image.load("Images/grayNormalEnemy.gif").convert_alpha()
        elif period == "future":
            self.sheet = pygame.image.load("Images/grayNormalFuture.gif").convert_alpha()

        self.sheet.set_clip(pygame.Rect(0*0,0,64,64))        
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        
        self.rect = pygame.Rect(x, y, 64, 64)
        self.attack_power = randint(30,40)
        self.health = 500
        self.collision = False
        self.isAlive = True
        self.time = pygame.time.get_ticks()
        self.delay = 750
        
        self.move_time = pygame.time.get_ticks()
        self.move_delay = 500
        self.decide = 1
        self.isPlayerLeft = True

    def update(self, up, down, left, right, running, platforms, player):
        if self.health <= 0 or self.rect.bottom >= 900:
            self.isAlive = False
            pygame.mixer.init()
            pygame.mixer.music.load("Sounds//enemyDeath.wav")
            pygame.mixer.music.play()
        if self.isAlive:                  
            if self.yval == 100:
                sys.exit()
   
            try:
                if self.rect.colliderect(player.rect):
                    if pygame.time.get_ticks() > self.time + self.delay:
                        player.health -= self.attack()

                        self.sheet.set_clip(pygame.Rect(64*4,0,64,64))        
                        self.image = self.sheet.subsurface(self.sheet.get_clip())

                        if self.isPlayerLeft:
                            self.image = self.sheet.subsurface(self.sheet.get_clip())
                            self.image = pygame.transform.flip(self.image,True,False)
                        
                        #print("ATTACKING")
                        self.time = pygame.time.get_ticks()
                    
                else:

                    dx = player.rect.left - self.rect.left
                    dy = player.rect.top - self.rect.top
                    dist = math.hypot(dx, dy)
                    dx, dy = dx/dist, dy/dist
                    #how fast the enemy runs to the player
                    self.rect.x += dx * 2.5
                    
                    if (self.isMovingLeft(dx) or self.isMovingRight(dx)):
                        if pygame.time.get_ticks() > self.move_time + self.move_delay:
                            if self.decide == 1:
                                self.sheet.set_clip(pygame.Rect(64*2,0,64,64))
                                self.image = self.sheet.subsurface(self.sheet.get_clip())
                                self.move_time = pygame.time.get_ticks()
                                self.decide = 2
                            elif self.decide == 2:
                                self.sheet.set_clip(pygame.Rect(64*3,0,64,64))
                                self.image = self.sheet.subsurface(self.sheet.get_clip())
                                self.move_time = pygame.time.get_ticks()
                                self.decide = 1
                    if self.isMovingLeft(dx):
                        self.image = self.sheet.subsurface(self.sheet.get_clip())
                        self.image = pygame.transform.flip(self.image,True,False)

                    self.rect.bottom += 7
                    self.collide(0,self.rect.bottom, platforms, dy)
                    
                    ndy = self.collide(self.isMovingLeft(dx), 0, platforms, dy)
                    if ndy != 0:
                        self.rect.y += -.7
                    else:
                        self.rect.y -= -.7

            except ZeroDivisionError:
                pass
        else:
            self.rect.top = -1000
            self.rect.left = -1000

    def collide(self, xvel, yvel, platforms, dy):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if not xvel and yvel == 0:
                    self.rect.right = p.rect.left
                    self.onGroundx = False
                    return dy
                if xvel and yvel == 0:
                    self.rect.left = p.rect.right
                    self.onGroundx = False
                    return dy
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom
        self.onGroundx = True
        return 0

    def attack(self):
        return self.attack_power

    def isMovingLeft(self, x):
        if x < 0:
            self.isPlayerLeft = True
            return True
        return False

    def isMovingRight(self, x):
        if x > 0:
            self.isPlayerLeft = False
            return True
        return False


class Rage_Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, period="present"):
        pygame.sprite.Sprite.__init__(self)
        self.xval = 0
        self.yval = 0
        self.onGround = False
        self.onGroundx = True
        self.image = pygame.Surface((64,64))
        
        if period == "present":
            self.sheet = pygame.image.load("Images/redRageEnemy.gif").convert_alpha()
        elif period == "future":
            self.sheet = pygame.image.load("Images/redRageFuture.gif").convert_alpha()

        self.sheet.set_clip(pygame.Rect(0*0,0,64,64))        
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        
        self.rect = pygame.Rect(x, y, 64, 64)
        self.attack_power = randint(30,40)
        self.health = 500
        self.collision = False
        self.isAlive = True
        self.time = pygame.time.get_ticks()
        self.delay = 750
        
        self.move_time = pygame.time.get_ticks()
        self.move_delay = 400
        self.decide = 1
        self.isPlayerLeft = True
        self.powerup = False

    def update(self, up, down, left, right, running, platforms, player):
        if self.health <= 0 or self.rect.bottom >= 900:
            self.isAlive = False
            pygame.mixer.init()
            pygame.mixer.music.load("Sounds//enemyDeath.wav")
            pygame.mixer.music.play()
        if self.isAlive:                  
            if self.yval == 100:
                sys.exit()
   
            try:
                if self.health <= 150 and self.powerup == False:
                    self.attack_power += (self.attack_power * 1.2)
                    self.powerup = True
                    
                if self.rect.colliderect(player.rect):
                    if pygame.time.get_ticks() > self.time + self.delay:
                        player.health -= self.attack()

                        self.sheet.set_clip(pygame.Rect(64*4,0,64,64))        
                        self.image = self.sheet.subsurface(self.sheet.get_clip())

                        if self.isPlayerLeft:
                            self.image = self.sheet.subsurface(self.sheet.get_clip())
                            self.image = pygame.transform.flip(self.image,True,False)
                        
                        #print("ATTACKING")
                        self.time = pygame.time.get_ticks()
                    
                else:

                    dx = player.rect.left - self.rect.left
                    dy = player.rect.top - self.rect.top
                    dist = math.hypot(dx, dy)
                    dx, dy = dx/dist, dy/dist
                    #how fast the enemy runs to the player
                    self.rect.x += dx * 2.5
                    
                    if (self.isMovingLeft(dx) or self.isMovingRight(dx)):
                        if pygame.time.get_ticks() > self.move_time + self.move_delay:
                            if self.decide == 1:
                                self.sheet.set_clip(pygame.Rect(64*2,0,64,64))
                                self.image = self.sheet.subsurface(self.sheet.get_clip())
                                self.move_time = pygame.time.get_ticks()
                                self.decide = 2
                            elif self.decide == 2:
                                self.sheet.set_clip(pygame.Rect(64*3,0,64,64))
                                self.image = self.sheet.subsurface(self.sheet.get_clip())
                                self.move_time = pygame.time.get_ticks()
                                self.decide = 1
                    if self.isMovingLeft(dx):
                        self.image = self.sheet.subsurface(self.sheet.get_clip())
                        self.image = pygame.transform.flip(self.image,True,False)
                    
                    self.rect.bottom += 7
                    self.collide(0,self.rect.bottom, platforms, dy)
                    
                    ndy = self.collide(self.isMovingLeft(dx), 0, platforms, dy)
                    if ndy != 0:
                        self.rect.y += -.7
                    else:
                        self.rect.y -= -.7

            except ZeroDivisionError:
                pass
        else:
            self.rect.top = -1000
            self.rect.left = -1000
       

    def collide(self, xvel, yvel, platforms, dy):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if not xvel and yvel == 0:
                    self.rect.right = p.rect.left
                    self.onGroundx = False
                    return dy
                if xvel and yvel == 0:
                    self.rect.left = p.rect.right
                    self.onGroundx = False
                    return dy
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom
        self.onGroundx = True
        return 0

    def attack(self):
        return self.attack_power

    def isMovingLeft(self, x):
        if x < 0:
            self.isPlayerLeft = True
            return True
        return False

    def isMovingRight(self, x):
        if x > 0:
            self.isPlayerLeft = False
            return True
        return False


class Fearful_Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, period="present"):
        pygame.sprite.Sprite.__init__(self)
        self.xval = 0
        self.yval = 0
        self.onGround = False
        self.onGroundx = True
        self.image = pygame.Surface((64,64))
        
        if period == "present":
            self.sheet = pygame.image.load("Images/blueFearfulEnemy.gif").convert_alpha()
        elif period == "future":
            self.sheet = pygame.image.load("Images/blueFearfulFuture.gif").convert_alpha()

        self.sheet.set_clip(pygame.Rect(0*0,0,64,64))        
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        
        self.rect = pygame.Rect(x, y, 64, 64)
        self.attack_power = randint(30,40)
        self.health = 500
        self.collision = False
        self.isAlive = True
        self.time = pygame.time.get_ticks()
        self.delay = 750
        
        self.move_time = pygame.time.get_ticks()
        self.move_delay = 400
        self.decide = 1
        self.isPlayerLeft = True

    def update(self, up, down, left, right, running, platforms, player):
        if self.health <= 0 or self.rect.bottom >= 900:
            self.isAlive = False
            pygame.mixer.init()
            pygame.mixer.music.load("Sounds//enemyDeath.wav")
            pygame.mixer.music.play()
        if self.isAlive:                  
            if self.yval == 100:
                sys.exit()
   
            try:
                if self.health <= 150:
                    dx = player.rect.left - self.rect.left
                    dy = player.rect.top - self.rect.top
                    dist = math.hypot(dx, dy)
                    dx, dy = dx/dist, dy/dist
                    #how fast the enemy runs to the player
                    self.rect.x += (-dx) * 2.5

                    if (self.isMovingLeft(dx) or self.isMovingRight(dx)):
                        if pygame.time.get_ticks() > self.move_time + self.move_delay:
                            if self.decide == 1:
                                self.sheet.set_clip(pygame.Rect(64*2,0,64,64))
                                self.image = self.sheet.subsurface(self.sheet.get_clip())
                                self.move_time = pygame.time.get_ticks()
                                self.decide = 2
                            elif self.decide == 2:
                                self.sheet.set_clip(pygame.Rect(64*3,0,64,64))
                                self.image = self.sheet.subsurface(self.sheet.get_clip())
                                self.move_time = pygame.time.get_ticks()
                                self.decide = 1
                    if self.isMovingLeft(dx):
                        self.image = self.sheet.subsurface(self.sheet.get_clip())
                        self.image = pygame.transform.flip(self.image,True,False)
                    
                    self.rect.bottom += 7
                    self.collide(0,self.rect.bottom, platforms, dy)
                    
                    ndy = self.collide(self.isMovingLeft(dx), 0, platforms, dy)
                    if ndy != 0:
                        self.rect.y += -.7
                    else:
                        self.rect.y -= -.7

                elif self.rect.colliderect(player.rect):
                    if pygame.time.get_ticks() > self.time + self.delay:
                        player.health -= self.attack()

                        self.sheet.set_clip(pygame.Rect(64*4,0,64,64))        
                        self.image = self.sheet.subsurface(self.sheet.get_clip())

                        if self.isPlayerLeft:
                            self.image = self.sheet.subsurface(self.sheet.get_clip())
                            self.image = pygame.transform.flip(self.image,True,False)
                        
                        #print("ATTACKING")
                        self.time = pygame.time.get_ticks()
                        
            
                else:

                    dx = player.rect.left - self.rect.left
                    dy = player.rect.top - self.rect.top
                    dist = math.hypot(dx, dy)
                    dx, dy = dx/dist, dy/dist
                    #how fast the enemy runs to the player
                    self.rect.x += dx * 2.5
                    
                    if (self.isMovingLeft(dx) or self.isMovingRight(dx)):
                        if pygame.time.get_ticks() > self.move_time + self.move_delay:
                            if self.decide == 1:
                                self.sheet.set_clip(pygame.Rect(64*2,0,64,64))
                                self.image = self.sheet.subsurface(self.sheet.get_clip())
                                self.move_time = pygame.time.get_ticks()
                                self.decide = 2
                            elif self.decide == 2:
                                self.sheet.set_clip(pygame.Rect(64*3,0,64,64))
                                self.image = self.sheet.subsurface(self.sheet.get_clip())
                                self.move_time = pygame.time.get_ticks()
                                self.decide = 1
                    if self.isMovingLeft(dx):
                        self.image = self.sheet.subsurface(self.sheet.get_clip())
                        self.image = pygame.transform.flip(self.image,True,False)
                    
                    self.rect.bottom += 7
                    self.collide(0,self.rect.bottom, platforms, dy)
                    
                    ndy = self.collide(self.isMovingLeft(dx), 0, platforms, dy)
                    if ndy != 0:
                        self.rect.y += -.7
                    else:
                        self.rect.y -= -.7

            except ZeroDivisionError:
                pass
        else:
            self.rect.top = -1000
            self.rect.left = -1000

    def collide(self, xvel, yvel, platforms, dy):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if not xvel and yvel == 0:
                    self.rect.right = p.rect.left
                    self.onGroundx = False
                    return dy
                if xvel and yvel == 0:
                    self.rect.left = p.rect.right
                    self.onGroundx = False
                    return dy
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom
        self.onGroundx = True
        return 0

    def attack(self):
        return self.attack_power

    def isMovingLeft(self, x):
        if x < 0:
            self.isPlayerLeft = True
            return True
        return False

    def isMovingRight(self, x):
        if x > 0:
            self.isPlayerLeft = False
            return True
        return False


### STRONG BUT SLOW ###
class First_Boss(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.xval = 0
        self.yval = 0
        self.onGround = False
        self.image = pygame.Surface((64,64))
        
        self.sheet = pygame.image.load("Images//enemySpritesheet.gif").convert_alpha()
        self.sheet.set_clip(pygame.Rect(0*0,0,64,64))        
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        
        self.rect = pygame.Rect(x, y, 64, 64)
        self.attack_power = 350
        self.health = 1000
        self.collision = False
        self.isAlive = True
        self.time = pygame.time.get_ticks()
        self.delay = 2000
        
        self.move_time = pygame.time.get_ticks()
        self.move_delay = 400
        self.decide = 1
        self.isPlayerLeft = True

    def update(self, up, down, left, right, running, platforms, player):
        if self.health <= 0 or self.rect.bottom >= 900:
            self.isAlive = False
            pygame.mixer.init()
            pygame.mixer.music.load("Sounds//enemyDeath.wav")
            pygame.mixer.music.play()
        if self.isAlive:                  
            if self.yval == 100:
                sys.exit()
   
            try:
                if self.rect.colliderect(player.rect):
                    if pygame.time.get_ticks() > self.time + self.delay:
                        player.health -= self.attack()

                        self.sheet.set_clip(pygame.Rect(64*4,0,64,64))        
                        self.image = self.sheet.subsurface(self.sheet.get_clip())

                        if self.isPlayerLeft:
                            self.image = self.sheet.subsurface(self.sheet.get_clip())
                            self.image = pygame.transform.flip(self.image,True,False)
                        
                        #print("ATTACKING")
                        self.time = pygame.time.get_ticks()
                    
                else:
                    dx = player.rect.left - self.rect.left
                    dy = player.rect.top - self.rect.top
                    dist = math.hypot(dx, dy)
                    dx, dy = dx/dist, dy/dist
                    #how fast the enemy runs to the player
                    self.rect.x += dx * 2.5
                    
                    if (self.isMovingLeft(dx) or self.isMovingRight(dx)):
                        if pygame.time.get_ticks() > self.move_time + self.move_delay:
                            if self.decide == 1:
                                self.sheet.set_clip(pygame.Rect(64*2,0,64,64))
                                self.image = self.sheet.subsurface(self.sheet.get_clip())
                                self.move_time = pygame.time.get_ticks()
                                self.decide = 2
                            elif self.decide == 2:
                                self.sheet.set_clip(pygame.Rect(64*3,0,64,64))
                                self.image = self.sheet.subsurface(self.sheet.get_clip())
                                self.move_time = pygame.time.get_ticks()
                                self.decide = 1
                    if self.isMovingLeft(dx):
                        self.image = self.sheet.subsurface(self.sheet.get_clip())
                        self.image = pygame.transform.flip(self.image,True,False)
                    
                    ndy = self.collide(self.isMovingLeft(dx), 0, platforms, dy)
                    
                    self.rect.bottom += 7
                    self.collide(0,self.rect.bottom, platforms, dy)
                    
            except ZeroDivisionError:
                pass
        else:
            self.rect.top = -1000
            self.rect.left = -1000
       

    def collide(self, xvel, yvel, platforms, dy):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if not xvel and yvel == 0:
                    self.rect.right = p.rect.left
                    self.onGroundx = False
                    return dy
                if xvel and yvel == 0:
                    self.rect.left = p.rect.right
                    self.onGroundx = False
                    return dy
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom
        self.onGroundx = True
        return 0

    def attack(self):
        return self.attack_power

    def isMovingLeft(self, x):
        if x < 0:
            self.isPlayerLeft = True
            return True
        return False

    def isMovingRight(self, x):
        if x > 0:
            self.isPlayerLeft = False
            return True
        return False




### WEAKER BUT FASTER ###
class Second_Boss(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.xval = 0
        self.yval = 0
        self.onGround = False
        self.image = pygame.Surface((64,64))
        
        self.sheet = pygame.image.load("Images//purpleEliteEnemy.gif").convert_alpha()
        self.sheet.set_clip(pygame.Rect(0*0,0,64,64))        
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        
        self.rect = pygame.Rect(x, y, 64, 64)
        self.attack_power = 125
        self.health = 1000
        self.collision = False
        self.isAlive = True
        self.time = pygame.time.get_ticks()
        self.delay = 500
        
        self.move_time = pygame.time.get_ticks()
        self.move_delay = 400
        self.decide = 1
        self.isPlayerLeft = True

    def update(self, up, down, left, right, running, platforms, player):
        if self.health <= 0 or self.rect.bottom >= 900:
            self.isAlive = False
            pygame.mixer.init()
            pygame.mixer.music.load("Sounds//enemyDeath.wav")
            pygame.mixer.music.play()
        if self.isAlive:                  
            if self.yval == 100:
                sys.exit()
   
            try:
                if self.rect.colliderect(player.rect):
                    if pygame.time.get_ticks() > self.time + self.delay:
                        player.health -= self.attack()

                        self.sheet.set_clip(pygame.Rect(64*4,0,64,64))        
                        self.image = self.sheet.subsurface(self.sheet.get_clip())

                        if self.isPlayerLeft:
                            self.image = self.sheet.subsurface(self.sheet.get_clip())
                            self.image = pygame.transform.flip(self.image,True,False)
                        
                        #print("ATTACKING")
                        self.time = pygame.time.get_ticks()
                    
                else:
                    dx = player.rect.left - self.rect.left
                    dy = player.rect.top - self.rect.top
                    dist = math.hypot(dx, dy)
                    dx, dy = dx/dist, dy/dist
                    #how fast the enemy runs to the player
                    self.rect.x += dx * 2.5
                    
                    if (self.isMovingLeft(dx) or self.isMovingRight(dx)):
                        if pygame.time.get_ticks() > self.move_time + self.move_delay:
                            if self.decide == 1:
                                self.sheet.set_clip(pygame.Rect(64*2,0,64,64))
                                self.image = self.sheet.subsurface(self.sheet.get_clip())
                                self.move_time = pygame.time.get_ticks()
                                self.decide = 2
                            elif self.decide == 2:
                                self.sheet.set_clip(pygame.Rect(64*3,0,64,64))
                                self.image = self.sheet.subsurface(self.sheet.get_clip())
                                self.move_time = pygame.time.get_ticks()
                                self.decide = 1
                    if self.isMovingLeft(dx):
                        self.image = self.sheet.subsurface(self.sheet.get_clip())
                        self.image = pygame.transform.flip(self.image,True,False)
                    
                    self.rect.bottom += 7
                    self.collide(0,self.rect.bottom, platforms, dy)
                    
                    ndy = self.collide(self.isMovingLeft(dx), 0, platforms, dy)
                    if ndy != 0:
                        self.rect.y += -.7
                    else:
                        self.rect.y -= -.7
                        
            except ZeroDivisionError:
                pass
        else:
            self.rect.top = -1000
            self.rect.left = -1000
       

    def collide(self, xvel, yvel, platforms, dy):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if not xvel and yvel == 0:
                    self.rect.right = p.rect.left
                    self.onGroundx = False
                    return dy
                if xvel and yvel == 0:
                    self.rect.left = p.rect.right
                    self.onGroundx = False
                    return dy
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom
        self.onGroundx = True
        return 0

    def attack(self):
        return self.attack_power

    def isMovingLeft(self, x):
        if x < 0:
            self.isPlayerLeft = True
            return True
        return False

    def isMovingRight(self, x):
        if x > 0:
            self.isPlayerLeft = False
            return True
        return False





### FAST AND QUICK ###
class Third_Boss(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.xval = 0
        self.yval = 0
        self.onGround = False
        self.image = pygame.Surface((64,64))
        
        self.sheet = pygame.image.load("Images//pinkLeaderEnemy.gif").convert_alpha()
        self.sheet.set_clip(pygame.Rect(0*0,0,64,64))        
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        
        self.rect = pygame.Rect(x, y, 64, 64)
        self.attack_power = 400
        self.health = 1500
        self.collision = False
        self.isAlive = True
        self.time = pygame.time.get_ticks()
        self.delay = 550
        
        self.move_time = pygame.time.get_ticks()
        self.move_delay = 400
        self.decide = 1
        self.isPlayerLeft = True

    def update(self, up, down, left, right, running, platforms, player):
        if self.health <= 0 or self.rect.bottom >= 900:
            self.isAlive = False
            pygame.mixer.init()
            pygame.mixer.music.load("Sounds//enemyDeath.wav")
            pygame.mixer.music.play()
        if self.isAlive:                  
            if self.yval == 100:
                sys.exit()
   
            try:
                if self.rect.colliderect(player.rect):
                    if pygame.time.get_ticks() > self.time + self.delay:
                        player.health -= self.attack()

                        self.sheet.set_clip(pygame.Rect(64*4,0,64,64))        
                        self.image = self.sheet.subsurface(self.sheet.get_clip())

                        if self.isPlayerLeft:
                            self.image = self.sheet.subsurface(self.sheet.get_clip())
                            self.image = pygame.transform.flip(self.image,True,False)
                        
                        #print("ATTACKING")
                        self.time = pygame.time.get_ticks()
                    
                else:
                    dx = player.rect.left - self.rect.left
                    dy = player.rect.top - self.rect.top
                    dist = math.hypot(dx, dy)
                    dx, dy = dx/dist, dy/dist
                    #how fast the enemy runs to the player
                    self.rect.x += dx * 2.5
                    
                    if (self.isMovingLeft(dx) or self.isMovingRight(dx)):
                        if pygame.time.get_ticks() > self.move_time + self.move_delay:
                            if self.decide == 1:
                                self.sheet.set_clip(pygame.Rect(64*2,0,64,64))
                                self.image = self.sheet.subsurface(self.sheet.get_clip())
                                self.move_time = pygame.time.get_ticks()
                                self.decide = 2
                            elif self.decide == 2:
                                self.sheet.set_clip(pygame.Rect(64*3,0,64,64))
                                self.image = self.sheet.subsurface(self.sheet.get_clip())
                                self.move_time = pygame.time.get_ticks()
                                self.decide = 1
                    if self.isMovingLeft(dx):
                        self.image = self.sheet.subsurface(self.sheet.get_clip())
                        self.image = pygame.transform.flip(self.image,True,False)
                    
                    self.rect.bottom += 7
                    self.collide(0,self.rect.bottom, platforms, dy)
                    
                    ndy = self.collide(self.isMovingLeft(dx), 0, platforms, dy)
                    if ndy != 0:
                        self.rect.y += -.7
                    else:
                        self.rect.y -= -.7
                    
            except ZeroDivisionError:
                pass
        else:
            self.rect.top = -1000
            self.rect.left = -1000
       

    def collide(self, xvel, yvel, platforms, dy):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if not xvel and yvel == 0:
                    self.rect.right = p.rect.left
                    self.onGroundx = False
                    return dy
                if xvel and yvel == 0:
                    self.rect.left = p.rect.right
                    self.onGroundx = False
                    return dy
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom
        self.onGroundx = True
        return 0

    def attack(self):
        return self.attack_power

    def isMovingLeft(self, x):
        if x < 0:
            self.isPlayerLeft = True
            return True
        return False

    def isMovingRight(self, x):
        if x > 0:
            self.isPlayerLeft = False
            return True
        return False
