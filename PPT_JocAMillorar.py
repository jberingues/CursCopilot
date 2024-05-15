# Desenvolupa un joc de Pedra, Paper i Tisores en Python basat en la consola
# El joc ha de ser modular, permetent actualitzacions fàcils o canvis de regles
# Implementa les regles del joc:
# - Pedra guanya a tisores
# - Tisores tallen paper
# - Paper cobreix pedra
# Inclou entrada d'usuari per seleccionar opcions i mostra els resultats del joc
# La interfície amb l'usuari ha de ser en català

import random

# Define game options
game_options = {
    1: 'pedra',
    2: 'paper',
    3: 'tisores'
}

# Define game rules
game_rules = {
    'pedra': ['tisores'],
    'paper': ['pedra'],
    'tisores': ['paper']
}

# Define game results
game_results = {
    'win': 'Tu guanyes!',
    'lose': 'Tu perds!',
    'tie': 'Empat!'
}   

# Get user input for game option
def get_user_input():
    while True:
        try:
            user_input = input('Introdueix un número (1-3): ')
            if user_input.isdigit() and int(user_input) in game_options:
                return game_options[int(user_input)]
            else:
                print('Entrada no vàlida. Si us plau, torna a intentar-ho.')
        except ValueError:
            print('Entrada no vàlida. Si us plau, torna a intentar-ho.')

# Determine game result
def get_game_result(user_option, computer_option)
    if user_option == computer_option:
        return game_results['tie']
    elif computer_option in game_rules[user_option]:
        return game_results['win']
    else:
        return game_results['lose']

# Display game results
def display_game_results(game_result, user_option, computer_option):
    print(f'Has triat {user_option}.')
    print(f'L\'ordinador ha triat {computer_option}.')
    print(game_result)

# Play the game
def main():
    print('Benvingut al joc de Pedra, Paper i Tisores!')
    while True:
        user_option = get_user_input()
        computer_option = random.choice(list(game_options.values()))
        game_result = get_game_result(user_option, computer_option)
        display_game_results(game_result, user_option, computer_option)
        play_again = input('Vols jugar de nou? (sí/no): ')
        if play_again.lower() != 'sí':
            break

if __name__ == '__main__':
    main()

