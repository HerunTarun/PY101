# Write two distinct ways of reversing the list without mutating the original list.
numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]

# Method 1
numbers1 = list(reversed(numbers))
print(numbers1)

# Method 2
print(numbers[::-1])
    