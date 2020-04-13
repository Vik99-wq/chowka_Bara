import numpy as np
import random


MAX_BLOCKS = 24
def p2():
    roll = roll_the_dice()
    move_pawn_to_next_pos(MAX_BLOCKS, p2_board, roll)
    print("\nP2 turn:", p2_count, "roll:", roll)
    print_matrix(p2_board)
    find_all_pawns_loctions(p2_board)
    return roll
def roll_the_dice():
    dice = [1, 1, 2, 2, 2, 3, 3, 4, 8]
    move = random.choice(dice)
    return move
def find_all_pawns_loctions(board):
    pawn_locations = np.where(board > 0)[0]
    print(pawn_locations)
    try:
        pawn1 = pawn_locations[0]
        pawn2 = pawn_locations[1]
        pawn3 = pawn_locations[2]
        pawn4 = pawn_locations[3]
    except(IndexError):
        print("Out of range\n")
def print_matrix(p1_board):
    print (p1_board[10], p1_board[9],p1_board[8],p1_board[7],p1_board[6])
    print (p1_board[11], p1_board[18],p1_board[19],p1_board[20],p1_board[5])
    print (p1_board[12], p1_board[17],p1_board[24],p1_board[21],p1_board[4])
    print (p1_board[13], p1_board[16],p1_board[23],p1_board[22],p1_board[3])
    print (p1_board[14], p1_board[15],p1_board[0],p1_board[1],p1_board[2])
    print("\n")

def move_pawn_to_next_pos(MAX_BLOCKS, p1_board, move):
    for i in range(MAX_BLOCKS, -1, -1):
        # Decide the next move
        if p1_board[i] > 0 and i < MAX_BLOCKS and i+move <= MAX_BLOCKS:
            # if move results in a single in the target or if position is safe or if the target is HOME
            if p1_board[i + move] == 0 or (i + move) % 4 == 0 or i + move == MAX_BLOCKS:
                p1_board[i] = p1_board[i] - 1
                p1_board[i + move] = p1_board[i + move] + 1
                return i

p1_board = np.array([4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
p2_board = np.array([4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
print_matrix(p1_board)
count = 1
p2_count = 1
# Each iteration is a turn ; Dont exceed 100 turns
while count < 100 and p1_board[MAX_BLOCKS] < 4:
    # Roll the dice
    move = roll_the_dice()
    print("\nturn:", count, "roll:", move)

    # Find farthest pawn to move
    ret = move_pawn_to_next_pos(MAX_BLOCKS, p1_board, move)
    print_matrix(p1_board)
    find_all_pawns_loctions(p1_board)
    p2_roll = p2()
    # Repeat turn
    if move == 4 or move == 8:
        move = roll_the_dice()
        print("\nturn:", count, "roll:", move)
        ret = move_pawn_to_next_pos(MAX_BLOCKS, p1_board, move)
        print_matrix(p1_board)
        find_all_pawns_loctions(p1_board)
    if p2_roll == 4 or p2_roll == 8:
        p2()
    # Increment number of attempts
    count = count + 1
    p2_count = p2_count + 1
