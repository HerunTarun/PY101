import json

def prompt(message):
    print(f'==> {message}\n')

with open('mortgagecalc_messages.json', 'r') as file:
    messages = json.load(file)

# Make a welcoming message
prompt(messages['start'])

# Obtain the loan amount
prompt(messages['obtain_loan_amount'])
loan_amount = input()

# Obtain the APR rate
prompt(messages['obtain_APR'])
apr = input()

# Obtain the loan duration
prompt(messages['obtain_mortgage_duration'])
mortgage_in_years = input()

# Calculate the monthly interest rate
monthly_interest = (loan_amount * apr) / 12

# Calculate the loan duration in months
mortgage_in_months = mortgage_in_years / 12

# Calculate the monthly payment
monthly_payment = loan_amount * (monthly_interest / (1 - (1 + monthly_interest) ** (-mortgage_in_months)))

# Print monthly payment
prompt(messages['payment'].format(monthly_payment = monthly_payment))



#TODO
# Convert all input to float
# clean up loan amount to remove commas when converting to float
# input validation to disallow negative numbers in loan amount and apr
# clean up for pylint


# Improvements
