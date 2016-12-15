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
        LANE_PLAYER1 = [1 for i in range(BOARD_SIZE)]
        LANE_PLAYER2 = [1 for i in range(BOARD_SIZE)]
        CURRENT_PLAYER = 2
        GAME_IS_WON = False
        GAME_WINNER = None

    def __init__(self, master=None): #MAIN
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def resetGame(self):
        self.Mancala.GOAL_PLAYER1 = 0
        self.Mancala.GOAL_PLAYER2 = 0
        self.Mancala.LANE_PLAYER1 = [4 for i in range(self.Mancala.BOARD_SIZE)]
        self.Mancala.LANE_PLAYER2 = [4 for i in range(self.Mancala.BOARD_SIZE)]
        self.Mancala.CURRENT_PLAYER = 2
        self.Mancala.GAME_IS_WON = False
        self.GAME_WINNER = None
        self.buttons1 = []
        self.buttons2 = []

    def getWhosTurn(self):
        if self.Mancala.CURRENT_PLAYER == 1:
            return 2
        return 1

    def scoregoal(self):
        if self.Mancala.CURRENT_PLAYER == 1:
            self.Mancala.GOAL_PLAYER1 += 1
        else: self.Mancala.GOAL_PLAYER2 += 1


    def compMakeMove(self):
        rand = random.randrange(self.Mancala.BOARD_SIZE)
        if self.Mancala.LANE_PLAYER2[rand] != 0:
            self.makeMove(rand, 1)
        else:
            self.compMakeMove()

    def makeMove(self, i, nrOfPlayers):
        # CHANGE CURRENT PLAYER
        self.Mancala.CURRENT_PLAYER = self.getWhosTurn()

        # FOR PLAYER 1
        if self.Mancala.CURRENT_PLAYER == 1:
            stones = self.Mancala.LANE_PLAYER1[i] # GET STONES
            self.Mancala.LANE_PLAYER1[i] = 0
        # FOR PLAYER 2
        else:
            stones = self.Mancala.LANE_PLAYER2[i]
            self.Mancala.LANE_PLAYER2[i] = 0

        # ROLL THE BOARD
        for fields in range(i+1, self.Mancala.BOARD_SIZE):
            if stones > 0:
                stones -= 1
                neighbor = self.Mancala.BOARD_SIZE - fields - 1
                if self.Mancala.CURRENT_PLAYER == 1:
                    if stones == 0 and self.Mancala.LANE_PLAYER1[fields] == 0 and self.Mancala.LANE_PLAYER2[neighbor] != 0:
                        self.Mancala.GOAL_PLAYER1 += self.Mancala.LANE_PLAYER2[neighbor] + 1
                        self.Mancala.LANE_PLAYER2[neighbor] = 0
                    else:
                        self.Mancala.LANE_PLAYER1[fields] += 1
                else:
                    if stones == 0 and self.Mancala.LANE_PLAYER2[fields] == 0 and self.Mancala.LANE_PLAYER1[neighbor] != 0:
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
                    self.Mancala.CURRENT_PLAYER = self.getWhosTurn()

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
        win = self.endstuff()

        self.updateboard()
        #if nrOfPlayers == 1 and self.Mancala.CURRENT_PLAYER == 2:
        if win:
            self.seewinner()
        elif nrOfPlayers == 1 and self.Mancala.CURRENT_PLAYER == 1:
            self.compMakeMove()

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
        self.resetGame()
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
            self.goal1.configure(bg="white")      # REPAINT BOARD
            self.goal2.configure(bg="pink")  # REPAINT BOARD

            for buttons in self.buttons2:
                if buttons["text"] != 0:
                    buttons.configure(state=NORMAL)
                else: buttons.configure(state=DISABLED)
            for buttons in self.buttons1:
                buttons.configure(state=DISABLED)

        # UPDATES IF PLAYER 2 IS CURRENT PLAYER
        else:
            self.goal1.configure(bg="lightblue")
            self.goal2.configure(bg="white")
            for buttons in self.buttons1:
                if buttons["text"] != 0:
                    buttons.configure(state=NORMAL)
                    
                else: buttons.configure(state=DISABLED)
            for buttons in self.buttons2:
                buttons.configure(state=DISABLED)


    def createboard(self, i, middleframe, nrOfPlayers):
        middleframe.configure(bg="white")
        left = Button(middleframe, text=self.Mancala.LANE_PLAYER1[i], bg="lightblue", height=2,\
                width=15, activebackground="blue", command=lambda i=i:self.makeMove(i, nrOfPlayers))
        if nrOfPlayers == 2:
            right = Button(middleframe, text=self.Mancala.LANE_PLAYER2[i], bg="pink",\
                    state=DISABLED, height=2, width=15, activebackground="red", command=lambda i=i: self.makeMove(5-i, nrOfPlayers))
        else:
            right = Button(middleframe, text=self.Mancala.LANE_PLAYER2[i], bg="pink",\
                    state=DISABLED, height=2, width=15, activebackground="red")
        left.bind('<Enter>', self.colorPitButtonLeft)
        left.bind('<Leave>', self.uncolorPitButtonLeft)
        right.bind('<Enter>', self.colorPitButtonRight)
        right.bind('<Leave>', self.uncolorPitButtonRight)

        left.grid(row=i, column=0, padx=15, pady=2)
        self.buttons1.append(left)
        right.grid(row=i, column=1, padx=15)
        self.buttons2.append(right)

    def create_everything(self, nrOfPlayers):
        #MIDDLEFRAME HANDLES GRID FOR FIELDS
        self.configure(bg="white")
        middleframe = Frame(self)
        middleframe.grid(row=4, column=0)
        #CREATE GOAL FOR PLAYER 2
        self.goal2 = Label(self, text="Player 2\n" + str(self.Mancala.GOAL_PLAYER2), \
                     height=3, width=55, bg="white", font=("Comic Sans MS", 14 ,"bold"))
        self.goal2.grid(row=1, column=0, sticky=W+E+N+S)
        for i in range(self.Mancala.BOARD_SIZE):
            self.createboard(i, middleframe, nrOfPlayers)
        #CREATE GOAL FOR PLAYER 1
        self.goal1 = Label(self, text=str(self.Mancala.GOAL_PLAYER1) + "\n Player 1", height=3, width = 55, bg="lightblue", font=("Comic Sans MS", 14 ,"bold"))
        self.goal1.grid(row=7, column=0, sticky=W+E+N+S)
        continueButton = Button(text= "Back to menu", width=15, height= 4, command=lambda: self.goToMenu(continueButton))
        continueButton.grid(row = 0, column=0, sticky=E)
        continueButton.bind('<Enter>', self.colorButton)
        continueButton.bind('<Leave>', self.uncolorButton)

    def create_widgets(self):
        def start_create_everything(nrOfPlayers):
            startPvP.destroy()
            startPvC.destroy()
            rules.destroy()
            quitb.destroy()
            self.resetGame()
            self.create_everything(nrOfPlayers)

        startPvC = Button(text="Start 1 Player Game",width=65, height=4,  font=("Comic Sans MS", 12 ,"bold"), command=lambda: start_create_everything(1))
        startPvP = Button(text="Start 2 Player Game",width=65, height=4,  font=("Comic Sans MS", 12 ,"bold"), command=lambda: start_create_everything(2))
        rules = Button(text="Mancala Rules", width=65, height=4, font=("Comic Sans MS", 12 ,"bold"), command=lambda: openrules())
        quitb = Button(text="Exit Game", width=65, height=4, font=("Comic Sans MS", 12 ,"bold"), fg= "red", command=lambda: BASE.destroy())
        startPvC.grid()
        startPvP.grid()
        rules.grid()
        rules.bind('<Enter>', self.colorButton)
        rules.bind('<Leave>', self.uncolorButton)
        startPvC.bind('<Enter>', self.colorButton)
        startPvC.bind('<Leave>', self.uncolorButton)
        startPvP.bind('<Enter>', self.colorButton)
        startPvP.bind('<Leave>', self.uncolorButton)
        quitb.bind('<Enter>', self.colorButton)
        quitb.bind('<Leave>', self.uncolorButton)
        quitb.grid()
    
    def colorButton(self, event):
        event.widget['bg']= 'lightgrey'    
        
    def uncolorButton(self, event):
        event.widget['bg']= 'white'

    def colorPitButtonLeft(self, event):
        if event.widget["state"] != "disabled":
            event.widget['bg']= 'blue'    
        
    def uncolorPitButtonLeft(self, event):
        event.widget['bg']= 'lightblue'

    def colorPitButtonRight(self, event):
        if event.widget["state"] != "disabled":
            event.widget['bg']= 'red'    
        
    def uncolorPitButtonRight(self, event):
        event.widget['bg']= 'pink'
                
def createMenuBar():
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=BASE.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Game Rules", command=lambda: openrules())
        menubar.add_cascade(label="Help", menu=helpmenu)

def openrules():
            messagebox.showinfo("Mancala Rules", "Players take turns to play seeds.  To take a turn," +
            " the player first chooses a non-empty hollow from one of the six in the near row and picks" + 
            " up all the seeds contained in it.  The player then drops a single seed into the next hollow" +
            " in an anticlockwise direction, a single seed into the hollow after that and so on until the" +
            " seeds run out.   This is called \"sowing\" the seeds. When the player reaches the end of a row," +
            " sowing continues in an anti-clockwise direction in the other row. \n\n"+
            "When a player picks a hollow with so many seeds (12 or more) that one or more laps is done, the 12th"+
            " (and 23rd) seed is not played in the originating hollow - the originating hollow is skipped and the" + 
            " seed is played in the next hollow on.  This means that the originating hollow is always left" +
            "empty at the end of the turn.\n\n" +
            "If the last seed is sown in the opponents row and the hollow concerned finishes with 2 or 3 seeds," +
            " those seeds are captured.  If the hollow that immediately precedes it also contains 2 or 3 seeds," +
            " these seeds are also captured and so on until a hollow is reached that does not contain 2 or 3 seeds"+
            " or the end of the opponents row is reached.")

BASE = Tk()
#BASE.geometry("675x475")
menubar = Menu(BASE)
createMenuBar()
BASE.config(menu=menubar)
APP = Application(master=BASE)
APP.master.title("Mancala")
APP.mainloop()
