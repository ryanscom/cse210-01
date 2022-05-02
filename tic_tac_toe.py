import tkinter as tk
from tkinter import*


"""
cse210: Tic Tac Toe assignment 
Author: Ryan Manthey

"""


def main():
    
        playgame = True
   
        while playgame == True: # Main game loop
            
            # messages list
            messages = ["Player X starts!"]

            n_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] # List for the board
            root = Tk()

            frm_main = tk.Frame(root)
            frm_main.master.title("TIC TAC TOE")

            # Make the main parent frames
            frm_1 = LabelFrame(root, width = 600, height = 50, bd = 2, relief ="groove", bg = "lavenderblush3") # Message frame
            frm_1.pack(side = TOP, fill = BOTH)
            frm_2 = LabelFrame(root, width = 600, height = 50, bd = 2, relief ="groove", bg = "lavenderblush3") # Message frame
            frm_2.pack(side = TOP, fill = BOTH)
            frm_3 = Frame(root, width = 600, height = 200, relief = "groove", bg = "lavenderblush3")
            frm_3.pack(side = TOP, fill = BOTH)

            # text displays
            title_display = tk.Label(frm_1, font = ("arial", 16, "bold"), bg = "lavenderblush3", text = "Let's play TIC TAC TOE!") # Message Label
            title_display.place(anchor = CENTER, relx=0.5, rely=0.5) # Used .place(anchor) instead of .pack to center the message.
            message_display = tk.Label(frm_2, text = messages[0], font = ("arial", 16, "bold"), bg = "lavenderblush3", fg = "maroon") 
            message_display.place(anchor = CENTER, relx=0.5, rely=0.5) # Used .place(anchor) instead of .pack to center the message.
            
            # List to hold the references to the buttons created below
            buttons = []

            # player list
            players = ["X"]

            # Grid variables
            Row = 2
            column = 0

            for index in range(9):
        
                # Get the current letter from the letters list
                boardbuttons = n_list[index]
              
                # Make the button
                button = Button(frm_3, text = boardbuttons, width = 9, height = 3, font = ("arial", 30, "bold"), command = lambda index = index, buttons = buttons, boardbuttons = boardbuttons, players = players, n_list = n_list, messages = messages, message_display = message_display, frm_2 = frm_2: click(index, buttons, boardbuttons, players, n_list, messages, message_display, frm_2), bg = "light grey", fg = "maroon",padx = 3,pady = 3, bd = 5)

                # Add button to the frame
                button.grid(row = Row, column = column )

                # Add a reference to the button to 'buttons'
                buttons.append(button) 

                column += 1

                if column > 2 and Row == 2:
                    column = 0
                    Row += 1
                if column > 2 and Row == 3:
                    column = 0
                    Row += 1

            running = input("Running... ")
           
            # playgame = False

def click(index, buttons, boardbuttons, players, n_list, messages, message_display, frm_2):

    # Disable the button by index and change number to player X or 0
    buttons[index].config(state = "disabled", text = players[0], fg = "white", bg = "maroon" )
    # buttons[index].config(text = n_list[boardbuttons -1], fg = "white", bg = "maroon" )

    # Switch number list index with player X or O
    n_list[boardbuttons - 1] = players[0]
    
    # Switch player and message for frm_2
    switchplayer(players, messages)
    message_display.config(text = messages[0], fg = "maroon")

    # Check if player won
    win_or_draw = win_conditions(n_list)

    #Screen for X, O, or draw
    if win_or_draw == "X" or win_or_draw == "O" or win_or_draw == "draw":
        for button in range(9):
            if n_list[index] == "X": 
                buttons[button].config(state = "disabled", bg = "grey", fg = "white")

        win_print(win_or_draw, messages)
        message_display.config(text = messages[0], fg = "white", bg = "maroon")
        frm_2.config(bg = "maroon")



def switchplayer(players, messages):
    if players[0] == "X":
        players[0] = "O"
        messages[0] = "It's player O's turn to pick a square!"
        
    elif players[0] == "O":
        players[0] = "X"
        messages[0] = "It's player X's turn to pick a square!"

def win_print(win, messages): # Prints who won the game or if it was a draw       
    if win == "X":
        messages[0] = "Player X won!"

    elif win == "O":
        messages[0] = "Player O won!"
        
    elif win == "draw":
        messages[0] = "It's a draw!"
        
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