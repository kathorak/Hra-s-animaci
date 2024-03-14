from time import time

class Timer:
    """
    Třída, jejíž instance měří nastavený časový limit.
    """
    def __init__(self, limit:float): #Konstruktor - Volá se při vytváření proměnné typu Timer
        self.set_time(limit) #Nastavení časového limitu z parametru konstruktoru
        self.restart() #Nastavení začátku času měření na "teď"

    def time_over(self) -> bool:
        """
        Funkce vracející pravdivostní hodnotu o uplynutí časového limitu od posledního restartu.
        
        Časovač neresetuje! K tomu je potřeba zavolat .restart()
        """
        #? aktuální čas mínus čas v bodě v minulosti je čas od bodu v minulosti do teď.
        #? Výsledné číslo je větší než limit? = True/False
        return time() - self.start_time > self.limit 

    def restart(self):
        """Metoda restartující časovač k opětovnému použití."""
        self.start_time = time()

    def set_time(self, limit:float):
        """Metoda pro nastavení nového časového limitu."""
        self.limit = limit
    