"""
cse210: Tic Tac Toe assignment 
Author: Ryan Manthey


"""

def main():

    playgame = True

    while playgame == True:
        win = "play"
        choice_x = False
        choice_o = False

        n_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        print()
        print("Let's play Tic Tac Toe! ")

        print_board(n_list)

        while win != "X" or win != "O":
        
            while choice_x == False:
                x_pick = input("(Pick a number between 1 and 9) X's turn to pick a square: ")
                x_pick = int(x_pick)
                x_pick = x_pick -1

                if n_list[x_pick] == "O":
                    print("Sorry player O already chose that square. ")
                if n_list[x_pick] == "X":
                    print("Sorry player X already chose that square. ")

                if n_list[x_pick] != "O":
                    if n_list[x_pick] != "X":
                        n_list[x_pick] = "X"
                        choice_x = True 
                        choice_o = False   
                
                
            print_board(n_list) 

            winner = win_conditions(n_list)
            
            if winner == "X" or winner == "O" or winner == "draw":
                if winner == "X":
                    win = "X"
                if winner == "O":
                    win = "O"
                if winner == "draw":
                    win = "draw"

                win_print(win) 
                yes_no = play_again()
                
                if yes_no == "y":
                    break
                
                if yes_no == "n":
                    playgame = False
                    break

            while choice_o == False:
                o_pick = input("(Pick a number between 1 and 9) O's turn to pick a square: ")
                o_pick = int(o_pick)
                o_pick = o_pick -1

                if n_list[o_pick] == "X":
                    print("Sorry player X already chose that square. ")
                elif n_list[o_pick] == "O":
                    print("Sorry player O already chose that square. ")

                if n_list[o_pick] != "X":
                    if n_list[o_pick] != "O":
                        n_list[o_pick] = "O"
                        choice_o = True
                        choice_x = False
                        
            print_board(n_list)

            winner = win_conditions(n_list)

            if winner == "X" or winner == "O" or winner == "draw":
                if winner == "X":
                    win = "X"
                if winner == "O":
                    win = "O"
                if winner == "draw":
                    win == "draw"

                win_print(win)  
                yes_no = play_again()
                
                if yes_no == "y":
                    break

                if yes_no == "n":
                    playgame = False
                    break

def win_print(win):       
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
   
def print_board(n_list):
    print(f"""
{n_list[0]}|{n_list[1]}|{n_list[2]}
-+-+-
{n_list[3]}|{n_list[4]}|{n_list[5]}
-+-+-
{n_list[6]}|{n_list[7]}|{n_list[8]}
""")

def win_conditions(n_list):
    if (n_list[0] == "X" and n_list[1] == "X" and n_list[2] == "X") or (n_list[3] == "X" and n_list[4] == "X" and n_list[5] == "X") or (n_list[6] == "X" and n_list[7] == "X" and n_list[8] == "X") or (n_list[0] == "X" and n_list[4] == "X" and n_list[8] == "X") or (n_list[2] == "X" and n_list[4] == "X" and n_list[6] == "X") or (n_list[0] == "X" and n_list[3] == "X" and n_list[6] == "X") or (n_list[1] == "X" and n_list[4] == "X" and n_list[7] == "X") or (n_list[2] == "X" and n_list[5] == "X" and n_list[8] == "X"):

        winner = "X"
        return winner

    if (n_list[0] == "O" and n_list[1] == "O" and n_list[2] == "O") or (n_list[3] == "O" and n_list[4] == "O" and n_list[5] == "O") or (n_list[6] == "O" and n_list[7] == "O" and n_list[8] == "O") or (n_list[0] == "O" and n_list[4] == "O" and n_list[8] == "O") or (n_list[2] == "O" and n_list[4] == "O" and n_list[6] == "O") or (n_list[0] == "O" and n_list[3] == "O" and n_list[6] == "O") or (n_list[1] == "O" and n_list[4] == "O" and n_list[7] == "O") or (n_list[2] == "O" and n_list[5] == "O" and n_list[8] == "O"):
        
        winner = "O"
        return winner

    if (n_list[0] == "X" or n_list[0] == "O") and (n_list[1] == "X" or n_list[1] == "O") and (n_list[2] == "X" or n_list[2] == "O") and (n_list[3] == "X" or n_list[3] == "O") and (n_list[4] == "X" or n_list[4] == "O") and (n_list[5] == "X" or n_list[5] == "O") and (n_list[6] == "X" or n_list[6] == "O") and (n_list[7] == "X" or n_list[7] == "O") and (n_list[8] == "X" or n_list[8] == "O"):

        winner = "draw"
        return winner

def play_again():

    answer = input("Do you want to play again? (Y/N): ")
    return answer

if __name__ == "__main__":
    main()