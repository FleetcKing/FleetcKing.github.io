#username may be no longer than 12 charictors
#username my have no spaces
#username must not contain digets

username = input("Enter your username. 12 charictors maximum, no spaces, cant contain numbers: ")
name_len = len(username)
name_space = username.find(" ")
name_numb = username.isalpha()

# while name_len > 12 or name_space != -1 or not name_numb:
#     if name_len > 12:
#         print(f"{username} is invalid. Username must not be longer than 12")
#         username = input("Enter your username. 12 charictors maximum, no spaces, cant contain numbers: ")   
#         print(f"your username is {username}")
    
#     elif name_space != -1:
#         print(f"{username} is invalid. Username cant have spaces")
#         username = input("Enter your username. 12 charictors maximum, no spaces, cant contain numbers: ")
#         print(f"your username is {username}")
    
#     elif not name_numb:
#         print(f"{username} is invalad. Must not contain numbers")
#         username = input("Enter your username. 12 charictors maximum, no spaces, cant contain numbers: ")
#         print(f"your username is {username}")

#cant break out of the while loop

if len(username) > 12:
    print("Your username cant be longer than 12!")

elif not username.find(" ") == -1:
    print("Your username cant have spaces!")
elif not username.isalpha():
    print("No numbers!")
else:
    print(f"your username is {username}")


