def odd_or_even(number):
    number = number * (-1)
    if number % 2 == 0:
        return False
    else:
        return True
        
print(odd_or_even(-1))
print(odd_or_even(-54))
print(odd_or_even(45))
print(odd_or_even(88))
print(odd_or_even(19))
print(odd_or_even(0))

# another way
# return abs(number) % 2 == 1