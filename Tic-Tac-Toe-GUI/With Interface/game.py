# game.py
import tkinter.messagebox as messagebox
from tkinter import Frame, Button, Label, DISABLED, NORMAL, Tk
from bot import get_bot_move

class TicTacToeGame:
    def __init__(self, window, human_vs_human=True):
        self.window = window
        self.human_vs_human = human_vs_human
        self.players = ['X', 'O']
        self.current_player = self.players[0]
        self.buttons = [[None, None, None] for _ in range(3)]
        self.create_gui()
        self.reset_game()

    def create_gui(self):
        self.title_label = Label(self.window, text="Tic-Tac-Toe", font=('consolas', 40))
        self.title_label.pack()

        self.status_label = Label(self.window, text=self.current_player + "'s turn", font=('consolas', 20))
        self.status_label.pack()

        self.reset_button = Button(self.window, text="Restart", font=('consolas', 20), command=self.reset_game)
        self.reset_button.pack()

        self.board_frame = Frame(self.window)
        self.board_frame.pack()

        for row in range(3):
            for col in range(3):
                self.buttons[row][col] = Button(self.board_frame, text="", font=('consolas', 20), width=5, height=2,
                                                 command=lambda row=row, col=col: self.make_move(row, col))
                self.buttons[row][col].grid(row=row, column=col)

    def reset_game(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="", state=NORMAL, bg="SystemButtonFace")
        self.current_player = self.players[0]
        self.status_label.config(text=self.current_player + "'s turn")

    def make_move(self, row, col):
        if self.buttons[row][col]['text'] == "" and not self.check_winner():
            self.buttons[row][col].config(text=self.current_player, state=DISABLED)
            if not self.check_winner() and not self.is_tie():
                self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]
                self.status_label.config(text=self.current_player + "'s turn")
                if not self.human_vs_human and self.current_player == self.players[1]:
                    self.window.after(2500, self.make_bot_move)  # 3000 milliseconds = 3 seconds
                    
    def make_bot_move(self):
        row, col = get_bot_move(self.buttons)
        self.make_move(row, col)

    def check_winner(self):
        for row in range(3):
            if self.buttons[row][0]['text'] == self.buttons[row][1]['text'] == self.buttons[row][2]['text'] != "":
                self.highlight_cells(row, 0, row, 1, row, 2)
                self.show_winner(self.buttons[row][0]['text'])
                return True

        for column in range(3):
            if self.buttons[0][column]['text'] == self.buttons[1][column]['text'] == self.buttons[2][column]['text'] != "":
                self.highlight_cells(0, column, 1, column, 2, column)
                self.show_winner(self.buttons[0][column]['text'])
                return True

        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != "":
            self.highlight_cells(0, 0, 1, 1, 2, 2)
            self.show_winner(self.buttons[0][0]['text'])
            return True

        elif self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != "":
            self.highlight_cells(0, 2, 1, 1, 2, 0)
            self.show_winner(self.buttons[0][2]['text'])
            return True

        return False

    def highlight_cells(self, *cells):
        for i in range(0, len(cells), 2):
            row, col = cells[i], cells[i+1]
            self.buttons[row][col].config(bg="green")

    def show_winner(self, winner):
        self.status_label.config(text="Player " + winner + " won!")

    def empty_spaces(self):
        spaces = 9
        for row in range(3):
            for column in range(3):
                if self.buttons[row][column]['text'] != "":
                    spaces -= 1

        return spaces == 0

    def is_tie(self):
        if self.empty_spaces() and not self.check_winner():
            for row in range(3):
                for column in range(3):
                    self.buttons[row][column].config(bg="yellow")
            return True
        return False

def start_game(human_vs_human=True):
    window = Tk()
    window.title("Tic-Tac-Toe Game")
    TicTacToeGame(window, human_vs_human)
    window.mainloop()
