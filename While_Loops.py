#while loop will execute code while some condition remains true
name = input("enter your name: ")

#strings
while name == "":
    print("you did not enter your name")
    name = input("enter your name: ")
print(f"your name is {name}")

#integers
age = int(input("enter your age: "))
while age < 0: 
    print("you wherent born yet, try again!: ")
    age = int(input("enter your age: "))
print(f"you are {age} years old")

#logical oporators

food = input("enter a food you like (q to quit): ")
while not food == "q":
    print(f"you like {food}")
    food = input("enter another food you like (q to quit): ")

print("bye")

food = input("enter a food you like (q to quit): ")
while food != "q":
    print(f"you like {food}")
    food = input("enter another food you like (q to quit): ")

print("bye")

# "or" logical oporator
num = int(input("enter a number between 1-10: "))
while num < 1 or num > 10:
    print(f"{num} is not valad: ")
    num = int(input("enter a number between 1-10: "))
print(f"you chose {num}")
    