import json

def prompt(message):
    print(f'==> {message}')

def valid_input(number):
    try:
        float(number)
    except ValueError:
        return True

    if str(number) in ['nan', 'inf', '']:
        prompt(messages['funny_input'])
        return True
    elif float(number) < 0:
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
while valid_input(loan_amount):
    prompt(messages['invalid_loan_input'])
    loan_amount = input().replace(',', '')

# Obtain the APR rate
prompt(messages['obtain_apr'])
apr = input()

# validate APR input
while valid_input(apr):
    prompt(messages['invalid_apr_input'])
    apr = input()

# Obtain the loan duration
prompt(messages['obtain_mortgage_duration'])
mortgage_in_months = input()

# validate loan duration
while valid_input(mortgage_in_months):
    prompt(messages['invalid_duration_input'])
    mortgage_in_months = input()

# Calculate the monthly interest rate
monthly_rate =  float(apr) / 12

# Calculate the monthly payment
interest_factor = 1 - ((1 + monthly_rate) ** (-float(mortgage_in_months)))
monthly_payment = float(loan_amount) * (monthly_rate / interest_factor)

# Print monthly payment
prompt(messages['payment'].format(monthly_payment = monthly_payment))



# TODO
# X Convert all input to float
# X clean up loan amount to remove commas when converting to float
# X input validation to disallow negative numbers in loan amount and apr
# fix calculation
# clean up for pylint


# Improvements
