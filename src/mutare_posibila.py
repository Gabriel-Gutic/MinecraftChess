import setari
import patrat


class MutarePosibila(patrat.Patrat):
    def __init__(self, pozitie, pozitie_piesa) -> None:
        super().__init__('MutarePosibila', pozitie)
        
        self._pozitie_piesa = pozitie_piesa
    
    def mutare_piesa(self):
        piesa = setari.tabla[self._pozitie_piesa[0]][self._pozitie_piesa[1]]
        if piesa is not None:
            piesa.pozitie = self._pozitie
            setari.tabla[self._pozitie_piesa[0]][self._pozitie_piesa[1]] = None
            setari.tabla[self._pozitie[0]][self._pozitie[1]] = piesa
        setari.mutari_posibile = []
    
    def verificare_click(self, coordonate_mouse):
        x = self._pozitie[0] * setari.MARIME_PATRAT
        y = self._pozitie[1] * setari.MARIME_PATRAT
        
        if x <= coordonate_mouse[0] <= x + setari.MARIME_PATRAT and y <= coordonate_mouse[1] <= y + setari.MARIME_PATRAT:
            self.mutare_piesa()
    
    
        
        