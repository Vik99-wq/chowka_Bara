import numpy as np
import  random

def roll_the_dice():
    dice = [1, 1, 2, 2, 2, 3, 3, 4, 8]
    move = random.choice(dice)
    print("move:", move)
    return move


def move_pawn_to_next_pos():
    for i in range(15, -1, -1):
        # Decide the next move
        if p1_board[i] > 0 and i < 15 and i+move <= 15:
            if p1_board[i+move] > 0:
                break
            p1_board[i] = p1_board[i] -1
            p1_board[i+move] = p1_board[i+move] + 1
            break

"""p1_board = np.array([[0,0,4,0,0], [0,0,0,0,0],[0,0,0,0,0], [0,0,0,0,0],[0,0,0,0,0]])
print(p1_board)
p2_board = np.array([[0,0,0,0,0], [0,0,0,0,0],[0,0,0,0,0], [0,0,0,0,0],[0,0,4,0,0]])
print(p2_board)
dice = [1,1,2,2,2,3,3,4,8]


def p1_roll():
    p1_roll = random.choice(dice)
    print(p1_roll)

def p2_roll():
    p2_roll = random.choice(dice)


while True:
    p1_roll()
"""
p1_board = np.array([4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

'''for i in range(16, 0, -1):
    p1_board[0] = p1_board[0] - 1
    if p1_board[0]<0:
        exit()
    dice = [1,1,2,2,2,3,3,4,8]
    move = 0
    move = move + random.choice(dice)
    p1_board[move] = 1
    print(p1_board)'''

print(p1_board)

count = 0
# Each iteration is a turn ; Dont exceed 100 turns
while count < 100 and p1_board[15] < 4:
    # Roll the dice
    move = roll_the_dice()

    # Find farthest pawn to move
    move_pawn_to_next_pos()

    # Increment number of attempts
    count = count + 1

    # Print current state of the board
    print(p1_board)
