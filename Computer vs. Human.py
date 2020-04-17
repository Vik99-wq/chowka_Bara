import numpy as np
import random
MAX_BLOCKS = 24


def human_move(p2_roll):
    ret_code = 0

    if p2_count == 1:
        which_pawn_to_move = input("Would you like to move the pawn closest to home(type 1)\n"
                                    "Second closest(type 2)\n"
                                    "Second farthest(type three)\n"
                                    "Farthest(type 4)\n"
                                    "Type Here: ")
    else:
        which_pawn_to_move = input("Which pawn would you like to move?\n")
    if which_pawn_to_move == "1":
        ret_code = move_human_pawn(pawn1, p2_roll, p2_board)
    elif which_pawn_to_move == "2":
        ret_code = move_human_pawn(pawn2, p2_roll, p2_board)
    elif which_pawn_to_move == "3":
        ret_code = move_human_pawn(pawn3, p2_roll, p2_board)
    elif which_pawn_to_move == "4":
        ret_code = move_human_pawn(pawn4, p2_roll, p2_board)
    else:
        print("Type a number between 1-4")
    return ret_code


def p2():
    roll = roll_the_dice()
    #move_pawn_to_next_pos(MAX_BLOCKS, p2_board, roll)
    print("\nP2 turn:", p2_count, "P2 roll:", roll)
    ret_code = 1
    while ret_code == 1:
        find_all_pawns_loctions(p2_board)
        ret_code = human_move(roll)

    print_matrix2(p1_board,p2_board)
    return roll


def roll_the_dice():
    dice = [1, 1, 2, 2, 2, 3, 3, 4, 8]
    move = random.choice(dice)
    return move


def find_all_pawns_loctions(board):
    pawn_locations = np.where(board > 0)[0]
    global pawn1
    global pawn2
    global pawn3
    global pawn4
    pawn1 = pawn_locations[0]
    try:
        pawn2 = pawn_locations[1]
    except IndexError:
        print("")
    try:
        pawn3 = pawn_locations[2]
    except IndexError:
        print("")
    try:
        pawn4 = pawn_locations[3]
    except IndexError:
        print("")


def print_matrix(board):
    print(board[10], board[9] , board[8], board[7], board[6])
    print(board[11], board[18], board[19], board[20], board[5])
    print(board[12], board[17], board[24], board[21], board[4])
    print(board[13], board[16], board[23], board[22], board[3])
    print(board[14], board[15], board[0], board[1], board[2])
    print("\n")


def print_matrix2(board1, board2):
    str_matrix = ""
    print (" P1 Matrix \t\t P2 Matrix")
    str_matrix = str_matrix + " " + str(board1[10]) + " " + str(board1[9]) + " " + str(board1[8]) + " " + str(
        board1[7]) + " " + str(board1[6]) + '\t\t' + " " + str(board2[10]) + " " + str(board2[9]) + " " +  str(board2[8]) + " " + str(board2[7]) + " " + str(board2[6]) + "\n"
    str_matrix = str_matrix + " " + str(board1[11]) + " " + str(board1[18]) + " " + str(board1[19]) + " " + str(
        board1[20]) + " " + str(board1[5]) + "\t\t" + " " + str(board2[11]) + " " + str(board2[
                                                                                            18]) + " " + str(
        board2[19]) + " " + str(board2[20]) + " " + str(board2[5]) + "\n"
    str_matrix = str_matrix + " " + str(board1[12]) + " " + str(board1[17]) + " " + str(board1[24]) + " " + str(
        board1[21]) + " " + str(board1[4]) + "\t\t" + " " + str(board2[12]) + " " + str(board2[
                                                                                            17]) + " " + str(
        board2[24]) + " " + str(board2[21]) + " " + str(board2[4]) + "\n"
    str_matrix = str_matrix + " " + str(board1[13]) + " " + str(board1[16]) + " " + str(board1[23]) + " " + str(
        board1[22]) + " " + str(board1[3]) + "\t\t" + " " + str(board2[13]) + " " + str(board2[
                                                                                            16]) + " " + str(
        board2[23]) + " " + str(board2[22]) + " " + str(board2[3]) + "\n"
    str_matrix = str_matrix + " " + str(board1[14]) + " " + str(board1[15]) + " " + str(board1[0]) + " " + str(
        board1[1]) + " " + str(board1[2]) + "\t\t" + " " + str(board2[14]) + " " + str(board2[
                                                                                           15]) + " " + str(
        board2[0]) + " " + str(board2[1]) + " " + str(board2[2]) + "\n"
    print (str_matrix)


def move_human_pawn(pawn, roll, p2_board):
    ret_code = 0
    if pawn < MAX_BLOCKS and pawn + roll <= MAX_BLOCKS:
        if p2_board[pawn + roll] > 0 and (pawn + roll) % 4 != 0:
            print("Invalid roll!!! Pick again")
            ret_code = 1
        elif p2_board[pawn + roll] == 0 or (pawn + roll) % 4 == 0:
            p2_board[pawn + roll] = p2_board[pawn + roll] + 1
            p2_board[pawn] = p2_board[pawn] - 1
    return ret_code


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
print_matrix2(p1_board, p2_board)
#print_matrix(p1_board)
count = 1
p2_count = 1
# Each iteration is a turn ; Dont exceed 100 turns
while count < 100 and p1_board[MAX_BLOCKS] < 4:
    # Roll the dice
    move = roll_the_dice()
    print("\nP1 turn:", count, "P1 roll:", move)
    # Find farthest pawn to move
    ret = move_pawn_to_next_pos(MAX_BLOCKS, p1_board, move)
    print_matrix2(p1_board,p2_board)
    find_all_pawns_loctions(p1_board)
    p2_roll = p2()
    # Repeat turn
    if move == 4 or move == 8:
        move = roll_the_dice()
        print("\nP1 turn:", count, "P1 roll:", move)
        print("\nP2 turn:", p2_count, "P2 roll:", p2_roll)
        ret = move_pawn_to_next_pos(MAX_BLOCKS, p1_board, move)
        print_matrix2(p1_board, p2_board)
        find_all_pawns_loctions(p1_board)
    if p2_roll == 4 or p2_roll == 8:
        p2()
    # Increment number of attempts
    count = count + 1
    p2_count = p2_count + 1
