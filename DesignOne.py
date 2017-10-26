import tkinter as tk
import tkinter.font

#################
### FUNCTIONS ###
#################

########################
### GLOBAL VARIABLES ###
########################

########################
### BUTTON FUNCTIONS ###
########################

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

btnOne = tk.Button(root, text = initialText, fg = "black", bg = "white", height = btnHeight, width = btnWidth, font = btnFont).grid(row = 0, column = 0)
btnTwo = tk.Button(root, text = initialText, fg = "black", bg = "white", height = btnHeight, width = btnWidth, font = btnFont).grid(row = 0, column = 1)
btnThree = tk.Button(root, text = initialText, fg = "black", bg = "white", height = btnHeight, width = btnWidth, font = btnFont).grid(row = 0, column = 2)
btnFour = tk.Button(root, text = initialText, fg = "black", bg = "white", height = btnHeight, width = btnWidth, font = btnFont).grid(row = 1, column = 0)
btnFive = tk.Button(root, text = initialText, fg = "black", bg = "white", height = btnHeight, width = btnWidth, font = btnFont).grid(row = 1, column = 1)
btnSix = tk.Button(root, text = initialText, fg = "black", bg = "white", height = btnHeight, width = btnWidth, font = btnFont).grid(row = 1, column = 2)
btnSeven = tk.Button(root, text = initialText, fg = "black", bg = "white", height = btnHeight, width = btnWidth, font = btnFont).grid(row = 2, column = 0)
btnEight = tk.Button(root, text = initialText, fg = "black", bg = "white", height = btnHeight, width = btnWidth, font = btnFont).grid(row = 2, column = 1)
btnNine = tk.Button(root, text = initialText, fg = "black", bg = "white", height = btnHeight, width = btnWidth, font = btnFont).grid(row = 2, column = 2)

lblInfo = tk.Label(root, text="Your turn!", font=("Helvetica", 13), bg = systemColour).grid(row = 3, column = 1)

root.mainloop()

while(True):
    x = input("Press enter to exit!")
    break
