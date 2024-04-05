# How can you determine whether a given string ends with an exclamation mark (!)? 
# Write some code that prints True or False depending on whether 
# the string ends with an exclamation mark.


def ends_with_exclamation(string):
    return string.endswith('!')
    
str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

print(ends_with_exclamation(str1))
print(ends_with_exclamation(str2))


