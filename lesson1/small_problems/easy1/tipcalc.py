bill = float(input('What is the bill? '))
tip_rate = float(input('What is the tip percentage? ')) / 100
print()
tip = bill * tip_rate
print(f'The tip is ${tip:.2f}')
total = bill + tip
print(f'The total is ${total:.2f}')