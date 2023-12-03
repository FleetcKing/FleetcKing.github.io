#the game of pig is where the player rolls a die. whatever the player lands on gets added to their score but if the player hits 1 they loose it all. 
playername = input("enter your name: ")

choose_roll = input(f'''Hello {playername}! type "r" to roll the dice: ''')

import random
roll = random.randint(1,6)
player_score = 0
while roll > 1:
    player_score = player_score + roll
    print(f"{playername} rolled a {roll}. {playername}'s score is now {player_score}")
    choose_roll = input(f'''Hello {playername}! press enter to roll the dice, type "s" to stop: ''')
    if choose_roll == "s":
        break
    import random
    roll = random.randint(1,6)
    player_score = player_score + roll

if roll == 1:
    print(f"{playername} Looses.")
else:
    print(f"{playername}'s score is {player_score}")


