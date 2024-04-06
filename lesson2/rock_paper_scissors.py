import json
import random
import os
import time

VALID_CHOICES = {'long': ['rock', 'paper', 'scissors', 'lizard', 'spock'],
                 'short': ['r', 'p', 's', 'l', 'k']}
WINNING_COMBINATIONS = {'rock': ['scissors', 'lizard'],
                        'scissors': ['paper', 'lizard'],
                        'paper': ['rock', 'spock'],
                        'lizard': ['spock', 'paper'],
                        'spock': ['scissors', 'rock']}
GAMES_TO_WIN = 3 # for a best of five match

def prompt(message):
    print(f'==> {message}')

def display_welcome():
    prompt(messages['welcome'])
    prompt(messages['name_intro'])
    prompt(messages['game_rules'])
    prompt(messages['match_rules'])

def display_loading_time():
    for num in range(1, 4):
        print(num * ".")
        time.sleep(1)

def display_replay_message():
    prompt(messages['replay'])

def display_goodbye():
    prompt(messages['goodbye'])

def display_game_result(winner, choice, computer_choice):
    if winner == 'win':
        prompt(messages['win'].format(choice = choice,
                                      computer_choice = computer_choice))
    elif winner == 'lose':
        prompt(messages['lose'].format(choice = choice,
                                       computer_choice = computer_choice))
    else:
        prompt(messages['tie'].format(choice = choice,
                                      computer_choice = computer_choice))

def display_match_score(scores):
    prompt(messages['match_score'].format(user_score = scores['user_score'],
                                    computer_score = scores['computer_score']))

def display_match_winner(scores):
    if scores['user_score'] == GAMES_TO_WIN:
        prompt(messages['user_match_winner'])

    if scores['computer_score'] == GAMES_TO_WIN:
        prompt(messages['computer_match_winner'])

    return False

def clear_score(scores):
    scores['user_score'] = 0
    scores['computer_score'] = 0

def clear_screen():
    os.system('clear')

def obtain_user_choice():
    prompt(messages['user_input'])

    choice = input()
    while is_invalid_input(choice):
        prompt(messages['invalid_input'])
        choice = input()

    choice = reformat_user_choice(choice)
    return choice

def is_invalid_input(choice):
    total_valid_inputs = []
    for inputs in VALID_CHOICES.values():
        total_valid_inputs += inputs

    if choice.lower() not in total_valid_inputs:
        return True

    return False

def reformat_user_choice(choice):
    if choice in VALID_CHOICES['long']:
        return choice

    match choice:
        case 'r':
            choice = 'rock'
        case 'p':
            choice = 'paper'
        case 's':
            choice = 'scissors'
        case 'l':
            choice = 'lizard'
        case 'k':
            choice = 'spock'

    return choice

def generate_computer_choice():
    computer_choice = random.choice(VALID_CHOICES['long'])

    return computer_choice

def calculate_winner(choice, computer_choice):
    if choice == computer_choice:
        return 'tie'

    if computer_choice in WINNING_COMBINATIONS[choice]:
        return 'win'

    return 'lose'

def update_match_score(winner, scores):
    if winner == 'win':
        scores['user_score'] += 1

    if winner == 'lose':
        scores['computer_score'] += 1

def is_game_over(scores):
    if GAMES_TO_WIN in list(scores.values()):
        return True

    return False

def restart_game():
    answer = input()
    while answer.lower() not in ['y', 'yes']:
        return False
    clear_screen()
    return True

def start_game():
    clear_screen()
    display_welcome()
    scores = {'user_score': 0, 'computer_score': 0}
    while True:
        choice = obtain_user_choice()
        computer_choice = generate_computer_choice()
        winner = calculate_winner(choice, computer_choice)

        update_match_score(winner, scores)

        clear_screen()
        display_loading_time()

        display_game_result(winner, choice, computer_choice)
        display_match_score(scores)

        if is_game_over(scores):
            display_match_winner(scores)
            clear_score(scores)
        else:
            continue

        display_replay_message()

        if not restart_game():
            display_goodbye()
            break

with open('rps_messages.json', 'r') as file:
    messages = json.load(file)

start_game()