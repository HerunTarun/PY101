# What will the following code print and why?

def outer():
    outer_var = 'Hello'

    def inner():
        inner_var = 'World'
        print(outer_var, inner_var)

    inner()

outer()

# This will print 'Hello World' because the inner() function
# has a locally scoped inner_var variable, and can access the 
# outer_var variable in the outer scope