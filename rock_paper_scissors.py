import json
import random
import os

VALID_CHOICES = {'long': ['rock', 'paper', 'scissors', 'lizard', 'spock'], 
                 'short': ['r', 'p', 's', 'l', 'k']}
WINNING_COMBINATIONS = {'rock': ['scissors', 'lizard'],
                        'scissors': ['paper', 'lizard'],
                        'paper': ['rock', 'spock'],
                        'lizard': ['spock', 'paper'],
                        'spock': ['scissors', 'rock']
}

def prompt(message):
    print(f'==> {message}')

def game_rules():
    prompt('placeholder')

def print_welcome():
    prompt(messages['welcome'])
    prompt(messages['game_rules'])

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
            choice = VALID_CHOICES["long"][0]
        case 'p':
            choice = VALID_CHOICES["long"][1]
        case 's':
            choice = VALID_CHOICES["long"][2]
        case 'l':
            choice = VALID_CHOICES["long"][3]
        case 'k':
            choice = VALID_CHOICES["long"][4]

    return choice

def generate_computer_choice():
    computer_choice = random.choice(VALID_CHOICES['long'])

    return computer_choice

def calculate_winner():
    choice = obtain_user_choice()
    computer_choice = generate_computer_choice()

    if choice == computer_choice:
        return messages['tie'].format(choice = choice, 
                                     computer_choice = computer_choice)

    if computer_choice in WINNING_COMBINATIONS[choice]:
        return messages['win'].format(choice = choice, 
                                      computer_choice = computer_choice)

    return messages['lose'].format(choice = choice, 
                                   computer_choice = computer_choice)

def print_winner():
    print(calculate_winner())

def play_again():
    answer = input()
    while answer.lower() not in ['y', 'yes']:
        return False
    os.system('clear')
    return True

def start_game():
    os.system('clear')
    print_welcome()
    while True:
        print_winner()
        prompt(messages['replay'])
        if not play_again():
            print(messages['goodbye'])
            break

with open('rps_messages.json', 'r') as file:
    messages = json.load(file)

start_game()
    
# TODO
# X restructure program to use functions
# X add json file for messages
# X Add clear screen at start of program and at replay
# X add goodbye message
# add help function
# add shortened input bonus feature
# add best of five bonus feature
# clear todo when done with code
# clean up pylint comments

