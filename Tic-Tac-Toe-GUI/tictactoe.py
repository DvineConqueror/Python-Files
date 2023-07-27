from tkinter import *
import random


def nextTurn(row, column):
    pass


def checkWinner():
    pass


def emptySpaces():
    pass


def newGame():
    pass


window = Tk()
window.title("Tic-Tac-Toe!")
players = ["X", "O"]
player = random.choice(players)
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

Label = Label(text=player + " turn", font=('helvetica', 40))
Label.pack(side="top")
reset_button = Button(text="Restart", font=('helvetica', 20), command=newGame)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('helvetica', 20), width=5, height=2, command= lambda row=row, column=column: nextTurn(row, column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()
