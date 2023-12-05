#the game of pig is where the player rolls a die. whatever the player lands on gets added to their score but if the player hits 1 they loose it all. 
player1name = input("player 1, enter your name: ")
player2name = input("player 2, enter your name: ")

def game():
    print(f"{player1name} its your turn")
    choose_roll = input('''Press enter to roll the dice: ''')
    import random
    roll = random.randint(1,6)
    player_score = 0
    while roll > 1:
        player_score = player_score + roll
        print(f"{player1name} rolled a {roll}. {player1name}'s score is now {player_score}")
        choose_roll = input(f'''Hello {player1name}! press enter to roll the dice, type "s" to stop: ''')
        if choose_roll == "s":
            break
        import random
        roll = random.randint(1,6)
        player_score = player_score + roll
        if roll == 1:
            print(f"{player1name} rolled a {roll}, {player1name} Looses. {player2name} Wins!")
            break
        else:
            print(f"{player1name}'s score is {player_score}")

    if roll != 1:
        print(f"{player2name} its your turn")
        choose_roll = input('''Press enter to roll the dice: ''')
        import random
        roll2 = random.randint(1,6)
        player2_score = 0
        while roll2 > 1:
            player2_score = player2_score + roll2
            print(f"{player2name} rolled a {roll}. {player2name}'s score is now {player_score}")
            choose_roll = input(f'''Hello {player2name}! press enter to roll the dice, type "s" to stop: ''')
            if choose_roll == "s":
                break
            import random
            roll = random.randint(1,6)
            player_score = player_score + roll
            if roll == 1:
                print(f"{player2name} rolled a {roll}, {player2name} Looses. {player1name} Wins!")
                break
            else:
                print(f"{player2name}'s score is {player_score}")
    else:
        print(f"{player2name} rolled a {roll}, {player2name} Looses. {player1name} Wins!")
    
    if roll and roll2 != 1:
        if player_score > player2_score:
            print(f"{player1name} has {player_score} points, {player2name} has {player2_score} points. {player1name} Wins!")
        elif player_score < player2_score:
            print(f"{player2name} has {player2_score} points, {player1name} has {player_score} points. {player2name} Wins!")
        elif player_score == player2_score:
            print(f"{player1name} has {player_score} points, {player2name} has {player2_score} points. {player1name} and {player2name} Tie!")

game()








