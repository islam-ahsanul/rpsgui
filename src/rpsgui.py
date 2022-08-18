from tkinter import *
from random import randint


class RPS:
    def __init__(self):
        self.root = Tk()
        self.root.title("Rock Paper Scissor")
        self.root.geometry("900x500")
        self.root.configure(bg="#f5fffa")
        # ----------------------------------------------------------------------------------------------
        self.player_winCount = 0
        self.computer_winCount = 0
        self.playerStr = StringVar()
        self.playerStr.set("You: 0")
        self.computerStr = StringVar()
        self.computerStr.set("Computer: 0")
        self.toolbar = Frame(self.root, borderwidth=1, relief=SUNKEN)
        self.score = Label(self.toolbar, text="\nFinal Score: ", anchor=E, pady=10, padx=40, background="#b3ffd9")
        self.score.pack(fill=X)
        self.score.config(font=("Verdana", 16))
        self.player_score = Label(self.toolbar, textvariable=self.playerStr, anchor=E, pady=10, padx=40, background="#ccffe6")
        self.player_score.pack(fill=X)
        self.player_score.config(font=("Verdana", 15))
        self.computer_score = Label(self.toolbar, textvariable=self.computerStr, anchor=E, pady=10, padx=40, background="#e6fff2")
        self.computer_score.pack(fill=X)
        self.computer_score.config(font=("Verdana", 15))
        self.toolbar.pack(side=TOP, fill=X)
        # ----------------------------------------------------------------------------------------------
        self.text = StringVar()
        self.text.set("")
        self.r = IntVar()
        self.r.set(0)

        Radiobutton(self.root, text="Rock    ", variable=self.r, value=1, font=("Verdana", 12, "italic"), background="#f5fffa", activebackground="#f5fffa").pack()
        Radiobutton(self.root, text="Paper   ", variable=self.r, value=2, font=("Verdana", 12, "italic"), background="#f5fffa", activebackground="#f5fffa").pack()
        Radiobutton(self.root, text="Scissor ", variable=self.r, value=3, font=("Verdana", 12, "italic"), background="#f5fffa", activebackground="#f5fffa").pack()

        self.myButton = Button(self.root, text="Submit", command=self.clicked, padx=15, font=("Verdana", 12), background="#FFFFFF", activebackground="#ccffe6", borderwidth=1, relief=RAISED)
        self.myButton.pack(pady=15)
        self.myLabel = Label(self.root, textvariable=self.text, font=("Verdana", 14), background="#f5fffa").pack()
        # --------------------------------------------------------------------------------------------------
        self.matchCount = 0
        self.statusVar = StringVar()
        self.statusVar.set("Match - ")
        self.status = Label(self.root, textvariable=self.statusVar, anchor=E, bd=1, relief=RIDGE, font=("Verdana", 11),
                            padx=15, pady=5, background="#ccffe6")
        self.status.pack(side=BOTTOM, fill=X)
        # --------------------------------------------------------------------------------------------------

        self.root.mainloop()

    def change_result(self, value):
        self.text.set(value)
        self.matchCount += 1
        self.statusVar.set("Match - {}".format(self.matchCount))

    def player_win(self):
        self.player_winCount += 1
        self.playerStr.set("You: {}".format(self.player_winCount))

    def computer_win(self):
        self.computer_winCount += 1
        self.computerStr.set("Computer: {}".format(self.computer_winCount))

    def clicked(self):
        computer = randint(1, 3)
        if computer == self.r.get():
            self.change_result("Draw")

        elif self.r.get() == 1:
            if computer == 2:
                self.change_result("You lost! Computer played Paper")
                self.computer_win()
            elif computer == 3:
                self.change_result("You won! Computer played Scissor")
                self.player_win()

        elif self.r.get() == 2:
            if computer == 1:
                self.change_result("You won! Computer played Rock")
                self.player_win()
            elif computer == 3:
                self.change_result("You lost! Computer played Scissor")
                self.computer_win()

        elif self.r.get() == 3:
            if computer == 1:
                self.change_result("You lost! Computer played Rock")
                self.computer_win()
            elif computer == 2:
                self.change_result("You won! Computer played Paper")
                self.player_win()


obj = RPS()