#this is a program that im making for myself to calculate reps and sets of bench for my workout program

bench_max_input = input("enter your current bench max?: ")

starting_day = int(input("enter what day your starting the program: "))

starting_month = int(input("enter the month your starting the program: "))

print(f"so your starting with a bench max of {bench_max_input} on {starting_day}/{starting_month} correct?")

max_day_month_conformation = int(input("enter 1 if correct and 0 if incorrect: "))

ending_day = starting_day + 30

for days in range(starting_day, ending_day):
    print(days)
