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


jacksonville_home = []
home_sale = bool(input("is this home for sale? true or false: "))
if home_sale == True:
    print("this home is for sale")
elif home_sale == False:
    print("this home is not for sale")
else:
    print("try typing true or false again")
    home_sale = (input("if the home has a pool enter yes, if not enter no: "))

print(home_sale)

home_price = str(input("please enter the price of the home: "))
home_name = input("please enter the name of the home: ")
home_pool = (input("if the home has a pool enter yes, if not enter no: "))
if home_pool == "yes":
    print("has a pool")
elif home_pool == "no":
    print("does not have a pool")
else:
    print("try typing yes or no again")
    home_pool = (input("if the home has a pool enter yes, if not enter no: "))
        
jacksonville_home.extend([home_sale, home_name, home_price, home_pool])

    
print(jacksonville_home)

if jacksonville_home[0]:
    print("this house is for sale!")
    print(f"the cost of {jacksonville_home[1]} is {jacksonville_home[2]}")
    print(f"this home {jacksonville_home[3]}")
else:
    print("this house is NOT for sale")








