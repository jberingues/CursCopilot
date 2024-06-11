# Desenvolupa un joc de Pedra, Paper i Tisores en Python basat en la consola
# El joc ha de ser modular, permetent actualitzacions fàcils o canvis de regles
# Implementa les regles del joc:
# - Pedra guanya a tisores
# - Tisores tallen paper
# - Paper cobreix pedra
# Inclou entrada d'usuari per seleccionar opcions i mostra els resultats del joc
# La interfície amb l'usuari ha de ser en català

import random

# Defineix opcions de joc
opcions_joc = {
    1: 'pedra',
    2: 'paper',
    3: 'tisores'
}

# Defineix regles de joc
regles_joc = {
    'pedra': ['tisores'],
    'paper': ['pedra'],
    'tisores': ['paper']
}

# Defineix resultats de joc
resultats_joc = {
    'win': 'Tu guanyes!',
    'lose': 'Tu perds!',
    'tie': 'Empat!'
}   

# Obté entrada de l'usuari
def obtenir_entrada_usuari():
    while True:
        try:
            entrada_usuari = input('Introdueix un número (1-3): ')
            if entrada_usuari.isdigit() and int(entrada_usuari) in opcions_joc:
                return opcions_joc[int(entrada_usuari)]
            else:
                print('Entrada no vàlida. Si us plau, torna a intentar-ho.')
        except ValueError:
            print('Entrada no vàlida. Si us plau, torna a intentar-ho.')

# Determina el resultat del joc
def obtenir_resultat_joc(opcio_usuari, opcio_ordinador)
    if opcio_usuari == opcio_ordinador:
        return resultats_joc['tie']
    elif opcio_ordinador in regles_joc[opcio_usuari]:
        return resultats_joc['win']
    else:
        return resultats_joc['lose']

# Mostra el resultat del joc
def mostrar_resultats_joc(resultat_joc, opcio_usuari, opcio_ordinador):
    print(f'Has triat {opcio_usuari}.')
    print(f'L\'ordinador ha triat {opcio_ordinador}.')
    print(resultat_joc)

# Juga el joc
def principal():
    print('Benvingut al joc de Pedra, Paper i Tisores!')
    while True:
        opcio_usuari = obtenir_entrada_usuari()
        opcio_ordinador = random.choice(list(opcions_joc.values()))
        resultat_joc = obtenir_resultat_joc(opcio_usuari, opcio_ordinador)
        mostrar_resultats_joc(resultat_joc, opcio_usuari, opcio_ordinador)
        jugar_de_nou = input('Vols jugar de nou? (sí/no): ')
        if jugar_de_nou.lower() != 'sí':
            break

if __name__ == '__main__':
    principal()

