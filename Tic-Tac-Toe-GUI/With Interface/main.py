# main.py
from tkinter import Tk, Button, Label
import game

def human_vs_human():
    game.start_game(human_vs_human=True)

def human_vs_bot():
    game.start_game(human_vs_human=False)

def exit_game():
    window.destroy()

if __name__ == "__main__":
    window = Tk()
    window.title("Tic-Tac-Toe Game")

    title_label = Label(text="Tic-Tac-Toe", font=('consolas', 40))
    title_label.pack()

    human_vs_human_btn = Button(window, text="Human vs Human", font=('consolas', 20), command=human_vs_human)
    human_vs_human_btn.pack()

    human_vs_bot_btn = Button(window, text="Human vs Bot", font=('consolas', 20), command=human_vs_bot)
    human_vs_bot_btn.pack()

    exit_btn = Button(window, text="Exit", font=('consolas', 20), command=exit_game)
    exit_btn.pack()

    window.mainloop()
