def greetings(name, position):
    f_name = ' '.join(name)
    return(f"Hello, {f_name}! It's nice to have a {position['title']} "
           f"{position['occupation']} around.")


greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.