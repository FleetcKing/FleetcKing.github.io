#computer guess
import random 
gen_guess = random.randint(0,2)
gen_guess = str(gen_guess)
computer_guess = []
if gen_guess == "0":
    computer_guess.append("rock")
if gen_guess == "1":
    computer_guess.append("paper")
if gen_guess == "2":
    computer_guess.append("scissors")
#user guess
user_guess = str.lower(input('''guess rock paper scissors. type "r" for rock, "p" for paper, and "s" for scissors: '''))
user_guess_string = []
if user_guess == "r":
    user_guess_string.append("rock")
if user_guess == "p":
    user_guess_string.append("paper")
if user_guess == "s":
    user_guess_string.append("scissors")

#draw
if user_guess == "r" and gen_guess == "0" or user_guess == "p" and gen_guess == "1" or user_guess == "s" and gen_guess == "2":
    print(f"you chose {user_guess_string}, computer chose {computer_guess}. thats a draw")
#user win
if user_guess == "r" and gen_guess == "2" or user_guess == "p" and gen_guess == "0" or user_guess == "s" and gen_guess == "1":
    print(f"you chose {user_guess_string}, computer chose {computer_guess}. you win")
#user loose
if user_guess == "r" and gen_guess == "1" or user_guess == "p" and gen_guess == "2" or user_guess == "s" and gen_guess == "0":
    print(f"you chose {user_guess_string}, computer chose {computer_guess}. you loose")