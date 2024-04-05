# Write two different ways to remove all of the elements from the following list:
numbers = [1, 2, 3, 4]

# Method 1
numbers.clear()

# Method 2
while numbers:
    numbers.pop(0)
print(numbers)