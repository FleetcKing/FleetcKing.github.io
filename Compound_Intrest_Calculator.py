p = 0
r = 0
t = 0

while p <= 0:
    p = float(input("Enter the princeple ammount: "))
    if p <= 0:
        print("princeple cant be $0")

while r <= 0:
    r = float(input("Enter the intrest rate: "))
    if r <= 0:
        print("rate cant be %0")

while t <= 0:
    t = float(input("Enter the time in years to pay it off: "))
    if t <= 0:
        print("time cant be 0 years")

total = p * pow((1 + r / 100), t)

print(f"Starting price of {p} after {t} years with %{r} intrest rate is ${total:,.2f}")