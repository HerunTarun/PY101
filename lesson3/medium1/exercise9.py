# Consider these two simple functions:
def foo(param="no"):
    return "yes"

def bar(param="no"):
    return param == "no" and foo() or "no"
# What will the following function invocation return?

print(bar(foo()))

# foo will return 'yes', which then goes into bar() as an argument
# False and True or 'no'
# so the function call should evaluate to 'no'