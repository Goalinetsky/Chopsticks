# Chopsticks hand game
import tkinter as tk
from tkinter import ttk

hands = [1,2,4,0]
gamemode = 'Standard'
selected = 'none'

def attack(hands, attacker, defender): # hand positions [0,1,2,3]    0 1  bot
    if hands[attacker] + hands[defender] < 5: #                      2 3  player
        hands[defender] = hands[attacker] + hands[defender]
    elif hands[attacker] + hands[defender] == 5:
        hands[defender] = 0
    elif hands[attacker] + hands[defender] > 5 and gamemode == 'Rollover':
        hands[defender] = hands[attacker] + hands[defender] - 5
    else:
        hands[defender] = 0
    return hands

def split(hands, donator, reciever, num): 
    hands[reciever] += num
    hands[donator] -= num
    return hands

def selectHand2(event): # handles mouse release to pick hand 2
    global selected
    if selected == 3 and hands[3] > 1:
        my_gui.arrowLeft.place(x=290, y=260)
        print('we got here')
    elif hands[2] !=0 and selected != 2:
        my_gui.player2.place_forget()
        my_gui.player2Selected.place(x=150, y=350)
        selected = 2
    elif hands[2] == 0:
        pass
    else:
        my_gui.player2Selected.place_forget()
        my_gui.player2.place(x=150, y=350)
        selected = 'none'
        
def selectHand3(event): # handles mouse release to pick hand 3
    global selected
    if selected == 2 and hands[2] > 1:
        my_gui.arrowRight.place(x=290, y=260)
    elif hands[3] !=0 and selected != 3:
        my_gui.player3.place_forget()
        my_gui.player3Selected.place(x=460, y=350)
        selected = 3
    elif hands[3] == 0:
        pass
    else:
        my_gui.player3Selected.place_forget()
        my_gui.player3.place(x=460, y=350)
        selected = 'none'


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
        self.modeSelect['values'] = ('Standard', 'Also Standard for rn')
        self.modeSelect.set('Standard')
        self.modeLabel = tk.Label(master, text="Select a gamemode", font=('Arial', 20))
        self.play = tk.Button(master, text="Play", font=('Arial', 15), command=self.gameStart)

        self.player2 = tk.Label(master, text=hands[2], font=('Arial', 45), borderwidth=2, relief='groove')
        self.player2.bind('<ButtonRelease-1>', selectHand2)
        self.player3 = tk.Label(master, text=hands[3], font=('Arial', 45), borderwidth=2, relief='groove')
        self.player3.bind('<ButtonRelease-1>', selectHand3)
        self.bot0 = tk.Label(master, text=hands[0], font=('Arial', 45), borderwidth=2, relief='groove')
        self.bot1 = tk.Label(master, text=hands[1], font=('Arial', 45), borderwidth=2, relief='groove')

        self.player2Selected = tk.Label(master, text=hands[2], font=('Arial', 45), borderwidth=4, relief='solid')
        self.player2Selected.bind('<ButtonRelease-1>', selectHand2)
        self.player3Selected = tk.Label(master, text=hands[3], font=('Arial', 45), borderwidth=4, relief='solid')
        self.player3Selected.bind('<ButtonRelease-1>', selectHand3)
        self.bot0Selected = tk.Label(master, text=hands[0], font=('Arial', 45), borderwidth=4, relief='solid')
        self.bot1Selected = tk.Label(master, text=hands[1], font=('Arial', 45), borderwidth=4, relief='solid')

        self.pic1 = tk.PhotoImage(file="arrow-left.png")
        self.arrowLeft = tk.Label(master, image=self.pic1)
        self.pic2 = tk.PhotoImage(file="arrow-right.png")
        self.arrowRight = tk.Label(master, image=self.pic2)

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

    def gameStart(self):
        self.modeLabel.place_forget()
        self.modeSelect.place_forget()
        self.play.place_forget()
        global gamemode
        gamemode = self.n.get()
        self.bot0.place(x=150, y=100)
        self.bot1.place(x=460, y=100)
        self.player2.place(x=150, y=350)
        self.player3.place(x=460, y=350)

    def endGame(self):
        print('play again?')

root = tk.Tk()
w = 650 # root width 
h = 500 # root height
x = root.winfo_screenwidth()/2 - w/2 # find x position to open
y = root.winfo_screenheight()/2 - h/2 # find y position to open
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
my_gui = GUI(root)
root.mainloop()