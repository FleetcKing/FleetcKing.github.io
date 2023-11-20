#pounds to kilograms calculator
while True:
    conversion = str.lower(input('''Do you want to convert kilograms to pounds or pounds to kilograms? Enter "kg" to convert kilograms, and "lb" to convert pounds: '''))
    if conversion == "lb":
        conversion = 1
        break
    if conversion == "kg":
        conversion = 0
        break
    print(f'''{conversion} is not valad. Try entering "lb" for pounds and "kg" for kilograms. This is case sensitive''')
    
if conversion == True: 
    lb = float(input("How many pounds do you want to convert?: "))
    solution = lb * 0.4535
    print(f"{lb}lbs is {solution}kg")

if conversion == False: 
    kg = float(input("How many kilograms do you want to convert?: "))
    solution = kg * 2.2046
    print(f"{kg} kilograms is {solution} pounds")