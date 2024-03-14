import pygame
from settings import *
from utility import get_image
from classes.my_timer import Timer

class Player(pygame.sprite.Sprite):
    """
    Třída reprezentující a popisující vlastnosti a chování hráče ve hře
    """
    def __init__(self, x, y):
        super().__init__() #Volání konstruktoru třídy pygame.sprite.Sprite

        #Souřadnice počáteční polohy hráče
        self.x = x
        self.y = y
        #! Použijí se jen na jednom místě!

        #"Arch" se všemi sprity hráče pro jeho animování
        self.spritesheet = pygame.image.load("assets/player.png").convert_alpha()
        #! Přístup do souboru je "pomalý" - raději si načíst všechny sprity do paměti (třeba list)

        #Nastavení výchozího spritu hráče
        self.image = get_image(self.spritesheet, 0, 0, 15, 16, 3)

        #Vytvoření rectu pro pohyb a detekci kolizí
        self.rect = self.image.get_rect(midbottom=(self.x, self.y))
        #! Jediné místo, kde se použije self.x a self.y!
        #-> Zbytečné instanční proměnné, šlo by použít argumenty konstruktoru x a y

        self.lives = 3 #Počet životů hráče
        self.speed = 3 #Rychlost hráče

        #Časovač pro pravidelnou změnu spritu v animaci
        #? Je nezávislý na snímkové frekvenci!
        self.timer = Timer(0.1)
        #TODO Možná bude stát za přejmenování (F2 přejmenuje všechny výskyty proměnné najednou)

        self.frame_count = 4 #Počet spritů/snímků pro animaci
        self.frame_index = 0 #Index aktuálního (počátečního) snímku

        #Proměnná pro stav nesmrtelnosti
        self.invul = False
        #TODO Raději použij další Timer

    def animation(self, direction):
        """Metoda měnící sprite hráče v průběhu animace"""
        if self.timer.time_over(): #Jen pokud doběhl limit časovače
            self.frame_index += 1 #Přidáme 1 k indexu pro snímky

            #? Nahradíme velký index za zbytek po dělení počtem snímků
            #?  (zbytek po dělení nikdy nepřekročí hodnotu dělitele)
            self.frame_index %= self.frame_count
            self.timer.restart() #Znovu spustíme časovač
        
        self.image = get_image( #Nahrajeme nový snímek jako sprite hráče
            self.spritesheet, 
            self.frame_index, #Udává sloupec ve spritesheetu
            direction, #Udává řádek ve spritesheetu
            15, 16, 3,
        )
        #TODO Může být v ifu pod timerem, protože pokud časovač nezvonil, není třeba měnit obrázek

    def update(self):
        """Metoda pro aktualizaci pozice hráče"""

        #? Vrátí "slovník" všech možných tlačítek s údaji o jejich stisknutí
        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT]: #Je stisknutá šipka vlevo?
            self.rect.x -= self.speed #Snížení horizontální souřadnice
            self.animation(2) #Vybrání odpovídající řádky ve spritesheetu (Otočení vlevo)
        elif key[pygame.K_RIGHT]: #Analogicky
            self.rect.x += self.speed
            self.animation(3)
        elif key[pygame.K_UP]:
            self.rect.y -= self.speed #Snížení vertikální souřadnice (To je tady pohyb k hornímu okraji obrazovky!)
            self.animation(1)
        elif key[pygame.K_DOWN]: #Analogicky
            self.rect.y += self.speed
            self.animation(0)
        
        #? Kontrola pohybuu pryč z obrazovky
        #?  a řešení pomocí teleportu na opačný okraj
        if self.rect.x < 0 - self.rect.width:
            self.rect.x = screen_width
        elif self.rect.x > screen_width:
            self.rect.x = -self.rect.width
        
        if self.rect.y < 0 - self.rect.height:
            self.rect.y = screen_height
        elif self.rect.y > screen_height:
            self.rect.y = -self.rect.height
  
    def draw(self, screen):
        """Metoda pro vykreslení hráče na danou obrazovku, v jeho aktuální pozici a stavem animace spritu."""
        screen.blit(self.image, self.rect)