# Determine whether the name Dino appears in the strings below 
# -- check each string separately:
str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."

def find_dino(string):
    return 'Dino' in string

print(find_dino(str1))
print(find_dino(str2))
    