#lenth method
name = input("enter your name: ")
name = len(name)
print(name)

#.find() method
name = input("enter your name: ")
result = name.find("e")
print(result)

#.rfind() , reverse find method
name = input("enter your name: ")
result = name.rfind("e")
print(result)

#capitalises the first letter in a string
name = input("enter your name: ")
result = name.capitalize("e")
print(result)

#makes the whole string uppercase
name = input("enter your name: ")
result = name.upper("e")
print(result)

#makes the whole string lowercase
name = input("enter your name: ")
result = name.lower("e")
print(result)

#returns true if the string is all digets. returns false if there are any spaces or letters
name = input("enter your name: ")
result = name.isdigit("e")
print(result)

# returns true if there are all letters in the string. returns false if there are any spaces or numbers.
name = input("enter your name: ")
result = name.isalpha("e")
print(result)

#counts the number of occurances in a string
name = input("enter your name: ")
result = name.count("e")
print(result)

# #replaces a letter or number in a string with something of your choice 
name = input("enter your name: ")
result = name.replace("2", "3")
print(result)

#islower outputs true if all is lowercase. otherwise false
name = input("enter your name: ")
result = name.islower()
print(result)

#isupper outputs true if all is uppercase otherwise false
name = input("enter your name: ")
result = name.isupper()
print(result)