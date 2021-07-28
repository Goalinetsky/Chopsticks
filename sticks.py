# Chopsticks hand game
import random
import tkinter as tk
from tkinter import ttk

hands = [1,1,1,1]
gamemode = 'standard'

def attack(hands, attacker, defender):
    if hands[attacker] + hands[defender] < 5:
        hands[defender] = hands[attacker] + hands[defender]
    elif hands[attacker] + hands[defender] == 5:
        hands[defender] = 0
    elif hands[attacker] + hands[defender] > 5 and gamemode == 'rollover':
        hands[defender] = hands[attacker] + hands[defender] - 5
    else:
        hands[defender] = 0
    return hands

def split(hands, donator, reciever, num):
    hands[reciever] += num
    hands[donator] -= num
    return hands

class GUI:
    def __init__(self, master):
        self.master = master
        master.title('Chopsticks')
        self.title = tk.Label(master, text="Chopsticks", font=('Arial', 25))
        self.pic = tk.PhotoImage(file="logo.png")
        self.logo = tk.Label(master, image=self.pic)
        self.start_button = tk.Button(master, text="Start", font=('Arial', 15), command=self.start)
        self.exit_button = tk.Button(master, text="Exit", font=('Arial', 15), command=master.quit)
        self.n = tk.StringVar()
        self.modeSelect = ttk.Combobox(master, width=30, textvariable=self.n )
        self.modeSelect['values'] = ('standard', 'rollover')
        self.modeLabel = tk.Label(master, text="Select a gamemode", font=('Arial', 20))
        self.play = tk.Button(master, text="Play", font=('Arial', 15), command=self.game)
        self.player0 = tk.Label(master, text=1)
        self.player1 = tk.Label(master, text=1)
        self.bot0 = tk.Label(master, text=1)
        self.bot1 = tk.Label(master, text=1)

        self.exit_button.place(x=50, y=450)
        self.start_button.place(x=540, y=450)
        self.title.place(x=245, y=401)
        self.logo.place(x=75, y=0)

    def start(self):
        self.start_button.place_forget()
        self.title.place_forget()
        self.exit_button.place_forget()
        self.logo.place_forget()
        self.modeSelect.place(x=223, y=200)
        self.modeLabel.place(x=202, y=150)
        self.play.place(x=298, y=400)

    def game(self):
        self.modeLabel.place_forget()
        self.modeSelect.place_forget()
        self.play.place_forget()
        global gamemode
        gamemode = self.n.get()
        self.bot0.grid(row=1)
        self.bot1.grid(row=1, column=1)
        self.player0.grid(row=2)
        self.player1.grid(row=2, column=1)

    def endGame(self):
        print('play again?')

root = tk.Tk()
root.geometry('650x500')
rootHeight = root.winfo_height()
rootWidth = root.winfo_width()
my_gui = GUI(root)
root.mainloop()