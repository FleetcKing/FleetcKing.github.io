player1_name = input("Player 1, enter your name: ")
while player1_name == "":
    print(f"{player1_name} is invalid")
    player1_name = input("Player 1, enter your name: ")

player2_name = input("player 2, enter your name: ")
while player2_name == "":
    print(f"{player1_name} is invalid")
    player2_name = input("Player 1, enter your name: ")

import random
choose_word_rand = random.randint(0,1)

if choose_word_rand == 0:
    word = input(f"{player1_name} choose a word. word is limited to 8 charictors. no numbers: ")
    player1 = 1 
    player2 = 0
    chooser = player1_name
    player = player2_name
elif choose_word_rand == 1:
    word = input(f"{player2_name} choose a word. word is limited to 8 charictors. no numbers: ")
    player1 = 0
    player2 = 1
    chooser = player2_name
    player = player1_name

spaces = word.find(" ")
alpha = word.isalpha()
lenth = len(word)

while spaces > 0 or not alpha or lenth > 8:
    spaces = word.find(" ")
    alpha = word.isalpha()
    lenth = len(word)
    if spaces > 0:
        print(f"{word} is invalid. One word no spaces.")
        word = input("Choose a word. Word is limited to 8 charictors. No numbers: ")
    elif not alpha:
        print(f"{word} is invalid. Cant include numbers.")
        word = input("Choose a word. Word is limited to 8 charictors. No numbers: ")
    elif lenth > 8: 
        print(f"{word} is invalid. limited to 8 charictors.")
        word = input("Choose a word. Word is limited to 8 charictors. No numbers: ")

guess_count = int()


#gameplay
#while guess count is less than 8 or players guess word is not == to the word or solve word is not == word. player keeps guessing
# if player1 guess = count

guess = ""
while word != guess and guess_count < 8:
    while_guess = input(f'''{chooser} chose a {lenth} letter word. {player}, choose a letter. or if you would like to solve type "solve" : ''')
    if len(word) == 8: 
        if while_guess == word[0] or while_guess == word[1] or while_guess == word[2] or while_guess == word[3] or while_guess == word[4] or while_guess == word [5] or while_guess == word[6] or while_guess == word[7]:
            guess = guess + while_guess
    elif len(word) == 7:
        if while_guess == word[0] or while_guess == word[1] or while_guess == word[2] or while_guess == word[3] or while_guess == word[4] or while_guess == word [5] or while_guess == word[6]:
            guess = guess + while_guess
    elif len(word) == 6: 
        if while_guess == word[0] or while_guess == word[1] or while_guess == word[2] or while_guess == word[3] or while_guess == word[4] or while_guess == word [5]:
            guess = guess + while_guess
    elif len(word) == 5:
        if while_guess == word[0] or while_guess == word[1] or while_guess == word[2] or while_guess == word[3] or while_guess == word[4]:
            guess = guess + while_guess
    elif len(word) == 4:
        if while_guess == word[0] or while_guess == word[1] or while_guess == word[2] or while_guess == word[3]:
            guess = guess + while_guess
    elif len(word) == 3:
        if while_guess == word[0] or while_guess == word[1] or while_guess == word[2]:
            guess = guess + while_guess
    else: 
        print(f"{while_guess} is not a letter.")
    guess_count = guess_count + 1 
    
    print(guess)
    print(word)
    print(guess_count)

if guess == word:
    print(f"{player} Wins!")
else:
    print(f"{chooser} wins!")

# print("you can only guess one letter at a time, otherwise solve.")
#         guess = input(f'''{chooser} chose a {lenth} letter word. {player} choose a letter. or if you would like to solve type "solve" : ''')
# print(f"you have found the letter {guess}!")
