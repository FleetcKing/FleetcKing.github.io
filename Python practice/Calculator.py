num1 = float(input("enter the first number: "))
oporator = input(" chose an input (+ - * /): ")
num2 = float(input("enter your second number: "))

if oporator == "/": 
    result = num1 / num2
elif oporator == "+":
    result = num1 + num2
elif oporator == "-":
    result = num1 - num2
elif oporator == "*":
    result = num1 * num2
else:
    print(f"{oporator} is not a valad oporator. try again using (+ - * /)")

