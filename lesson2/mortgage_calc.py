import json
import os

MONTHS_IN_YEAR = 12

def prompt(message):
    print(f'==> {message}')

def obtain_loan():
    prompt(messages['obtain_loan_amount'])
    loan_amount = input().replace(',', '')

    while is_invalid_loan_amount(loan_amount):
        prompt(messages['invalid_loan_input'])
        loan_amount = input().replace(',', '')

    return loan_amount

def obtain_apr():
    prompt(messages['obtain_apr'])
    apr = input()

    while is_invalid_apr(apr):
        prompt(messages['invalid_apr_input'])
        apr = input()

    return apr

def obtain_duration():
    unit = choose_mortgage_duration_unit()
    prompt(choose_mortgage_duration_prompt(unit))
    mortgage_duration = input()

    while is_invalid_duration(mortgage_duration):
        prompt(messages['invalid_duration_input'])
        mortgage_duration = input()

    return mortgage_duration, unit

def choose_mortgage_duration_unit():
    prompt(messages['choose_mortgage_duration_unit_1'])
    prompt(messages['choose_mortgage_duration_unit_2'])
    unit = input().lower()

    while is_invalid_unit(unit):
        prompt(messages['invalid_mortgage_unit'])
        unit = input().lower()

    return unit

def choose_mortgage_duration_prompt(unit):
    match unit:
        case 'y':
            return messages['obtain_mortgage_duration_years']
        case 'm':
            return messages['obtain_mortgage_duration_months']

def is_invalid_input(number):
    try:
        float(number)
    except ValueError:
        return True

    if str(number) in ['nan', 'inf', '']:
        prompt(messages['funny_input'])
        return True

    if float(number) < 0:
        return True

    return False

def is_zero_input(number):
    if float(number) == 0:
        return True

    return False

def is_invalid_loan_amount(number):
    if is_invalid_input(number) or is_zero_input(number):
        return True

    return False

def is_invalid_apr(number):
    if is_invalid_input(number):
        return True

    return False

def is_invalid_duration(number):
    if is_invalid_input(number) or is_zero_input(number):
        return True

    return False

def is_invalid_unit(unit_str):
    try:
        str(unit_str)
    except ValueError:
        return True

    if str(unit_str) not in ['y', 'm']:
        return True

    if str(unit_str) in ['nan', 'inf', '']:
        prompt(messages['funny_input'])
        return True

    return False

def calculate_interest_factor(apr, duration, unit):
    if unit != 'm':
        duration = float(duration)
        duration *= MONTHS_IN_YEAR

    if float(apr) == 0:
        return 1 / float(duration)

    monthly_rate =  (float(apr)/100) / MONTHS_IN_YEAR
    interest_denominator = 1 - (1 + monthly_rate) ** (-float(duration))

    return monthly_rate / interest_denominator

def calculate_monthly_payment(loan_amount, apr, duration, unit):
    interest_factor = calculate_interest_factor(apr, duration, unit)
    monthly_payment = float(loan_amount) * interest_factor

    return monthly_payment

def obtain_loan_details():
    loan_amount = obtain_loan()
    apr = obtain_apr()
    duration, unit = obtain_duration()
    monthly_payment = calculate_monthly_payment(loan_amount,
                                                apr,
                                                duration,
                                                unit)

    return loan_amount, apr, duration, unit, monthly_payment

def format_unit_in_payment(unit, duration):
    match unit:
        case 'y':
            if float(duration) == 1:
                return 'year'
            return 'years'
        case 'm':
            if float(duration) == 1:
                return 'month'
            return 'months'

def print_monthly_payment():
    loan_amount, apr, duration, unit, monthly_payment = obtain_loan_details()

    unit = format_unit_in_payment(unit, duration)

    prompt(messages['payment'].format(monthly_payment = monthly_payment,
                                  loan_amount = loan_amount,
                                  apr = apr,
                                  unit = unit,
                                  duration = duration))

def repeat_program():
    retry = input()
    while retry.lower() not in ['y', 'yes']:
        return False
    os.system('clear')
    return True

def start_program():
    os.system('clear')
    prompt(messages['start'])
    while True:
        print_monthly_payment()
        prompt(messages['retry'])
        if not repeat_program():
            prompt(messages['goodbye'])
            break

with open('mortgagecalc_messages.json', 'r') as file:
    messages = json.load(file)

start_program()

# Code Review
# refactor program to accurately reflect what's happening in th emain loop