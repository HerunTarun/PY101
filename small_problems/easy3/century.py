def century(year):
    century = year // 100
    if year % 10 != 0:
        century += 1
    
    if str(century).endswith("11"):
        return str(century) + "th"
    elif str(century).endswith("12"):
        return str(century) + "th"     
    elif str(century).endswith("13"):
        return str(century) + "th"       
        
    if str(century)[-1] == "1":
        return str(century) + "st"
    elif str(century)[-1] == "2":
        return str(century) + "nd"
    elif str(century)[-1] == "3":
        return str(century) + "rd"
    else:
        return str(century) + "th"
        
        
        
print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True