import setari
from mutare_posibila import MutarePosibila

import pygame


class Piesa:
    def __init__(self, echipa, tip, pozitie) -> None:
        self._pozitie = pozitie
        self._tip = tip
        self._echipa = echipa
        
        self._imagine = pygame.image.load('Imagini/Piese/' + echipa + '/' + tip + '.png')
        self._imagine = pygame.transform.scale(self._imagine, (setari.MARIME_PIESA, setari.MARIME_PIESA))
        
    def deseneaza(self, surface):
        surface.blit(self._imagine, (self._pozitie[0] * setari.MARIME_PATRAT + setari.MARIME_SPATIU, self._pozitie[1] * setari.MARIME_PATRAT + setari.MARIME_SPATIU))
    
    @property
    def pozitie(self):
        return self._pozitie
    
    @pozitie.setter
    def pozitie(self, pozitie_noua):
        self._pozitie = pozitie_noua
    
    def afiseaza_mutari(self):
        if self._tip == 'Pion':
            if self._echipa == 'Alb' and setari.tabla[self._pozitie[0]][self._pozitie[1] - 1] is None:
                setari.mutari_posibile.append(MutarePosibila((self._pozitie[0], self._pozitie[1] - 1), self._pozitie))
                if self._pozitie[1] == 6 and setari.tabla[self._pozitie[0]][self._pozitie[1] - 2] is None:
                    setari.mutari_posibile.append(MutarePosibila((self._pozitie[0], self._pozitie[1] - 2), self._pozitie))
    
    def verificare_click(self, coordonate_mouse):
        x = self._pozitie[0] * setari.MARIME_PATRAT + setari.MARIME_SPATIU
        y = self._pozitie[1] * setari.MARIME_PATRAT + setari.MARIME_SPATIU
        
        if x <= coordonate_mouse[0] <= x + setari.MARIME_PIESA and y <= coordonate_mouse[1] <= y + setari.MARIME_PIESA:
            setari.mutari_posibile = []
            self.afiseaza_mutari()
        
def generare_tabla():
    tabla = [[None for i in range(8)] for j in range(8)]
    
    # Echipa Alb
    for i in range(8):
        tabla[i][6] = Piesa('Alb', 'Pion', (i, 6))
    
    tabla[0][7] = Piesa("Alb", "Turn",   (0, 7))
    tabla[7][7] = Piesa("Alb", "Turn",   (7, 7))
    tabla[1][7] = Piesa("Alb", "Cal",    (1, 7))
    tabla[6][7] = Piesa("Alb", "Cal",    (6, 7))
    tabla[2][7] = Piesa("Alb", "Nebun",  (2, 7))
    tabla[5][7] = Piesa("Alb", "Nebun",  (5, 7))
    tabla[3][7] = Piesa("Alb", "Regina", (3, 7))
    tabla[4][7] = Piesa("Alb", "Rege",   (4, 7))
    
    # Echipa Negru
    for i in range(8):
        tabla[i][1] = Piesa('Negru', 'Pion', (i, 1))
    
    tabla[0][0] = Piesa("Negru", "Turn",   (0, 0))
    tabla[7][0] = Piesa("Negru", "Turn",   (7, 0))
    tabla[1][0] = Piesa("Negru", "Cal",    (1, 0))
    tabla[6][0] = Piesa("Negru", "Cal",    (6, 0))
    tabla[2][0] = Piesa("Negru", "Nebun",  (2, 0))
    tabla[5][0] = Piesa("Negru", "Nebun",  (5, 0))
    tabla[3][0] = Piesa("Negru", "Regina", (3, 0))
    tabla[4][0] = Piesa("Negru", "Rege",   (4, 0))
    
    return tabla