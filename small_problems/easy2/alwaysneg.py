def negative(number):
    return number * (-1) if number > 0 else number
    # return -abs(number)

print(negative(5) == -5)      # True
print(negative(-3) == -3)     # True
print(negative(0) == 0)       # True