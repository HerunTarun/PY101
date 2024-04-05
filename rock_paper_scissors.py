import json
import random
import os

VALID_CHOICES = {'long': ['rock', 'paper', 'scissors', 'lizard', 'spock'],
                 'short': ['r', 'p', 's', 'l', 'k']}
WINNING_COMBINATIONS = {'rock': ['scissors', 'lizard'],
                        'scissors': ['paper', 'lizard'],
                        'paper': ['rock', 'spock'],
                        'lizard': ['spock', 'paper'],
                        'spock': ['scissors', 'rock']}
ROUNDS_TO_WIN = 3 # for a best of five match

def prompt(message):
    print(f'==> {message}')

def print_welcome():
    prompt(messages['welcome'])
    prompt(messages['name_intro'])
    prompt(messages['game_rules'])
    prompt(messages['match_rules'])

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

    if choice not in total_valid_inputs:
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
        scores.append('1')

    if winner == 'lose':
        scores.append('2')

def display_game_score(winner, choice, computer_choice):
    if winner == 'win':
        prompt(messages['win'].format(choice = choice,
                                      computer_choice = computer_choice))
    elif winner == 'lose':
        prompt(messages['lose'].format(choice = choice,
                                       computer_choice = computer_choice))
    else:
        prompt(messages['tie'].format(choice = choice,
                                      computer_choice = computer_choice))

def display_match_score(user_score, computer_score):
    prompt(messages['match_score'].format(user_score = user_score,
                                          computer_score = computer_score))

def clear_score(scores):
    scores.clear()

def is_game_over(user_score, computer_score):
    if ROUNDS_TO_WIN in (user_score, computer_score):
        return True

    return False

def display_match_winner(user_score, computer_score):
    if user_score == ROUNDS_TO_WIN:
        prompt(messages['user_match_winner'])

    if computer_score == ROUNDS_TO_WIN:
        prompt(messages['computer_match_winner'])

    return False

def play_again():
    answer = input()
    while answer.lower() not in ['y', 'yes']:
        return False
    os.system('clear')
    return True

def start_game():
    os.system('clear')
    print_welcome()
    scores = []
    while True:
        choice = obtain_user_choice()
        computer_choice = generate_computer_choice()
        winner = calculate_winner(choice, computer_choice)
        update_match_score(winner, scores)
        user_score = scores.count('1')
        computer_score = scores.count('2')
        os.system('clear')
        display_game_score(winner, choice, computer_choice)
        display_match_score(user_score, computer_score)

        if is_game_over(user_score, computer_score):
            display_match_winner(user_score, computer_score)
            clear_score(scores)
        else:
            continue

        prompt(messages['replay'])
        if not play_again():
            prompt(messages['goodbye'])
            break

with open('rps_messages.json', 'r') as file:
    messages = json.load(file)

start_game()