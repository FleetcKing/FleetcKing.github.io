#nested loops are a loop whithin another loop:
# Outer loop
#    inner loop
#you can have any loop inside any loop. 

#make your string on one line
for x in range(1,11):
    print(x, end = "")
#space out your string
for x in range(1,11):
    print(x, end = " ")

#repete this 3 times
for x in range(3):
    for y in range(1,11):
        print(y, end = " ")

#repete the loop but in a new line each time
for x in range(3):
    for y in range(1,11):
        print(y, end = " ")
    print()

# Make a rectangle
rows = int(input("enter how many rows: "))
colums = int(input("enter how many colums: "))
symbol = input("enter the symbol of your choice: ")

for x in range(rows):
    for y in range(colums):
        print(symbol, end=" ")
    print()
