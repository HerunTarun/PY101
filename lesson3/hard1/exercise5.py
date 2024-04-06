# What do you expect to happen when the greeting variable is 
# referenced in the last line of the code below?
if False:
    greeting = "hello world"

print(greeting)

# An **NameError  will be raised. Variable used before assignment. 
# Since the if loop was never entered, python won't register that a variable
# was initialized