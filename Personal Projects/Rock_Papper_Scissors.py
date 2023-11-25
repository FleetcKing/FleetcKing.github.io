#singleplayer
def single_player():
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
        while user_guess != "r" and user_guess != "p" and user_guess != "s":
            print(f"{user_guess} is invalid")
            user_guess = str.lower(input('''try typeing "r" for rock, "p" for paper, and "s" for scissors: '''))
        
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
#multiplayer
def multiplayer():
        #user1 guess
        player1_name = input("Player 1, enter your name: ")
        while player1_name == "":
            print("you must type in your name: ")
            player1_name = input("Player 1, enter your name: ")
        player1  = str.lower(input('''Player 1, guess rock paper scissors. type "r" for rock, "p" for paper, and "s" for scissors: '''))
        while player1 != "r" and player1 != "p" and player1 != "s":
            print(f"{player1} is invalid")
            player1  = str.lower(input('''Try typeing "r" for rock, "p" for paper, and "s" for scissors: '''))
        player1_string = []
        if player1 == "r":
            player1_string.append("rock")
        if player1 == "p":
            player1_string.append("paper")
        if player1 == "s":
            player1_string.append("scissors")
        
        #user2 guess
        player2_name = input("player 2 enter your name: ")
        while player2_name == "":
            print("you must type in your name: ")
            player2_name = input("Player 2, enter your name: ")
        player2  = str.lower(input('''Player 2, guess rock paper scissors. type "r" for rock, "p" for paper, and "s" for scissors: '''))
        while player2 != "r" and player2 != "p" and player2 != "s":
            print(f"{player2} is invalid")
            player2  = str.lower(input('''Try typeing "r" for rock, "p" for paper, and "s" for scissors: '''))
        player2_string = []
        if player2 == "r":
            player2_string.append("rock")
        if player2 == "p":
            player2_string.append("paper")
        if player2 == "s":
            player2_string.append("scissors")

        #draw
        if player1 == "r" and player2 == "r" or player1 == "p" and player2 == "p" or player1 == "s" and player2 == "s":
            print(f"{player1_name} chose {player1_string}, {player2_name} chose {player2_string}. Thats a draw")
        #player 1 win
        if player1 == "r" and player2 == "s" or player1 == "p" and player2 == "r" or player1 == "s" and player2 == "p":
            print(f"{player1_name} chose {player1_string}, {player2_name} chose {player2_string}. {player1_name} Wins!")
        #player 2 win
        if player1 == "r" and player2 == "p" or player1 == "p" and player2 == "s" or player1 == "s" and player2 == "r":
            print(f"{player1_name} chose {player1_string}, {player2_name} chose {player2_string}. {player2_name} Wins!")
#cheats
def cheats():
        #user1 guess
        player1_name = input("Player 1, enter your name: ")
        while player1_name == "":
            print("you must enter your name: ")
            player1_name = input("Player 1, enter your name: ")
        
        player1 = str.lower(input('''Player 1, guess rock paper scissors. type "r" for rock, "p" for paper, and "s" for scissors: '''))
        while player1 != "r" and player1 != "p" and player1 != "s":
            print(f"{player1} is invalid")
            player1  = str.lower(input('''try typing "r" for rock, "p" for paper, and "s" for scissors: '''))
        
        #user2 guess
        player2_name = input("player 2 enter your name: ")
        while player2_name == "":
            print("you must enter your name: ")
            player2_name = input("player2 enter your name: ")
        player2  = str.lower(input('''Player 2, guess rock paper scissors. type "r" for rock, "p" for paper, and "s" for scissors: '''))
        while player2 != "r" and player2 != "p" and player2 != "s":
            print(f"{player2} is invalid.")
            player2 = str.lower(input('''Try typing "r" for rock, "p" for paper, and "s" for scissors: '''))
            
        player2_string = []
        if player2 == "r":
            player2_string.append("rock")
        if player2 == "p":
            player2_string.append("paper")
        if player2 == "s":
            player2_string.append("scissors")

        player1_string = []
        if player2 == "r":
            player1_string.append("paper")
        if player2 == "p":
            player1_string.append("scissors")
        if player2 == "s":
            player1_string.append("rock")
       
        print(f"{player1_name} chose {player1_string}, {player2_name} chose {player2_string}. {player1_name} Wins!")
# best of 3
def best_of_3():
   
    player1_score = int()
    player2_score = int() 
    
    
    #player 1 name
    player1_name = input("Player 1, enter your name: ")
    while player1_name == "":
            print("you must type in your name: ")
            player1_name = input("Player 1, enter your name: ")
    #player 2 name
    player2_name = input("player 2 enter your name: ")
    while player2_name == "":
            print("you must type in your name: ")
            player2_name = input("Player 2, enter your name: ")
    #game loop
    while player1_score < 2 and player2_score < 2:
        #player 1 guess
        player1  = str.lower(input('''Player 1, guess rock paper scissors. type "r" for rock, "p" for paper, and "s" for scissors: '''))
        while player1 != "r" and player1 != "p" and player1 != "s":
            print(f"{player1} is invalid")
            player1  = str.lower(input('''Try typeing "r" for rock, "p" for paper, and "s" for scissors: '''))
        player1_string = []
        if player1 == "r":
            player1_string.append("rock")
        if player1 == "p":
            player1_string.append("paper")
        if player1 == "s":
            player1_string.append("scissors")
        
        #player 2 guess
        player2  = str.lower(input('''Player 2, guess rock paper scissors. type "r" for rock, "p" for paper, and "s" for scissors: '''))
        while player2 != "r" and player2 != "p" and player2 != "s":
            print(f"{player2} is invalid")
            player2  = str.lower(input('''Try typeing "r" for rock, "p" for paper, and "s" for scissors: '''))
        player2_string = []
        if player2 == "r":
            player2_string.append("rock")
        if player2 == "p":
            player2_string.append("paper")
        if player2 == "s":
            player2_string.append("scissors")

        #draw
        if player1 == "r" and player2 == "r" or player1 == "p" and player2 == "p" or player1 == "s" and player2 == "s":
            print(f"{player1_name} chose {player1_string}, {player2_name} chose {player2_string}. Thats a draw")
        #player 1 win
        if player1 == "r" and player2 == "s" or player1 == "p" and player2 == "r" or player1 == "s" and player2 == "p":
            print(f"{player1_name} chose {player1_string}, {player2_name} chose {player2_string}. {player1_name} Wins!")
            player1_score = player1_score + 1
            
            print(f"{player1_name} {player1_score} | {player2_name} {player2_score}")
        #player 2 win
        if player1 == "r" and player2 == "p" or player1 == "p" and player2 == "s" or player1 == "s" and player2 == "r":
            print(f"{player1_name} chose {player1_string}, {player2_name} chose {player2_string}. {player2_name} Wins!")
            player2_score = player2_score + 1
            
            print(f"{player1_name} {player1_score} | {player2_name} {player2_score}")
    if player1_score > player2_score:
        print(f"{player1_name} Wins!")
    if player2_score > player1_score:
        print(f"{player2_name} Wins!")

#choosing single player or multiplayer 
single_or_multi = str.lower(input('''singleplayer or multiplayer? "s" for single, "m" for multiplayer, "3" for best of 3: '''))
while single_or_multi != "s" and single_or_multi != "m" and single_or_multi != "c" and single_or_multi != "3":
    print(f"{single_or_multi} is invalid")
    single_or_multi = str.lower(input('''try typing "s" for single, m for multiplayer: '''))

if single_or_multi == "s":
    print("singleplayer game")
    single_player()
    
if single_or_multi == "m":
    print("multiplayer game")
    multiplayer()

if single_or_multi == "c":
    print("multiplayer game")
    cheats()

if single_or_multi == "3":
    print("best of 3")
    best_of_3()
