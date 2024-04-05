# Starting with the string:
famous_words = "seven years ago..."
# Show two different ways to create a new string with "Four score and " 
# prepended to the front of the string.

# Method 1
famous_words1 = "Four score and " + famous_words
print(famous_words1)

# Method 2
famous_words2 = f'Four score and {famous_words}'
print(famous_words2)