# Joc d’aventures de texte amb el que anirem recorrent diferents habitacions 
# d’un castell. A cada habitació ens hi trobarem vàries portes, de la que en podrem
# escollir una i anar a una altra habitació. D’aquesta manera podrem recórrer el
# castell fins que trobem trobar un tresor.
pistes = [
    "Hi ha un retrat antic amb els ulls que semblen seguir-te.",
    "Hi ha un llibre obert amb una pàgina marcada que parla d'un ritual antic.",
    "Hi ha un eco suau que ressona a través dels corredors buits.",
    "Hi ha un aroma estrany que flueix des de l'habitació següent.",
    "Hi ha un joc d'escacs a mig jugar, com si els jugadors haguessin desaparegut de sobte.",
    "Hi ha un calaix mig obert amb un mapa antic i desgastat.",
    "Hi ha un mirall trencat que reflecteix una imatge distorsionada de l'habitació.",
    "Hi ha un diari amb la darrera entrada escrita fa molts anys.",
    "Hi ha un armari tancat amb un soroll suau que prové de l'interior.",
    "Hi ha unes empremtes de pols que semblen indicar una ruta secreta."
]

sensacions = [
    "Ho veus: una cortina de vellut polsós que oneja lleugerament amb l'aire fred.",
    "Escoltes: el crepitar distant d'un foc que no pots veure.",
    "Olores: l'aroma penetrant de la cera de les espelmes que es fonen.",
    "Sents: la rugositat de la pedra freda sota els teus dits.",
    "Intueixes: una presència oculta, com si algú més estigués a l'habitació.",
    "Ho veus: un raig de llum que es filtra a través d'una escletxa en la paret.",
    "Escoltes: el xiulet del vent que es cola per les finestres tancades.",
    "Olores: el pols antic i l'humitat de les parets de pedra.",
    "Sents: el terra de pedra irregular sota els teus peus.",
    "Intueixes: un canvi subtil en l'aire, com si alguna cosa estigués a punt de passar.",
    "Ho veus: un reflex en un mirall trencat, massa ràpid per identificar.",
    "Escoltes: el so suau i inquietant d'una cançó que no pots identificar."
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
            return None
        if len(self.elements) == len(self.elements_usats):
            self.elements_usats = []
        element = random.choice(self.elements)
        while element in self.elements_usats:
            element = random.choice(self.elements)
        self.elements_usats.append(element)
        return element

    def reset(self):
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
    def corre_trobada(self) -> SortidaTrobada:
        pass

class TrobadaPerDefecte(Trobada):
    def __init__(self, pistes, sensacions):
        self.generador_pista_sensacio = GeneradorPistaSensacio(pistes, sensacions)

    def corre_trobada(self) -> SortidaTrobada:
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
    Habitacio("Torre de la Princesa", TrobadaPerDefecte(pistes, sensacions)),
    Habitacio("Cova del Drac", TrobadaPerDefecte(pistes, sensacions)),
    Habitacio("Biblioteca Encantada", TrobadaPerDefecte(pistes, sensacions)),
    Habitacio("Jardí Secret", TrobadaPerDefecte(pistes, sensacions)),
    Habitacio("Soterrani Obscur", TrobadaPerDefecte(pistes, sensacions))
]
import random

class Castell:
    def __init__(self, habitacions):
        self.selector_habitacio = SelectorAleatoriElements(habitacions)

    def selecciona_porta(self):
        num_portes = random.randint(2, 4)
        print(f"\nHi ha {num_portes} portes. Selecciona una porta (1-{num_portes}):")

        while True:
            porta_seleccionada = input("> ")
            if porta_seleccionada.isdigit() and 1 <= int(porta_seleccionada) <= num_portes:
                return int(porta_seleccionada)
            else:
                print(f"Entrada invàlida. Si us plau, selecciona una porta (1-{num_portes}):")

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
        print("\nBenvingut al Joc! L'objectiu és navegar pel castell i trobar el tresor.\n")

        while True:
            sortida = self.castell.habitacio_seguent()

            if sortida == SortidaTrobada.FI:
                self.castell.reset()
                print("\nGame over. Vols explorar un castell diferent? (s/n)")

                if input("> ").lower() != "s":
                    break

#Engega el programa
joc = Joc(habitacions)
joc.jugar_joc()


