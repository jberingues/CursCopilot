# TODO: Develop a console-based Rock Paper Scissors Lizard Spock game in Python
# Game should be modular, allowing for easy updates or rule changes
# Implement game rules:
# - Scissors decapitate lizard
# - Scissors cuts paper
# - Paper covers rock 
# - Rock crushes lizard 
# - Lizard poisons Spock 
# - Spock smashes scissors 
# - Lizard eats paper 
# - Paper disproves Spock 
# - Spock vaporizes rock 
# - Rock crushes scissors
# Include user input for selecting options and display game results

import random

# Define game options
game_options = {
    1: 'rock',
    2: 'paper',
    3: 'scissors',
    4: 'lizard',
    5: 'Spock'
}

# Define game rules
game_rules = {
    'rock': ['scissors', 'lizard'],
    'paper': ['rock', 'Spock'],
    'scissors': ['paper', 'lizard'],
    'lizard': ['Spock', 'paper'],
    'Spock': ['scissors', 'rock']
}

# Define game results
game_results = {
    'win': 'You win!',
    'lose': 'You lose!',
    'tie': 'It\'s a tie!'
}

# Get user input for game option
def get_user_input():
    while True:
        try:
            user_input = input('Enter a number (1-5) or text to select an option: ')
            if user_input.isdigit() and int(user_input) in game_options:
                return game_options[int(user_input)]
            elif user_input.lower() in game_options.values():
                return user_input.lower()
            else:
                print('Invalid input. Please try again.')
        except ValueError:
            print('Invalid input. Please try again.')
            
# Determine game result
def get_game_result(user_option, computer_option):
    if user_option == computer_option:
        return game_results['tie']
    elif computer_option in game_rules[user_option]:
        return game_results['win']
    else:
        return game_results['lose']
    
# Display game results
def display_game_results(game_result, user_option, computer_option):
    print(f'You chose {user_option}.')
    print(f'The computer chose {computer_option}.')
    print(game_result)

# Main function
def main():
    print('Welcome to Rock Paper Scissors Lizard Spock!')
    print('Select an option:')
    for key, value in game_options.items():
        print(f'{key}: {value}')
    user_option = get_user_input()
    computer_option = random.choice(list(game_options.values()))
    game_result = get_game_result(user_option, computer_option)
    display_game_results(game_result, user_option, computer_option)

# Run main function
if __name__ == '__main__':
    main()

