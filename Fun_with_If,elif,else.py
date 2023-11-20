# user_age = int(input("enter your age: "))
# if user_age > 100:
#     print("you are to old")
# elif user_age >= 18:
#     print("you are signed up") 
# elif user_age <= 0:
#     print("your not born yet")
# else:
#     print("sorry you must be 18+ to sign up")


# response = input("should we go out to eat tonight y/n: ")
# if response == "n":
#     print("what do we have to eat at home")
# elif response == "y":
#     print("wher do you wanna go for dinner")
# else :
#     print("try answering again y for yes and n for no")

# name = input("enter your name")
# if name == "":
#     print("you did not enter your name")
# else:
#     print(f"hello {name}")


# user_input = int(input("what iphone do you have: "))
# if user_input == 15:
#     print("you have the newest iphone")
# elif user_input > 15:
#     print("phone from the future, nice!")
# elif user_input == 1: 
#     print("you have a piece of history in your pocket")
# elif user_input <= 10 > 15:
#     print("you have a newer generation of iphone")
# elif user_input <= 0:
#     print("that phone doeset exist try again")
# elif user_input < 10 >= 2:
#     print("you have an older gen of iphone")
# else:
#     print("try typing again but just in a number like 10,11,12 ect")


home = []

print ("Is the house for sale?")
while True:
    home_sale = int(input("pick a number, 1 is yes, 2 is no: "))
    if home_sale == 1:
        home.insert(0,"is for sale!",)
        break
    if home_sale == 2:
        home.insert(0,"is not for sale")
        break
    print("you have made an invalid choice, try again.")
    
home_price = str(input("please enter the price of the house: "))
home.insert(2,home_price)

home_name = input("please enter the name of the house: ")
home.insert(1,home_name)

print ("does the house have a pool??")
while True:
    home_pool = int(input("pick a number, 1 is yes, 2 is no: "))
    if home_pool == 1:
        home.insert(4,"this house comes with a pool",)
        break
    if home_pool == 2:
        home.insert(4,"this house does not have a pool")
        break
    print("you have made an invalid choice, try again.")

print(f"{home[1]} {home[0]}")
print(f"the cost of this house is ${home[2]}")
print(f"{home[3]}")







