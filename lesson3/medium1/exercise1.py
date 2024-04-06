# For this practice problem, write a program that outputs 
# The Flintstones Rock! 10 times, with each line indented 
# 1 space to the right of the line above it. 
# The output should start out like this:
# The Flintstones Rock!
#  The Flintstones Rock!
#   The Flintstones Rock!
#   ...

counter = 0
while counter < 10:
    print(counter * " " + "The Flintstones Rock!" )
    counter += 1

# Another Method

for space in range(10):
    print(space * " " + "The Flintstones Rock!")