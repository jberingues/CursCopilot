# Joc d’aventures de texte amb el que anirem recorrent diferents habitacions 
# d’un castell. A cada habitació ens hi trobarem vàries portes, de la que en podrem
# escollir una i anar a una altra habitació. D’aquesta manera podrem recórrer el
# castell fins que trobem trobar un tresor.

pistes = [
    "Hi ha un retrat antic amb els ulls que semblen seguir-te.",
    "Hi ha un llibre obert amb una pàgina marcada que parla d'un ritual antic.",
    "Hi ha un eco suau que ressona des de la profunditat del corredor.",
    "Hi ha un aroma dolç i desconegut que flueix des de l'habitació següent.",
    "Hi ha un joc d'escacs a mig jugar, com si els jugadors haguessin desaparegut de sobte.",
    "Hi ha un mirall que no reflecteix la teva imatge.",
    "Hi ha un mapa antic penjat a la paret amb una zona marcada.",
    "Hi ha un diari amb l'última entrada escrita fa centenars d'anys.",
    "Hi ha un calaix mig obert amb una clau d'or dins.",
    "Hi ha un soroll estrany que sembla venir de darrere la paret."
]

sensacions = [
    "Ho veus, una llum tènue que es filtra a través d'una finestra trencada.",
    "Escoltes, el so distant d'una gota d'aigua que cau en una bassa.",
    "Sents, l'olor de la pols i el moho que omple l'aire.",
    "Tactes, la rugositat de la pedra freda de les parets.",
    "Intueixes, una presència estranya que et fa posar la pell de gallina.",
    "Ho veus, un quadre antic amb la pintura esquerdada i descolorida.",
    "Escoltes, el xiulet del vent que es cola per les esquerdes de la pedra.",
    "Sents, l'olor de la fusta vella i humida del mobiliari.",
    "Tactes, la suavitat del vellut d'un tron d'or desgastat.",
    "Intueixes, un secret amagat dins les ombres de l'habitació.",
    "Ho veus, un llibre obert amb pàgines grogues pel pas del temps.",
    "Escoltes, el creixement sord del foc en una llar de foc pròxima."
]

import random

class SelectorAleatoriElements:
    def __init__(self, elements):
        self.elements = elements
        self.elements_usats = []

    def afegir_elements(self, element):
        self.elements.append(element)

    def extreu_element_aleatori(self):
        if not self.elements:
            self.elements, self.elements_usats = self.elements_usats, []
        element_seleccionat = random.choice(self.elements)
        self.elements.remove(element_seleccionat)
        self.elements_usats.append(element_seleccionat)
        return element_seleccionat

    def reset(self):
        self.elements.extend(self.elements_usats)
        self.elements_usats = []

class GeneradorPistaSensacio:
    _instance = None

    def __new__(cls, pistes, sensacions):
        if cls._instance is None:
            cls._instance = super(GeneradorPistaSensacio, cls).__new__(cls)
            cls._instance.selector_pista = SelectorAleatoriElements(pistes)
            cls._instance.selector_sensacio = SelectorAleatoriElements(sensacions)
        return cls._instance

    def obtenir_pista_sensacio(self):
        pista = self.selector_pista.extreu_element_aleatori()
        sensacio = self.selector_sensacio.extreu_element_aleatori()
        return f"{pista} {sensacio}"
    
from enum import Enum

class SortidaTrobada(Enum):
    CONTINUA = 1
    FI = 2

from abc import ABC, abstractmethod

class Trobada(ABC):
    @abstractmethod
    def corre_trobada(self):
        pass

class TrobadaPerDefecte(Trobada):
    def __init__(self, pistes, sensacions):
        self.generador_pista_sensacio = GeneradorPistaSensacio(pistes, sensacions)

    def corre_trobada(self):
        pista_sensacio = self.generador_pista_sensacio.obtenir_pista_sensacio()
        print(pista_sensacio)
        return SortidaTrobada.CONTINUA
    
class Habitacio:
    def __init__(self, nom, trobada):
        self.nom = nom
        self.trobada = trobada

    def visita_habitacio(self):
        return self.trobada.corre_trobada()

habitacions = [
    Habitacio("Sala del Tron", TrobadaPerDefecte(pistes, sensacions)),
    Habitacio("Torre de la Guaita", TrobadaPerDefecte(pistes, sensacions)),
    Habitacio("Biblioteca Secreta", TrobadaPerDefecte(pistes, sensacions)),
    Habitacio("Cova del Drac", TrobadaPerDefecte(pistes, sensacions)),
    Habitacio("Laboratori Alquimista", TrobadaPerDefecte(pistes, sensacions)),
    Habitacio("Capella Espectral", TrobadaPerDefecte(pistes, sensacions))
]

import random

class Castell:
    def __init__(self, habitacions):
        self.selector_habitacio = SelectorAleatoriElements(habitacions)

    def selecciona_porta(self):
        num_portes = random.randint(2, 4)
        print(f"\nHi ha {num_portes} portes davant teu.")

        while True:
            eleccio = input(f"Selecciona una porta (1-{num_portes}): ")
            if eleccio.isdigit() and 1 <= int(eleccio) <= num_portes:
                return int(eleccio)
            else:
                print("Entrada invàlida. Si us plau, intenta-ho de nou.")

    def habitacio_seguent(self):
        self.selecciona_porta()
        habitacio = self.selector_habitacio.extreu_element_aleatori()
        print(f"\nHas entrat a la {habitacio.nom}.")
        return habitacio.visita_habitacio()

    def reset(self):
        self.selector_habitacio.reset()

class Joc:
    def __init__(self, habitacions):
        self.castell = Castell(habitacions)

    def jugar_joc(self):
        print("Benvingut al joc! L'objectiu és navegar pel castell i trobar el tresor.\n")

        while True:
            resultat = self.castell.habitacio_seguent()
            if resultat == SortidaTrobada.FI:
                self.castell.reset()
                print("\nGame over. Vols explorar un castell diferent? (s/n)")

                if input("> ").lower() != 's':
                    break

#Engega el programa
joc = Joc(habitacions)
joc.jugar_joc()
