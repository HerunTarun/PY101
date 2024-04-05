def crunch(string):
    newstring = ''
    index = 0
    length = len(string)
    while index < len(string):
        if string[index] == len(string) or string[index] != string[index + 1]:
            newstring += string[index]
        index += 1
    return newstring
# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')








# Solution:
# def crunch(string):
#     newstring = ''
#     index = 0
    
#     while index < len(string):
#         first = len(string) - 1
#         if index == first or string[index] != string[index + 1]:
#             newstring += string[index]
            
#         index += 1
    
#     return newstring














# Practice Tries
    # working = list(string)
    # index = 0
    # while working[index] == working[index + 1]:
    #     working.pop(index + 1)
    #     index += 1
    # return ''.join(working)