"""
cse210: Tic Tac Toe assignment 
Author: Ryan Manthey

"""
def main():

    playgame = True

    while playgame == True: # Main game loop
        win = "play"
        choice_x = False
        choice_o = False

        n_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] # List for the board

        print()
        print("Let's play Tic Tac Toe! ") # Welcome statement

        print_board(n_list) 

        while win != "X" or win != "O": # Screen board for X and O
        
            while choice_x == False: # Loop for player X
                x_pick = input("(Pick a number between 1 and 9) X's turn to pick a square: ")
                x_pick = int(x_pick)
                x_pick = x_pick -1

                used_space_message(n_list, x_pick)

                if n_list[x_pick] != "O":
                    if n_list[x_pick] != "X":
                        n_list[x_pick] = "X"
                        choice_x = True 
                        choice_o = False   
                           
            print_board(n_list) 
            winner = win_conditions(n_list)
            
            if winner == "X" or winner == "O" or winner == "draw":

                win_print(winner) 
                yes_no = play_again()
                
                if yes_no == "y":
                    break
                
                if yes_no == "n":
                    playgame = False
                    break

            while choice_o == False: # Loop for player O
                o_pick = input("(Pick a number between 1 and 9) O's turn to pick a square: ")
                o_pick = int(o_pick)
                o_pick = o_pick -1

                used_space_message(n_list, o_pick)
                
                if n_list[o_pick] != "X":
                    if n_list[o_pick] != "O":
                        n_list[o_pick] = "O"
                        choice_o = True
                        choice_x = False
                        
            print_board(n_list)
            winner = win_conditions(n_list)

            if winner == "X" or winner == "O" or winner == "draw":
             
                win_print(winner)  
                yes_no = play_again()
                
                if yes_no == "y":
                    break

                if yes_no == "n":
                    playgame = False
                    break

def used_space_message(n_list, pick): # Prints messages when a space has already been used
    if n_list[pick] == "X":
        print("Sorry player X already chose that square. ")
    elif n_list[pick] == "O":
        print("Sorry player O already chose that square. ")

def win_print(win): # Prints who won the game or if it was a draw       
    if win == "X":
        print()
        print("Player X won!")
        print()

    elif win == "O":
        print()
        print("player O won!")
        print()

    elif win == "draw":
        print()
        print("It's a draw!")
        print()
   
def print_board(n_list): # prints the game board that references the indexes from n_list
    print(f"""
{n_list[0]}|{n_list[1]}|{n_list[2]}
-+-+-
{n_list[3]}|{n_list[4]}|{n_list[5]}
-+-+-
{n_list[6]}|{n_list[7]}|{n_list[8]}
""")

def win_conditions(n_list): # list of win conditions for player X, O, as well as draw conditions
    if (n_list[0] == "X" and n_list[1] == "X" and n_list[2] == "X") or (n_list[3] == "X" and n_list[4] == "X" and n_list[5] == "X") or (n_list[6] == "X" and n_list[7] == "X" and n_list[8] == "X") or (n_list[0] == "X" and n_list[4] == "X" and n_list[8] == "X") or (n_list[2] == "X" and n_list[4] == "X" and n_list[6] == "X") or (n_list[0] == "X" and n_list[3] == "X" and n_list[6] == "X") or (n_list[1] == "X" and n_list[4] == "X" and n_list[7] == "X") or (n_list[2] == "X" and n_list[5] == "X" and n_list[8] == "X"):

        winner = "X"
        return winner

    if (n_list[0] == "O" and n_list[1] == "O" and n_list[2] == "O") or (n_list[3] == "O" and n_list[4] == "O" and n_list[5] == "O") or (n_list[6] == "O" and n_list[7] == "O" and n_list[8] == "O") or (n_list[0] == "O" and n_list[4] == "O" and n_list[8] == "O") or (n_list[2] == "O" and n_list[4] == "O" and n_list[6] == "O") or (n_list[0] == "O" and n_list[3] == "O" and n_list[6] == "O") or (n_list[1] == "O" and n_list[4] == "O" and n_list[7] == "O") or (n_list[2] == "O" and n_list[5] == "O" and n_list[8] == "O"):
        
        winner = "O"
        return winner

    if (n_list[0] == "X" or n_list[0] == "O") and (n_list[1] == "X" or n_list[1] == "O") and (n_list[2] == "X" or n_list[2] == "O") and (n_list[3] == "X" or n_list[3] == "O") and (n_list[4] == "X" or n_list[4] == "O") and (n_list[5] == "X" or n_list[5] == "O") and (n_list[6] == "X" or n_list[6] == "O") and (n_list[7] == "X" or n_list[7] == "O") and (n_list[8] == "X" or n_list[8] == "O"):

        winner = "draw"
        return winner

def play_again(): # play again message with input
    answer = input("Do you want to play again? (Y/N): ")
    return answer

if __name__ == "__main__":
    main()