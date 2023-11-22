
unit = str.lower(input("enter your starting unit of fahrehneight, celcious, or kelvin (F,C,K): "))
temp = float(input("enter the tempeture in a number: "))
converted_unit = str.lower(input("what unit would you like to convert too (F,C,K): "))

if unit == "f" and converted_unit == "c":
    solution = (temp - 32) * 5/9
elif unit == "c" and converted_unit == "f":
    solution = (temp * 9/5) + 32
elif unit == "f" and converted_unit == "k":
    solution = (temp - 32) * 5/9 + 273.15
elif unit == "c" and converted_unit == "k":
    solution = temp + 273.15
elif unit == "k" and converted_unit == "f":
    solution = (temp - 273.15) * 9/5 + 32
elif unit == "k" and converted_unit == "c":
    solution = temp - 273.15 

print(round(solution))





        