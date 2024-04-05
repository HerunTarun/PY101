from datetime import datetime

age = int(input("How old are you? "))
re_age = int(input("At what age would you like to retire? "))

current_year = datetime.now().year
re_year = current_year + re_age
years_left = re_age - age

print(f"It's {current_year}. You will retire in {re_year}."
    f" You only have {years_left} years of work to go!")