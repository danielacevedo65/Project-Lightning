# -*- coding: utf-8 -*-
"""
Created on Sun Nov 08 15:47:52 2015

@author: tpwur
"""
import pygame

SQUARE_TOPLEFT_X = 64
SQUARE_BOTRIGHT_X = 64
SQUARE_BOTRIGHT_Y = 64


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.xval = 0
        self.yval = 0
        self.onGround = False
        '''
        self.image = pygame.Surface((64,64))
        self.image.fill(pygame.Color("#DDDDDD"))
        '''
        self.sheet = pygame.image.load("Images//tomSpritesheet.gif").convert_alpha()
        self.sheet.set_clip(pygame.Rect(0,0,64,64))        
        self.image = self.sheet.subsurface(self.sheet.get_clip())
                
        self.rect = pygame.Rect(x, y, 64, 64)
        self.health = 1500
        
        self.time = pygame.time.get_ticks()
        self.delay = 100
        
        self.move_time = pygame.time.get_ticks()
        self.move_delay = 400
        self.decide = 1

        self.isPlayerLeft = False

        
    def update(self, up, down, left, right, attack, platforms,enemies):
        if up:
            # only jump if on the ground
            if self.onGround:
                self.yval -= 10   
            self.sheet.set_clip(pygame.Rect(64*2,0,64,64))
            self.image = self.sheet.subsurface(self.sheet.get_clip())

        if down:
            self.sheet.set_clip(pygame.Rect(64*3,0,64,64))
            self.image = self.sheet.subsurface(self.sheet.get_clip())

        if attack:                   
            if pygame.time.get_ticks() > self.time + self.delay:
                pygame.mixer.init()
                pygame.mixer.music.load("Sounds/sword2.wav")
                pygame.mixer.music.play()                
                
                self.sheet.set_clip(pygame.Rect(64*7,0, 64, 64))
                self.image = self.sheet.subsurface(self.sheet.get_clip())
                enemiesHit = self.collideEnemies(self.xval,self.yval,enemies)
                for i in enemiesHit:
                    enemies[i].health -= 50
                    #print("Enemy's health is now: " + str(enemies[i].health))
                self.time = pygame.time.get_ticks()

        if (left or right):
            if pygame.time.get_ticks() > self.move_time + self.move_delay:
                if self.decide == 1 and not up:
                    self.sheet.set_clip(pygame.Rect(64*5,0,64,64))
                    self.image = self.sheet.subsurface(self.sheet.get_clip())
                    self.move_time = pygame.time.get_ticks()
                    self.decide = 2
                elif self.decide == 2 and not up:
                    self.sheet.set_clip(pygame.Rect(64*4,0,64,64))
                    self.image = self.sheet.subsurface(self.sheet.get_clip())
                    self.move_time = pygame.time.get_ticks()
                    self.decide = 1
            if left:
                self.isPlayerLeft = True
                self.xval = -3
                self.displayLeft()
            if right:
                self.isPlayerLeft = False
                self.xval = 3           

        if not self.onGround:
            # only accelerate with gravity if in the air
            self.yval += 0.3
            # max falling speed
            if self.yval > 100: self.health -= 5000

        if not(left or right or attack):
            self.xval = 0
            self.sheet.set_clip(pygame.Rect(0,0,64,64))
            self.image = self.sheet.subsurface(self.sheet.get_clip())
        
        self.displayLeft()

        # increment in x direction
        self.rect.left += self.xval
        # do x-axis collisions
        self.collide(self.xval, 0, platforms)
        # increment in y direction
        self.rect.top += self.yval
        # assuming we're in the air
        self.onGround = False;
        # do y-axis collisions
        self.collide(0, self.yval, platforms)


    def collide(self, xval, yval, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if xval > 0:
                    self.rect.right = p.rect.left
                    #print "collide right"
                if xval < 0:
                    self.rect.left = p.rect.right
                    #print "collide left"
                if yval > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yval = 0
                if yval < 0:
                    self.rect.top = p.rect.bottom


    def collideEnemies(self, xval, yval, enemies):
        damagedEnemies = []
        for i,e in enumerate(enemies):
            if pygame.sprite.collide_rect(self, e):
                damagedEnemies.append(i)
                #print("collide " + str(i))
        return damagedEnemies


    def displayLeft(self):
        if self.isPlayerLeft:
            self.image = self.sheet.subsurface(self.sheet.get_clip())
            self.image = pygame.transform.flip(self.image,True,False)           


