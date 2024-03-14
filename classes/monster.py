from typing import Any
import pygame
from utility import get_image
from settings import *
from classes.my_timer import Timer

class Monster(pygame.sprite.Sprite):
    """
    Třída reprezentující a popisující vlastnosti a chování příšery ve hře.

    Obecně funguje analogicky, jako hráč, jen ovládání je pevně dané.
    Tahle se pohybuje horizontálně a změní směr při srážce s okrajem okna.
    """

    #? Stálo by za to udělat obecnou příšeru a od ní dědit s rozdílnými vlastnostmi
    #?  abychom mohli mít různě rychlé, s různými sprity, s různými vzorci chování, najednou.
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.spritesheet = pygame.image.load("assets/monster.png").convert_alpha()
        self.image = get_image(self.spritesheet, 0, 9, 16, 8, 3)
        self.rect = self.image.get_rect(midbottom=(self.x, self.y))
        self.timer = Timer(0.1)
        self.frame_count = 2
        self.frame_index = 0
        self.direction = "Left" #Proměnná pro aktuální směr pohybu
        self.speed = 5

    def animation(self):
        if self.timer.time_over():
            self.frame_index += 1
            self.frame_index %= self.frame_count
            self.timer.restart()
        
        self.image = get_image(
            self.spritesheet, 
            self.frame_index,
            9, #Animace tady není závislá na směru pohybu
            16, 8, 3,
        )

    def update(self):
        self.animation()

        #? Kontrola pohybuu pryč z obrazovky
        #?  a řešení pomocí změny směru pohybu
        if self.rect.x <= 0:
            self.direction = "Right"
        elif self.rect.x >= screen_width - self.rect.width:
            self.direction = "Left"

        #? Krok v už určitě správném směru pohybu
        match self.direction: #Něco jako elif, ale nemusím psát podmínku opakovaně
            case "Left": #if self.direction == "Left"
                self.rect.x -= self.speed
            case "Right": #elif self.direction == "Right"
                self.rect.x += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)
