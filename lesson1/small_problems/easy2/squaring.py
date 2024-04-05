def multiply(num1, num2):
    return num1 * num2
    
def square(num):
    return  multiply(num, num)
    

# print(square(5) == 25)   # True
# print(square(-8) == 64)  # True

# Further Exploration

def power(num, power):
    return multiply(num, num) * (num ** (power - 2))
    
print(power(-2, 1))