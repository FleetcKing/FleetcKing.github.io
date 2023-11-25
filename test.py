#validate username
#no longer than 12 charictors
#must have a number
#must have a capital
#no spaces

username = input("Enter your username. Limited to 12 charictors. Must include a number. Must have a capital. No spaces  : ")
name = username.find(" ")
name_c= username.count(str())
name_numb = username.isalpha()
name_cap = username.islower()

#12 charictors
while name_c > 13:
    print(f"{username} is invalid. Limited to 12 charictors")
    username = input("Enter your username. Limited to 12 charictors. Must include a number. Must have a capital. No spaces  : ")
    name_c= username.count(str())
#must include a number
while name_numb:
    print(f"{username} is invalid. Must include a number and no spaces.")
    username = input("Enter your username. Limited to 12 charictors. Must include a number. Must have a capital. No spaces  : ")
    name_numb = username.isalpha()
#must inclide a capital letter
while name_cap: 
    print(f"{username} is invalid. Must include a capital letter.")
    username = input("Enter your username. Limited to 12 charictors. Must include a number. Must have a capital. No spaces  : ")
    name_cap = username.islower()
#cant contain spaces
while name != -1: 
    print(f"{username} is invalid. No spaces")
    username = input("Enter your username. Limited to 12 charictors. Must include a number. Must have a capital. No spaces  : ")
    name = username.find(" ")

print(f"{username} is your username")

