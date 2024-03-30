import json
import random
import os

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']
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
    print(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = input()
    while choice not in VALID_CHOICES:
        print("That's not a valid choice")
        choice = input()

    return choice

def is_invalid_input():
    # add input validation
    prompt('placeholder')

def generate_computer_choice():
    computer_choice = random.choice(VALID_CHOICES)
    
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
        prompt("Do you want to play again (y/n)?")
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

