import setari

import pygame


class Patrat:
    def __init__(self, echipa, pozitie) -> None:
        self._pozitie = pozitie
        self._echipa = echipa
        
        self._imagine = pygame.image.load('Imagini/Patrate/Design1/' + echipa + '.png')
        self._imagine = pygame.transform.scale(self._imagine, (setari.MARIME_PATRAT, setari.MARIME_PATRAT))
        
    
    def deseneaza(self, surface):
        surface.blit(self._imagine, (self._pozitie[0] * setari.MARIME_PATRAT, self._pozitie[1] * setari.MARIME_PATRAT))
        

def generare_tabla():
    tabla = []
    for j in range(8):
        tabla.append([])
        for i in range(8):
            if i % 2 == j % 2:
                tabla[j].append(Patrat("Alb", (i, j)))
            else:
                tabla[j].append(Patrat("Negru", (i, j)))
    return tabla