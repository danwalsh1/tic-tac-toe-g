import tkinter as tk
import tkinter.font

######################
###### SETTINGS ######
# players/ai/network #
gamemode = "ai"      #
# simple/advanced    #
aiType = "simple"    #
# size of the board  #
boardSize = 3        #
######################

########################
### GLOBAL VARIABLES ###
########################

#>> Setup the initial labels for the board and number of turns taken
labels = [""] * boardSize**2
turn = 0

#################
### FUNCTIONS ###
#################

def playTurn(labels, pos, turn):
    if(turn%2 == 0):
        labels[pos] = "X"
    else:
        labels[pos] = "O"

    return labels

def checkHor(labels, size):
    #>> Check rows for wins

    #>> Check for X win
    win = True
    count = 0
    while(count < size):
        count2 = count*size
        while(count2 < (count+1)*size):
            if(labels[count2] != "X" and win == True):
                win = False
            count2 += 1

        if(win == True):
            return "X"
        else:
            win = True
        count += 1
    #>> Check for O win
    win = True
    count = 0
    while(count < size):
        count2 = count*size
        while(count2 < (count+1)*size):
            if(labels[count2] != "O" and win == True):
                win = False
            count2 += 1

        if(win == True):
            return "O"
        else:
            win = True
        count += 1
    #>> No win has been found
    return "-"

def checkVer(labels, size):
    #>> Check columns for wins

    #>> Check for X win
    win = True
    count = 0
    while(count < size):
        count2 = 0
        while(count2 < size):
            #print(str(count+count2*size) + ":" + str(count) + ":" + str(count2))
            if(labels[count+count2*size] != "X" and win == True):
                win = False
            count2 += 1
        if(win == True):
            return "X"
        else:
            win = True
        count += 1
    #>> Check for O win
    win = True
    count = 0
    while(count < size):
        count2 = 0
        while(count2 < size):
            if(labels[count+count2*size] != "O" and win == True):
                win = False
            count2 += 1
        if(win == True):
            return "O"
        else:
            win = True
        count += 1
    #>> No win has been found
    return "-"

def checkDia(labels, size):
    #>> Check diagonals for wins

    #>> Top left to bottom right
    #>> Check for X win
    win = True
    count = 0
    while(count < size):
        if(labels[count*size+count] != "X" and win == True):
            win = False
        count += 1
    if(win == True):
        return "X"
    #>> Check for O win
    win = True
    count = 0
    while(count < size):
        if(labels[count*size+count] != "O" and win == True):
            win = False
        count += 1
    if(win == True):
        return "O"
    #>> Top right to bottom left
    #>> Check for X win
    win = True
    count = 0
    while(count < size):
        if(labels[(size-1)*(count+1)] != "X" and win == True):
            win = False
        count += 1
    if(win == True):
        return "X"
    #>> Check for O win
    win = True
    count = 0
    while(count < size):
        if(labels[(size-1)*(count+1)] != "O" and win == True):
            win = False
        count += 1
    if(win == True):
        return "O"
    
    
    return "-"

def checkEnd(labels, size):
    ''' This function is used to check if the game has ended in a draw '''
    count = 0
    while(count < size**2):
        if(labels[count] != "X" and labels[count] != "O"):
            return "-"
        count += 1
    return "DRAW"

def checkWin():
    ''' The function uses other function to check for either player win along all options '''
    global labels
    global boardSize
    check = False
    check = checkHor(labels, boardSize)
    if(check == "X" or check == "O"):
        return check
    check = checkVer(labels, boardSize)
    if(check == "X" or check == "O"):
        return check
    check = checkDia(labels, boardSize)

    check2 = checkEnd(labels, boardSize)
    if(check2 == "DRAW"):
        return check2
    return check

def btnPress(btnNum):
    check = checkWin()
    if(check == "-"):
        #>> Move turn onto next player
        print("No win found!")
    elif(check == "X"):
        print("Player 1 has won!")
    elif(check == "O"):
        print("Player 2 has won!")
    elif(check == "DRAW"):
        print("Game has ended in a draw!")
    else:
        print("ERROR: playerThread >> checkWin() returned:: " + str(check))
    return

########################
### BUTTON FUNCTIONS ###
########################

def btnOneF():
    btnPress(1)
    lblInfo.config(text = "yay")
    return

def btnTwoF():
    btnPress(2)
    return

def btnThreeF():
    btnPress(3)
    return

def btnFourF():
    btnPress(4)
    return

def btnFiveF():
    btnPress(5)
    return

def btnSixF():
    btnPress(6)
    return

def btnSevenF():
    btnPress(7)
    return

def btnEightF():
    btnPress(8)
    return

def btnNineF():
    btnPress(9)
    return

############
### GAME ###
############

###########
### GUI ###
###########

root = tk.Tk()

btnHeight = 2
btnWidth = 5
btnFont = tk.font.Font(size = 40)
initialText = ""
systemColour = "light grey"

root.configure(background = systemColour)

root.geometry("500x500+400+300")
root.title("Tic-Tac-Toe")

btnOne = tk.Button(root, text = initialText, fg = "black", bg = "white", height = btnHeight, width = btnWidth, font = btnFont, command = btnOneF).grid(row = 0, column = 0)
btnTwo = tk.Button(root, text = initialText, fg = "black", bg = "white", height = btnHeight, width = btnWidth, font = btnFont, command = btnTwoF).grid(row = 0, column = 1)
btnThree = tk.Button(root, text = initialText, fg = "black", bg = "white", height = btnHeight, width = btnWidth, font = btnFont, command = btnThreeF).grid(row = 0, column = 2)
btnFour = tk.Button(root, text = initialText, fg = "black", bg = "white", height = btnHeight, width = btnWidth, font = btnFont, command = btnFourF).grid(row = 1, column = 0)
btnFive = tk.Button(root, text = initialText, fg = "black", bg = "white", height = btnHeight, width = btnWidth, font = btnFont, command = btnFiveF).grid(row = 1, column = 1)
btnSix = tk.Button(root, text = initialText, fg = "black", bg = "white", height = btnHeight, width = btnWidth, font = btnFont, command = btnSixF).grid(row = 1, column = 2)
btnSeven = tk.Button(root, text = initialText, fg = "black", bg = "white", height = btnHeight, width = btnWidth, font = btnFont, command = btnSevenF).grid(row = 2, column = 0)
btnEight = tk.Button(root, text = initialText, fg = "black", bg = "white", height = btnHeight, width = btnWidth, font = btnFont, command = btnEightF).grid(row = 2, column = 1)
btnNine = tk.Button(root, text = initialText, fg = "black", bg = "white", height = btnHeight, width = btnWidth, font = btnFont, command = btnNineF).grid(row = 2, column = 2)

lblInfo = tk.Label(root, text="Your turn!", font=("Helvetica", 13), bg = systemColour)
lblInfo.grid(row = 3, column = 1)

root.mainloop()

while(True):
    x = input("Press enter to exit!")
    break
