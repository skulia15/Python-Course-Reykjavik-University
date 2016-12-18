import sys
import time
from tkinter import *
from tkinter import messagebox
import random

class Application(Frame):
    buttons1 = []
    buttons2 = []
    class Mancala():
        GOAL_PLAYER1 = 0
        GOAL_PLAYER2 = 0
        BOARD_SIZE = 6
        LANE_PLAYER1 = []
        LANE_PLAYER2 = []
        CURRENT_PLAYER = 0
        GAME_IS_WON = False
        GAME_WINNER = None

    def __init__(self, master=None): #MAIN
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def resetgame(self):
        self.Mancala.GOAL_PLAYER1 = 0
        self.Mancala.GOAL_PLAYER2 = 0
        self.Mancala.LANE_PLAYER1 = [4 for i in range(self.Mancala.BOARD_SIZE)]
        self.Mancala.LANE_PLAYER2 = [4 for i in range(self.Mancala.BOARD_SIZE)]
        self.Mancala.CURRENT_PLAYER = 1
        self.Mancala.GAME_IS_WON = False
        self.Mancala.GAME_WINNER = None
        self.buttons1 = []
        self.buttons2 = []

    def getopponent(self):
        if self.Mancala.CURRENT_PLAYER == 1:
            return 2
        return 1

    def scoregoal(self):
        if self.Mancala.CURRENT_PLAYER == 1:
            self.Mancala.GOAL_PLAYER1 += 1
        else: self.Mancala.GOAL_PLAYER2 += 1


    def compmakemove(self):
        rand = random.randrange(self.Mancala.BOARD_SIZE)
        if self.Mancala.LANE_PLAYER2[rand] != 0:
            self.makemove(rand, 1)
        else:
            self.compmakemove()
    def updatemancala(self, i, stones):
        # ROLL THE BOARD
        for fields in range(i+1, self.Mancala.BOARD_SIZE):
            if stones > 0:
                stones -= 1
                neighbor = self.Mancala.BOARD_SIZE - fields - 1
                if self.Mancala.CURRENT_PLAYER == 1:
                    if stones == 0 and self.Mancala.LANE_PLAYER1[fields] == 0 \
                    and self.Mancala.LANE_PLAYER2[neighbor] != 0:
                        self.Mancala.GOAL_PLAYER1 += self.Mancala.LANE_PLAYER2[neighbor] + 1
                        self.Mancala.LANE_PLAYER2[neighbor] = 0
                    else:
                        self.Mancala.LANE_PLAYER1[fields] += 1
                else:
                    if stones == 0 and self.Mancala.LANE_PLAYER2[fields] == 0 \
                    and self.Mancala.LANE_PLAYER1[neighbor] != 0:
                        self.Mancala.GOAL_PLAYER2 += self.Mancala.LANE_PLAYER1[neighbor] + 1
                        self.Mancala.LANE_PLAYER1[neighbor] = 0
                    else:
                        self.Mancala.LANE_PLAYER2[fields] += 1

        # GET NEXT LANE
        currlane = self.Mancala.CURRENT_PLAYER

        while stones:
            # GET NEXT LANE
            if currlane == 1:
                currlane = 2
            else: currlane = 1

            # IF DONE WITH CURRENT PLAYERS LANE
            if currlane != self.Mancala.CURRENT_PLAYER:
                self.scoregoal()
                stones -= 1
                # IF WE FINISH AT GOAL GO AGAIN
                if stones == 0:
                    self.Mancala.CURRENT_PLAYER = self.getopponent()

            # GO THOUGH NEXT LANE
            for fields in range(self.Mancala.BOARD_SIZE):
                if stones > 0:
                    stones -= 1
                    neighbor = self.Mancala.BOARD_SIZE - fields - 1
                    if currlane == 1:
                        if currlane == self.Mancala.CURRENT_PLAYER and stones == 0 and \
                                        self.Mancala.LANE_PLAYER1[fields] == 0 and\
                                        self.Mancala.LANE_PLAYER2[neighbor] != 0:
                            self.Mancala.GOAL_PLAYER1 += self.Mancala.LANE_PLAYER2[neighbor] + 1
                            self.Mancala.LANE_PLAYER2[neighbor] = 0
                        else:
                            self.Mancala.LANE_PLAYER1[fields] += 1
                    else:
                        if currlane == self.Mancala.CURRENT_PLAYER and stones == 0 and\
                                        self.Mancala.LANE_PLAYER2[fields] == 0 and\
                                        self.Mancala.LANE_PLAYER1[neighbor] != 0:
                            self.Mancala.GOAL_PLAYER2 += self.Mancala.LANE_PLAYER1[neighbor] + 1
                            self.Mancala.LANE_PLAYER1[neighbor] = 0
                        else:
                            self.Mancala.LANE_PLAYER2[fields] += 1

    def uncolorrange(self, event): # RESET COLORS FROM LAST FUNCTION
        for x in range(self.Mancala.BOARD_SIZE):
            self.buttons1[x].configure(fg="black", bg="lightblue")
            self.buttons2[x].configure(fg="black", bg="pink")
        self.goal1.configure(fg="black", bg="lightblue")
        self.goal2.configure(fg="black", bg="pink")
        #self.recolorrange("lightblue", "lightblue", "pink", "pink", event.widget.i)

    def colorrange(self, event): # SHOW HOW FAR THE STONES WILL TRAVEL
        if event.widget["state"] == DISABLED:
            return

        i = event.widget.i

        if self.Mancala.CURRENT_PLAYER == 1:
            # NUMBER OF FIELDS THE STONES CAN TRAVEL
            stones = self.Mancala.LANE_PLAYER1[i]
            currlane = 1
            # ORIGINAL FIELD COLORED DIFFERENTLY
            self.buttons1[i].configure(fg="white", bg="navy")
        else:
            stones = self.Mancala.LANE_PLAYER2[5-i]
            currlane = 2
            self.buttons2[i].configure(fg="white", bg="darkred")
        if stones > 12:
            circle = True
        else:
            circle = False

        # COLOR FIELDS IN THE SAME LANE AS THE ORIGINAL FIELD
        if currlane == 1:
            for fields in range(i+1, self.Mancala.BOARD_SIZE):
                if stones > 0:
                    stones -= 1
                    self.buttons1[fields].configure(fg="white", bg="blue")
        else:
            for fields in range(5-(i-1), self.Mancala.BOARD_SIZE):
                if stones > 0:
                    stones -= 1
                    self.buttons2[5-fields].configure(fg="white", bg="red")
        while stones:
            # GET NEXT LANE
            if currlane == 1:
                currlane = 2
            else: currlane = 1

            if currlane != self.Mancala.CURRENT_PLAYER: #CHECK IF THE PLAYER WILL SCORE
                stones -= 1
                if stones == 0 and circle:
                    if self.Mancala.CURRENT_PLAYER == 1:
                        self.goal1.configure(fg="white", bg="purple")
                    else:
                        self.goal2.configure(fg="white", bg="orange")
                else:
                    if self.Mancala.CURRENT_PLAYER == 1:
                        self.goal1.configure(fg="white", bg="blue")
                    else:
                        self.goal2.configure(fg="white", bg="red")
                

            # GO THROUGH NEXT LANE
            for fields in range(self.Mancala.BOARD_SIZE):
                if stones > 0:
                    stones -= 1
                    if stones == 0 and circle:
                        if currlane == 1:
                            self.buttons1[fields].configure(fg="white", bg="purple")
                        else:
                            self.buttons2[5-fields].configure(fg="white", bg="orange")     
                    else:
                        if currlane == 1:
                            self.buttons1[fields].configure(fg="white", bg="blue")
                        else:
                            self.buttons2[5-fields].configure(fg="white", bg="red")

        if self.Mancala.CURRENT_PLAYER == 1:
            self.buttons1[i].configure(fg="white", bg="navy") #RECOLOR ORIGINAL BUTTON, IN CASE IT WAS OVERWRITTEN
        else:
            self.buttons2[i].configure(fg="white", bg="darkred")


    def makemove(self, i, nrofplayers):
        self.uncolorrange("shithappens") # EXCUSE THE HAX
        # FOR PLAYER 1
        if self.Mancala.CURRENT_PLAYER == 1:
            stones = self.Mancala.LANE_PLAYER1[i] # GET STONES
            self.Mancala.LANE_PLAYER1[i] = 0
        # FOR PLAYER 2
        else:
            stones = self.Mancala.LANE_PLAYER2[i]
            self.Mancala.LANE_PLAYER2[i] = 0

        # UPDATE VALUES
        self.updatemancala(i, stones)

        win = self.endstuff()

        self.updateboard()
        #if nrofplayers == 1 and self.Mancala.CURRENT_PLAYER == 2:
        if win:
            self.seewinner()
        elif nrofplayers == 1 and self.Mancala.CURRENT_PLAYER == 1:
            BASE.after(1000, self.compmakemove)

        # CHANGE CURRENT PLAYER
        self.Mancala.CURRENT_PLAYER = self.getopponent()

    def endstuff(self):
        # IF EMPTY TAKE SUM OF OPPONENTS BOARD TO OPPONENT
        zeroboard = [0 for i in range(self.Mancala.BOARD_SIZE)]
        if self.Mancala.LANE_PLAYER1 == zeroboard:
            self.Mancala.GOAL_PLAYER2 += sum(self.Mancala.LANE_PLAYER2)
            self.Mancala.LANE_PLAYER2 = zeroboard
            self.Mancala.GAME_IS_WON = True
        elif self.Mancala.LANE_PLAYER2 == zeroboard:
            self.Mancala.GOAL_PLAYER1 += sum(self.Mancala.LANE_PLAYER1)
            self.Mancala.LANE_PLAYER1 = [0 for i in range(self.Mancala.BOARD_SIZE)]
            self.Mancala.GAME_IS_WON = True

        if self.Mancala.GAME_IS_WON:
            self.Mancala.GAME_WINNER = self.getwinner()
            return True
        return False

    def seewinner(self):
        if self.Mancala.GAME_WINNER == 0:
            displayWinner = "It's a draw!"
        else:
            displayWinner = "Player " + str(self.Mancala.GAME_WINNER) + " won the game!"
        messagebox.showinfo("The game has been won", displayWinner)

    def goToMenu(self, continueButton):
        for widget in self.winfo_children():
            widget.destroy()
        continueButton.destroy()
        self.resetgame()
        self.__init__()

    def getwinner(self):
        if self.Mancala.GOAL_PLAYER1 > self.Mancala.GOAL_PLAYER2:
            return 1
        elif self.Mancala.GOAL_PLAYER2 > self.Mancala.GOAL_PLAYER1:
            return 2
        else:
            return 0

    def updateboard(self):
        # UPDATE BOARD
        for x in range(self.Mancala.BOARD_SIZE):
            self.buttons1[x].configure(text=self.Mancala.LANE_PLAYER1[x])
            self.buttons2[x].configure(text=self.Mancala.LANE_PLAYER2[self.Mancala.BOARD_SIZE-1-x])
        self.goal1.configure(text=str(self.Mancala.GOAL_PLAYER1) + "\n Player 1")
        self.goal2.configure(text="Player 2\n" + str(self.Mancala.GOAL_PLAYER2))

        # UPDATES IF PLAYER 1 IS CURRENT PLAYER
        if self.Mancala.CURRENT_PLAYER == 1:
            self.goal1.configure(fg="black", bg="white")      # REPAINT BOARD
            self.goal2.configure(fg="black", bg="pink")  # REPAINT BOARD

            for buttons in self.buttons2:
                if buttons["text"] != 0:
                    buttons.configure(state=NORMAL)
                else: buttons.configure(state=DISABLED)
            for buttons in self.buttons1:
                buttons.configure(state=DISABLED)

        # UPDATES IF PLAYER 2 IS CURRENT PLAYER
        else:
            self.goal1.configure(fg="black", bg="lightblue")
            self.goal2.configure(fg="black", bg="white")
            for buttons in self.buttons1:
                if buttons["text"] != 0:
                    buttons.configure(state=NORMAL)
                    
                else: buttons.configure(state=DISABLED)
            for buttons in self.buttons2:
                buttons.configure(state=DISABLED)


    def createboard(self, i, middleframe, nrofplayers):
        middleframe.configure(bg="white")
        left = Button(middleframe, text=self.Mancala.LANE_PLAYER1[i], bg="lightblue", height=2,
                      width=15, activebackground="blue",
                      command=lambda i=i: self.makemove(i, nrofplayers))
        left.i = i
        if nrofplayers == 2:
            right = Button(middleframe, text=self.Mancala.LANE_PLAYER2[i], bg="pink",
                           state=DISABLED, height=2, width=15, activebackground="red",
                           command=lambda i=i: self.makemove(5-i, nrofplayers))
            right.bind('<Enter>', self.colorrange)
            right.bind('<Leave>', self.uncolorrange)
        else:
            right = Button(middleframe, text=self.Mancala.LANE_PLAYER2[i], bg="pink",\
                    state=DISABLED, height=2, width=15)
        right.i = i
        left.bind('<Enter>', self.colorrange)
        left.bind('<Leave>', self.uncolorrange)

        left.grid(row=i, column=0, padx=15, pady=2)
        self.buttons1.append(left)
        right.grid(row=i, column=1, padx=15)
        self.buttons2.append(right)
    def create_everything(self, nrofplayers):
        # MIDDLEFRAME HANDLES GRID FOR FIELDS
        self.configure(bg="white")
        middleframe = Frame(self)
        middleframe.grid(row=4, column=0)

        # CREATE GOAL FOR PLAYER 2
        self.goal2 = Label(self, text="Player 2\n" + str(self.Mancala.GOAL_PLAYER2), \
                     height=3, width=55, bg="white", font=("Comic Sans MS", 14, "bold"))
        self.goal2.grid(row=1, column=0, sticky=W+E+N+S)
        for i in range(self.Mancala.BOARD_SIZE):
            self.createboard(i, middleframe, nrofplayers)
        # CREATE GOAL FOR PLAYER 1
        self.goal1 = Label(self, text=str(self.Mancala.GOAL_PLAYER1) + "\n Player 1", height=3, width = 55, bg="lightblue", font=("Comic Sans MS", 14 ,"bold"))
        self.goal1.grid(row=7, column=0, sticky=W+E+N+S)

        # BACK TO MENU BUTTON
        btmbutton = Button(text="Back to menu", width=15, height=4, command=lambda: self.goToMenu(btmbutton))
        btmbutton.grid(row=0, column=0, sticky=E)
        btmbutton.bind('<Enter>', self.colorButton)
        btmbutton.bind('<Leave>', self.uncolorButton)

    def create_widgets(self):
        def start_create_everything(nrofplayers):
            startpvc.destroy()
            startpvp.destroy()
            rules.destroy()
            quitb.destroy()
            self.resetgame()
            self.create_everything(nrofplayers)

        menubuttonfont = ("Comic Sans MS", 12, "bold")
        startpvc = Button(text="Start 1 Player Game", width=65, height=4, \
            font=menubuttonfont, command=lambda: start_create_everything(1))
        startpvp = Button(text="Start 2 Player Game", width=65, height=4, \
            font=menubuttonfont, command=lambda: start_create_everything(2))
        rules = Button(text="Mancala Rules", width=65, height=4, \
            font=menubuttonfont, command=lambda: openrules())
        quitb = Button(text="Exit Game", width=65, height=4, \
            font=menubuttonfont, fg="red", command=lambda: BASE.destroy())
        startpvc.grid()
        startpvp.grid()
        rules.grid()
        rules.bind('<Enter>', self.colorButton)
        rules.bind('<Leave>', self.uncolorButton)
        startpvc.bind('<Enter>', self.colorButton)
        startpvc.bind('<Leave>', self.uncolorButton)
        startpvp.bind('<Enter>', self.colorButton)
        startpvp.bind('<Leave>', self.uncolorButton)
        quitb.bind('<Enter>', self.colorButton)
        quitb.bind('<Leave>', self.uncolorButton)
        quitb.grid()

    def colorButton(self, event):
        event.widget['bg'] = 'lightgrey'

    def uncolorButton(self, event):
        event.widget['bg'] = 'white'

    def colorPitButtonLeft(self, event):
        if event.widget["state"] != "disabled":
            event.widget['bg'] = 'blue'

    def uncolorPitButtonLeft(self, event):
        event.widget['bg'] = 'lightblue'

    def colorPitButtonRight(self, event):
        if event.widget["state"] != "disabled":
            event.widget['bg'] = 'red'

    def uncolorPitButtonRight(self, event):
        event.widget['bg'] = 'pink'

def createMenuBar():
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Exit", command=BASE.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Game Rules", command=lambda: openrules())
    menubar.add_cascade(label="Help", menu=helpmenu)

def openrules():
    messagebox.showinfo("Mancala Rules", "A Mancala board consists of 2 sides of 6 pits, and 2 goals."+
                        " Each pit contains 4 stones.\nTo take a turn, the player first chooses a"+
                        " non-empty pit from their side and picks up all the stones contained in it." +
                        " The player then drops a single stone into the next pit in an anticlockwise" +
                        " direction, a single stone into the pit after that and so on until the" +
                        " stones run out. If the player passes their own goal, they drop a stone there as well," +
                        " but they skip the opponents goal. They then proceed to place the stones in the other lane.\n" +
                        " If the last stone dropped is in the player's goal, they get a free turn.\nIf the last stone" +
                        " dropped is in an empty pit on the players side, that stone, and all the stones in the pit" +
                        " opposite are placed in the player's goal.\nThe game ends when all the pits on one side are empty." +
                        " All the stones on the opposite side are then placed in the corresponding goal.\nThe winner is" +
                        " the player with the most stones in their goal when the game ends."
                        )

BASE = Tk()
menubar = Menu(BASE)
createMenuBar()
BASE.config(menu=menubar)
APP = Application(master=BASE)
APP.master.title("Mancala")
APP.mainloop()
