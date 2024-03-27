import json
import os

def prompt(message):
    print(f'==> {message}')

def check_invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False

def choose_language():
    prompt("Please enter 'en' for english and 'fr' for francais")
    language = input().strip().lower()

    while language.lower() not in ['english', 'francais', 'en', 'fr']:
        prompt("Try either 'english' or 'francais'!")
        prompt("Essayez « english » ou « francais »!")
        language = input().strip().lower()

    match language:
        case 'english':
            language = 'en'
        case 'en':
            language = 'en'
        case 'francais':
            language = 'fr'
        case 'fr':
            language = 'fr'

    return language

def obtaining_numbers():
    prompt(data['first'])
    number1 = input().strip()

    while check_invalid_number(number1):
        prompt(data['invalid_num'])
        number1 = input().strip()

    prompt(data['second'])
    number2 = input().strip()

    while check_invalid_number(number2):
        prompt(data['invalid_num'])
        number2 = input().strip()

    return number1, number2

def check_invalid_division(num1, num2):
    try:
        float(num1) / float(num2)
    except ZeroDivisionError:
        return True
    return False

def obtaining_operation():
    prompt(data['select'])
    operation = input().strip()

    while operation not in ['1', '2', '3', '4']:
        prompt(data['invalid_select'])
        operation = input().strip()

    return operation

def make_calculation(number1, number2, operation):
    match operation:
        case '1':     # 1 represents addition
            output = float(number1) + float(number2)
            operation = "+"
        case '2':     # 2 represents subtraction
            output = float(number1) - float(number2)
            operation = "-"
        case '3':      # 3 represents multiplication
            output = float(number1) * float(number2)
            operation = "*"
        case '4':      # 4 represents division
            while check_invalid_division(number1, number2):
                prompt(data['invalid_division'])
                number1, number2 = obtaining_numbers()

            output = float(number1) / float(number2)
            operation = "/"

    return output, operation


def main():
    number1, number2 = obtaining_numbers()

    operation = obtaining_operation()

    output, operation = make_calculation(number1, number2, operation)

    prompt(f'{number1} {operation} {number2} = {output:.2f}')

def prompt_play_again():
    prompt(data['again'])
    retry = input()
    if retry != 'y':
        prompt(data['bye'])
        return False

    return True

with open ('calculator_messages.json', 'r') as file:
    data = json.load(file)[choose_language()]

prompt(data['start'])

while True:
    main()

    if not prompt_play_again():
        break

    os.system('clear')