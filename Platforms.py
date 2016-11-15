# -*- coding: utf-8 -*-
"""
Created on Sun Nov 08 16:04:10 2015

@author: tpwur
"""
import pygame

class TileM(pygame.sprite.Sprite):
    def __init__(self, x, y, period):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.Surface((64, 64))
        
        if period == "present":
            self.image = pygame.image.load("Images/topTileM.png").convert()
        elif period == "past":
            self.image = pygame.image.load("Images/pastBlock.jpg").convert()
        elif period == "future":
            self.image = pygame.image.load("Images/TileMFuture.png").convert()
        
        self.rect = pygame.Rect(x, y, 64, 64)


    def update(self):
        pass


class End(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((64,64))
        self.image.convert()
        self.image.fill(pygame.Color("black"))
        self.rect = pygame.Rect(x,y,64,64)
        

class Block(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((64,64))
        self.image.convert()
        self.rect = pygame.Rect(x,y,64,64)
  
      
class Key(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((64,64))
        self.image.convert()
        #self.image.fill(pygame.Color("yellow"))
        self.image = pygame.image.load("Images//key.png").convert() 
        self.image = pygame.transform.scale(self.image,(64,64))                
        self.rect = pygame.Rect(x,y,64,64)
        
        
class Door(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((64,64))
        self.image.convert()
        self.image.fill(pygame.Color("brown"))
        self.rect = pygame.Rect(x,y,64,64)            
        