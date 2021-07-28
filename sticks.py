# Chopsticks hand game
import tkinter as tk
from tkinter import ttk

playerLeft = 1
playerRight = 1
botLeft = 1
botRight = 1
gamemode = 'standard'

def attack(attacker, defender):
    if attacker + defender < 5:
        defender = attacker + defender
    elif attacker + defender == 5:
        defender = 0
    elif attacker + defender > 5 and gamemode == 'rollover':
        defender = attacker + defender - 5
    else:
        defender = 0
    return attacker, defender

def split(donator, reciever, num):
    reciever += num
    donator -= num
    return donator, reciever

class GUI:
    def __init__(self, master):
        self.master = master
        master.title('Chopsticks')
        self.title = tk.Label(master, text="Chopsticks")
        self.greet_button = tk.Button(master, text="Start", command=self.start)
        self.close_button = tk.Button(master, text="Exit", command=master.quit)
        self.n = tk.StringVar()
        self.modeSelect = ttk.Combobox(master, width=30, textvariable=self.n )
        self.modeSelect['values'] = ('standard', 'rollover')
        self.modeLabel = tk.Label(master, text="Select a gamemode")
        self.play = tk.Button(master, text="Play", command=self.game)
        self.close_button.grid(row=1, column=9)
        self.greet_button.grid(row=1)
        self.title.grid(columnspan=10, ipadx=0, ipady=0)

    def start(self):
        print("Greetings!")
        self.greet_button.grid_forget()
        self.title.grid_forget()
        self.close_button.grid_forget()
        self.modeSelect.grid(row=1, column=1)
        self.modeLabel.grid(row=1)
        self.play.grid(row=2, columnspan=2)

    def game(self):
        print("game goes here")

root = tk.Tk()
my_gui = GUI(root)
root.mainloop()