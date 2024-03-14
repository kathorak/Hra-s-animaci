import pygame
from settings import *
from classes.player import Player
from classes.monster import Monster


pygame.init()
clock = pygame.time.Clock() #Vytvoření hodinek
screen = pygame.display.set_mode((screen_width, screen_height)) #Vytvoření obrazovky
font = pygame.font.Font(None, 25) #Příprava fontu pro vypisování na obrazovku

game_over = False #Proměnná pro stav hry
elapsed_time = 0 #Proměnná pro uběhlý čas ve hře

player = Player(100, 300) #Proměnná hráče s počáteční polohou

#Proměnné příšer s počátečními polohami:
#TODO Bylo by fajn je dát do listu, když je jich víc
m1 = Monster(200, 400) 
m2 = Monster(300, 500)
m3 = Monster(100, 300)

while True: #Herní smyčka
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #? Při kliknutí na křížek se hra ukončí
            pygame.quit()
            exit()

    #Pokud jsme neprohráli...
    if game_over == False:
        screen.fill((255, 255, 255)) #Přebarvení všeho z minulého snímku
        text = font.render(f"Lives: {player.lives}", False, "#000000") #Počet životů připraveným fontem
        screen.blit(text, (700, 10)) #Vypsání počtu životů na obrazovku

        player.draw(screen) #Vykreslení hráče na obrazovku
        player.update() #Aktualizace pozice hráče
        #! Nemělo by to být v opačném pořadí?

        #Vykreslení příšer
        m1.draw(screen)
        m2.draw(screen)
        m3.draw(screen)

        #Aktualizace pozice příšer
        m1.update()
        m2.update()
        m3.update()
        #! Nemělo by to být v opačném pořadí?
        #TODO Kdyby byly příšery v listu, daly by se aktualizovat v cyklu

        #Pokud jsme přišli o všechny životy, nastavíme stav na prohraný
        if player.lives <= 0:
            game_over = True

    else:
        #TODO Tady bude kód pro prohranou hru
        pass

    pygame.display.update() #Aktualizace starého snímku za nově vykreslený
    clock.tick(60) #Frekvence obnovování

















