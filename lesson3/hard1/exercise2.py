# What does the last line in the following code output?
dictionary = {'first': [1]}
num_list = dictionary['first']
num_list.append(2)

print(num_list)
print(dictionary)

# It will print {'first': [1, 2]} because the nested list will be changed, 
# which is then reflected when the dictionary object is referenced
