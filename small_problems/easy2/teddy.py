import random

name = input('What is your name? ')

if name == '':
    name = 'Teddy'
    
age = random.randint(20, 100)

print(f'{name} is {age} years old!')