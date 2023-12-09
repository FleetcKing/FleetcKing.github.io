#Create a 5x5 grid, a, b, c, d, e by 1, 2, 3, 4, 5, 
#0 is white 1 is black 
#player inputs "start" to start the game 
#player can choose between infanate game mode or timed game mode or limited moves game mode. 
#start game
#import time and start timer 
#start tracking moves 
#if a1 = true end game and if a2 = true end game ect
#add together all squares and assign to a varyable. if variable == 25 end game and player wins. 
#if variable does not == 25 when the time is out or if variable does not == 25 and the player runs out of turns, player looses.
board = []
import random
 
for i in range(5):
    # build each row
    row = []
    for j in range(5):
        row.append(0)
    board.append(row)
 
print(board)
 
 
 
random_row = random.randint(0, 4)
random_col = random.randint(0, 4)
 
board[random_row][random_col] = 1
 
print(board)

