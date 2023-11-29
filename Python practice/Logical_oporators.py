#logical oporators are used on conditional statements like if statements. 
#and oporators check if two or more conditions are true
#or checks if at least one condition is true
#not changes the result of a condition. if true its now false and vise versa 

temp = -10
if temp > 0 and temp < 30:
    print("the tempeture is good")
else:
    print("the tempeture is bad")

temp2 = 40
if temp2 <= 0 or temp2 >=30:
    print("temp is bad")
else:
    print("temp is good")

#boolian conditional statement
sunny = True

if not sunny:
    print("its sunny outside")
else:
    print("its cloudy outside")