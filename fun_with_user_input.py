#madlib
adjective = input("enter an adjective: ")
location = input("enter a location: ")
name = input("enter a name: ")
adjective2 = input("enter another adjective: ")
pronoun = input(f"enter {name}'s girl/boy/them pronouns: ")
gender = input(f"enter {name}'s gender: ")
adjective3 = input("enter another adjective: ")
verb = input("enter a verb: ")

print(f"on one {adjective} morning in {location}, there was a young boy named {name}, skipping down the sidewalk. {name} was a {adjective2} little {pronoun} and all {gender}" 
          f" wanted was a {adjective3} ice cream. while {verb} the road to the ice cream truck {name} got hit by a car and died. the end")

#volume calculator
lenth = float(input("enter lenth: "))
width = float(input("enter width: "))
height = float(input("enter height: "))

volume = lenth * width * height

print(volume)

#item total calculator 
item = input("what did you get: ")
ammount = float(input(f"how many {item}'s did you get: "))
price = float(input(f"how much do {item}'s cost?: "))

total = price * ammount

print(total)



