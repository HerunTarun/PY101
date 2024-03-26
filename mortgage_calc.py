import json

def prompt(message):
    print(f'==> {message}')

def valid_input():
    try:
        float(loan_amount)
    except ValueError:
        return True

    if str(loan_amount) in ['nan', 'inf']:
        prompt(messages['funny_input'])
        return True

    return False


with open('mortgagecalc_messages.json', 'r') as file:
    messages = json.load(file)

# Make a welcoming message
prompt(messages['start'])

# Obtain the loan amount
prompt(messages['obtain_loan_amount'])
loan_amount = input().replace(',', '')

# validate loan amount
while valid_input():
    prompt(messages['invalid_loan_input'])
    loan_amount = input().replace(',', '')

# Obtain the APR rate
prompt(messages['obtain_apr'])
apr = float(input()) / 100

# validate APR input
while valid_input():
    prompt(messages['invalid_apr_input'])
    loan_amount = input().replace(',', '')

# Obtain the loan duration
prompt(messages['obtain_mortgage_duration'])
mortgage_in_months = float(input())

# Calculate the monthly interest rate
monthly_interest_rate =  apr / 12

# Calculate the monthly payment
interest_factor = 1 - ((1 + monthly_interest_rate) ** (-mortgage_in_months))
monthly_payment = loan_amount * (monthly_interest_rate / interest_factor)

# Print monthly payment
prompt(messages['payment'].format(monthly_payment = monthly_payment))



# TODO
# X Convert all input to float
# X clean up loan amount to remove commas when converting to float
# input validation to disallow negative numbers in loan amount and apr
# clean up for pylint


# Improvements
