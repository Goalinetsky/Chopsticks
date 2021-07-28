import tkinter as tk

playerLeft = 1
playerRight = 1
botLeft = 1
botRight = 1
gamemode = 'standard'
gamemodeList = ['standard', 'rollover']

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
        master.title = ('Sticks')
        self.label = tk.Label(master, text = "test")
        self.label.pack
        self.greet_button = tk.Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()
        self.close_button = tk.Button(master, text="Close", command=master.quit)
        self.close_button.pack()
    def greet(self):
        print("Greetings!")

root = tk.Tk()
my_gui = GUI(root)
root.mainloop()