# What will the following code do?

def my_func():
    num = 10

my_func()
print(num)

# This code will raise a NameError, since num is not defined in the
# the global scope. The num inside my_func is local to that function