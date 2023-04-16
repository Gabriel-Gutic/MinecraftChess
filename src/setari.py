import pygame


MARIME_PATRAT = 80
MARIME_PIESA = 64
MARIME_SPATIU = (MARIME_PATRAT - MARIME_PIESA) // 2

MARIME = (MARIME_PATRAT * 8, MARIME_PATRAT * 8)


suprafata = pygame.display.set_mode(MARIME)

patrate = []
mutari_posibile = []

tabla = []

ruleaza = True