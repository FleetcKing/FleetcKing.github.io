#Arithmatic operators________________
trends = 1

#addition operator 
trends = trends + 1 

#subtraction operator 
trends = trends -  2

#multiplication operator 
trends = trends * 3

#division operator 
trends = trends / 3

#exponent operator 
trends = trends ** 5

#augmented assignment operator
trends += 1
trends -= 2
trends *= 3
trends /= 4
trends **= 5
#modulo operator: gives the remainder of the divided variable. popular to use it to find if the outcome is even or odd. 
trends %= 6 

print(trends)


#Built in functions_________________
x = 2.4
y = -8
z = 1.6

#round function: rounds x to the nearest whole integer
result = round(.8)
result = round(x)

#absolute value: distance away from 0 as a whole number
result = abs(-5)
result = abs(y)

#power: raises your variable or number to the power of your choice
result = pow(1, 3)
result = pow(y, 3)

#max: finds the maximum value between variables 
result = max(x,y,z)

#min: finds the minimum value between variables
result = min(x,y,z)

print(result)


#Math modules_______________________
import math 

#value of pi
print(math.pi)

# exponential constant or E
print(math.e)

#taking the square root of a number 
x = 9.1
result - math.sqrt(x)
print(result)

#ceiling function: will always round up 
result = math.ceil(x)
print(result)

#floor function: will always round down
result = math.floor(x)
print(x)


#circumference of a circle calculator__________________
import math
radious = float(input("enter the circles radious: "))
circumference = math.pi * 2 * radious
print(circumference)


#area of a circle calculator_________________
import math
radious = float(input("enter the radious: "))
area = math.pi * radious ** 2
print(area)


#hypotinuse calculator_____________
import math
leg = float(input("enter the leg(a) of the triangle: "))
bottom = float(input("enter bottom(b) of the triangle: "))
hypotinuse = math.sqrt(leg ** 2 + bottom ** 2)
print(hypotinuse)
