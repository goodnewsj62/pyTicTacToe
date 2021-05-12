# my approach to making tic tac toe

import random
import time


directions = {"up-left":" ", "up-center":" ","up-right":" ","mid-left":" ","mid-center":" ","mid-right":" ",\
    "down-left":" ","down-center":" ","down-right":" "}

player = ['X', 'O']

def reset():
    for k,v in  directions.items():
        directions[k] = " "

def choose_player(player):
    while True:
        choice = input("choose your player [X or O]: ")
        if choice.lower() == 'x' or choice.lower() == 'o':
            return player.index(choice.upper())

def print_winner(func,directions,computer):
    win_condition,winner = func(directions)
    if win_condition:
        if winner == computer:
            print("Computer wins!")
            return True
        else:
            print("Yay! you won!")
            return True
    return False
        


def check_matched(key_dict):
    k = [val for val in key_dict.values()]
    if k[0] == k[1] == k[2] != " " or k[0] == k[3] == k[6] != " " or k[0] == k[4] == k[8] != " ":
        return True , k[0]
    elif k[3] == k[4] == k[5] != " " or k[1] == k[4] == k[7]!= " "  or k[2] == k[4] == k[6] != " ":
        return True ,k[4]
    elif k[6] == k[7] == k[8] != " ":
        return True, k[8]
    return False, None

def your_move(func,key_dict):
    while True:
        move = input("Your turn: ")
        if move not in key_dict:
            print("Enter valid cell name")
        elif func(directions,move):
            print("cell already has a value")
        else:
            return move

def cell_state(key_dict,key):
    if key_dict[key] == " ":
        return False
    return True


    
def display_result(key_dict):
    k =  [val for val in key_dict.values()]
    print(f""" 
                {k[0]} | {k[1]}  | {k[2]}
                -----------
                {k[3]} | {k[4]}  | {k[5]}
                -----------
                {k[6]} | {k[7]}  | {k[8]}
            """)

def wellcome():
    print(" Py Tic Tac Toe ".center(70,'*'))
    print("\nlets play:_ \n")
    print("""
            Enter any of this keyword for cell input

            up-left  | up-center  | up-right
            --------------------------------
            mid-left | mid-center | mid-right
            --------------------------------
            down-left| down-center| down-right
    """)

def comp_move(directions,keys):
    while True:
            k = random.randint(0, 8)
            if not cell_state(directions, keys[k]):
                return keys[k]

def all_cells_filled(key_dict):
    if any(val == " " for val in key_dict.values()):
        return False
    return True


def play_game():
    keys =  [key for key in directions.keys()]
    player_ = ""
    computer = ""


    wellcome()
    while True:

        res = input("To play (enter y or yes) to break enter any other alphabet: ")
        if not (res.lower() == 'y' or  res.lower() == 'yes'):
            break
        reset()
        
        choice = choose_player(player)
        if choice == 0:
            player_ = player[0]
            computer = player[1] 
        else:
            player_ = player[1]
            computer = player[0]

        while True:
            
            move = your_move(cell_state, directions)        
            directions[move] = player_


            if print_winner(check_matched,directions, computer):
                display_result(directions)
                break
            if all_cells_filled(directions):
                print("We got a tie!")
                break

            display_result(directions)

            directions[comp_move(directions,keys)] = computer

            time.sleep(1)

            display_result(directions)

            if print_winner(check_matched,directions, computer):
                display_result(directions)
                break
            if all_cells_filled(directions):
                print("We got a tie!")
                break


play_game()
        

        