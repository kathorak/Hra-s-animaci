import pygame

def get_image(sheet:pygame.surface.Surface, frame_x:int, frame_y:int, width:int, height:int, scale:float):
    """
    Funkce, která vezme spritesheet, souřadnice x a y požadovaného obrázku v něm,
    šířku a výšku tohoto obrázku, a škálovací faktor, a vrátí `Surface` s daným přeškálovaným obrázkem.
    """
    #? Vytvoření "plátna" o velikosti obrázku
    img = pygame.Surface((width, height)).convert_alpha()

    #? Překreslení dané části spritesheetu s obrázkem na "plátno"
    img.blit(sheet, (0, 0), ((frame_x * width), (frame_y * height), width, height))

    #? Přeškálování obrázku
    img = pygame.transform.scale(img, (width*scale, height*scale))

    #? Nastavení barvy v obrázku, která bude považovaná za průhlednou
    img.set_colorkey((0, 0, 0))
    return img