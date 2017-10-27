import tkinter as tk
import tkinter.font
import socket as s
import threading as t
import pickle as p

############################
######### SETTINGS #########
# size of the board        #
boardSize = 3              #
#>> Host's IP Address      #
hostIP = '127.0.0.1'       #
#>> Port to use for socket #
port = 12345               #
############################

########################
### GLOBAL VARIABLES ###
########################

#>> Setup the initial labels for the board and number of turns taken
labels = [""] * boardSize**2
gameFinished = False
sock = s.socket(s.AF_INET, s.SOCK_STREAM)
playerNum = "0"

#################
### FUNCTIONS ###
#################

def getBoardFromList(gameList, boardSize = 3):
    ''' This function is used to return a list with the game board elements only '''
    labels = [''] * (boardSize**2)
    for i in range(0, boardSize**2):
        labels[i] = gameList[i]

    return labels

def updateButtons():
    btnOne.config(text = labels[0])
    btnTwo.config(text = labels[1])
    btnThree.config(text = labels[2])
    btnFour.config(text = labels[3])
    btnFive.config(text = labels[4])
    btnSix.config(text = labels[5])
    btnSeven.config(text = labels[6])
    btnEight.config(text = labels[7])
    btnNine.config(text = labels[8])

def recvFromServer():
    global labels
    global gameFinished
    
    while(True):
        pData = sock.recv(1024)
        if not pData:
            break
        data = p.loads(pData)
        boardLabels = getBoardFromList(data)
        if(boardLabels != labels):
            labels = boardLabels
            updateButtons()

        if(data[10] == "win"):
            if(data[11] == "x"):
                if(playerNum == "1"):
                    lblInfo.config(text = "You have won!")
                else:
                    lblInfo.config(text = "Player 1 has won!")
                gameFinished = True
            elif(data[11] == "o"):
                if(playerNum == "2"):
                    lblInfo.config(text = "You have won!")
                else:
                    lblInfo.config(text = "Player 2 has won!")
            elif(data[11] == "DRAW"):
                lblInfo.config(text = "Draw!")
            else:
                print("ERROR:: Winner not recognised!")
            gameFinished = True
            break
        elif(data[10] == "playerNum"):
            playerNum = data[11]
            lblPlayerNum.config(text = "Player " + playerNum)
                

def btnPress(btnNum):
    global labels
    global gameFinished

    if(gameFinished == False):
        message = str(btnNum-1)
        sock.send(message.encode())

    return

########################
### BUTTON FUNCTIONS ###
########################

def btnOneF():
    btnPress(1)
    btnOne.config(text = labels[0])
    return

def btnTwoF():
    btnPress(2)
    btnTwo.config(text = labels[1])
    return

def btnThreeF():
    btnPress(3)
    btnThree.config(text = labels[2])
    return

def btnFourF():
    btnPress(4)
    btnFour.config(text = labels[3])
    return

def btnFiveF():
    btnPress(5)
    btnFive.config(text = labels[4])
    return

def btnSixF():
    btnPress(6)
    btnSix.config(text = labels[5])
    return

def btnSevenF():
    btnPress(7)
    btnSeven.config(text = labels[6])
    return

def btnEightF():
    btnPress(8)
    btnEight.config(text = labels[7])
    return

def btnNineF():
    btnPress(9)
    btnNine.config(text = labels[8])
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
root.resizable(0,0)

root.title("Tic-Tac-Toe")

btnOne = tk.Button(root, text = initialText, fg = "black", bg = "white", height = btnHeight, width = btnWidth, font = btnFont, command = btnOneF)
btnOne.grid(row = 0, column = 0)
btnTwo = tk.Button(root, text = initialText, fg = "black", bg = "white", height = btnHeight, width = btnWidth, font = btnFont, command = btnTwoF)
btnTwo.grid(row = 0, column = 1)
btnThree = tk.Button(root, text = initialText, fg = "black", bg = "white", height = btnHeight, width = btnWidth, font = btnFont, command = btnThreeF)
btnThree.grid(row = 0, column = 2)
btnFour = tk.Button(root, text = initialText, fg = "black", bg = "white", height = btnHeight, width = btnWidth, font = btnFont, command = btnFourF)
btnFour.grid(row = 1, column = 0)
btnFive = tk.Button(root, text = initialText, fg = "black", bg = "white", height = btnHeight, width = btnWidth, font = btnFont, command = btnFiveF)
btnFive.grid(row = 1, column = 1)
btnSix = tk.Button(root, text = initialText, fg = "black", bg = "white", height = btnHeight, width = btnWidth, font = btnFont, command = btnSixF)
btnSix.grid(row = 1, column = 2)
btnSeven = tk.Button(root, text = initialText, fg = "black", bg = "white", height = btnHeight, width = btnWidth, font = btnFont, command = btnSevenF)
btnSeven.grid(row = 2, column = 0)
btnEight = tk.Button(root, text = initialText, fg = "black", bg = "white", height = btnHeight, width = btnWidth, font = btnFont, command = btnEightF)
btnEight.grid(row = 2, column = 1)
btnNine = tk.Button(root, text = initialText, fg = "black", bg = "white", height = btnHeight, width = btnWidth, font = btnFont, command = btnNineF)
btnNine.grid(row = 2, column = 2)

lblPlayerNum = tk.Label(root, text="", font=("Helvetica", 13), bg = systemColour)
lblPlayerNum.grid(row = 3, column = 0)
lblInfo = tk.Label(root, text="Your turn!", font=("Helvetica", 13), bg = systemColour)
lblInfo.grid(row = 3, column = 1)

#root.mainloop()

sock.connect((hostIP, port))

iThread = t.Thread(target=recvFromServer)
iThread.daemon = True
iThread.start()

root.mainloop()

while(True):
    x = input("Press enter to exit!")
    break
