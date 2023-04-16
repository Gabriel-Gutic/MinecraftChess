import setari
import culori
import patrat
import piesa

import pygame


pygame.init()

setari.patrate = patrat.generare_tabla()
setari.tabla = piesa.generare_tabla()

coordonate_mouse = (0, 0)


def main():
    while setari.ruleaza:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.MOUSEMOTION:
                coordonate_mouse = event.dict['pos']
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for line in setari.tabla:
                    for piesa in line:
                        if piesa is not None:
                            piesa.verificare_click(coordonate_mouse)
                for mutare_posibila in setari.mutari_posibile:
                    mutare_posibila.verificare_click(coordonate_mouse)
            elif event.type == pygame.QUIT:
                setari.ruleaza = False
                
        setari.suprafata.fill(culori.ROSU)
        
        for line in setari.patrate:
            for patrat in line:
                patrat.deseneaza(setari.suprafata)
                
        for mutare_posibila in setari.mutari_posibile:
            mutare_posibila.deseneaza(setari.suprafata)
        
        for line in setari.tabla:
            for piesa in line:
                if piesa is not None:
                    piesa.deseneaza(setari.suprafata)
        
        pygame.display.update()


if __name__ == '__main__':
    main()
