from tkinter import *

class Application(Frame):
    class Mancala:
        GOAL_PLAYER1 = 0
        GOAL_PLAYER2 = 0
        BOARD_SIZE = 6
        LANE_PLAYER1 = [4, 4, 4, 4, 4, 4]
        LANE_PLAYER2 = [4, 4, 4, 4, 4, 4]
        CURRENT_PLAYER = 2
        GAME_IS_WON = False

    buttons1 = []
    buttons2 = []

    def __init__(self, master=None): #MAIN
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def getWhosTurn(self):
        if self.Mancala.CURRENT_PLAYER == 2:
            return 1
        else:
            return 2

    def scoregoal(self):
        if self.Mancala.CURRENT_PLAYER == 1:
            self.Mancala.GOAL_PLAYER1 += 1
        else: self.Mancala.GOAL_PLAYER2 += 1

    def makeMove(self, i):
        #SEE WHO MADE THE TURN
        self.Mancala.CURRENT_PLAYER = self.getWhosTurn()
        print("Player "+ str(self.Mancala.CURRENT_PLAYER) + " made a move")

        #FOR PLAYER 1
        if self.Mancala.CURRENT_PLAYER == 1:
            stones = self.Mancala.LANE_PLAYER1[i] # GET STONES
            self.Mancala.LANE_PLAYER1[i] = 0
        #FOR PLAYER 2
        else:
            stones = self.Mancala.LANE_PLAYER2[i]
            self.Mancala.LANE_PLAYER2[i] = 0

        # ROLL THE BOARD
        for fields in range(i+1, self.Mancala.BOARD_SIZE):
            if stones > 0:
                stones -= 1
                if self.Mancala.CURRENT_PLAYER == 1:
                    self.Mancala.LANE_PLAYER1[fields] += 1
                else:
                    self.Mancala.LANE_PLAYER2[fields] += 1
        # GET NEXT LANE
        if self.Mancala.CURRENT_PLAYER != 1:
            currlane = 2
        else: currlane = 1

        while stones:
            # GET NEXT LANE
            if currlane == 1:
                currlane = 2
            else: currlane = 1

            # IF DONE WITH CURRENT PLAYERS LANE
            if currlane != self.Mancala.CURRENT_PLAYER:
                self.scoregoal()
                stones -= 1

            # GO THOUGH NEXT LANE
            for fields in range(self.Mancala.BOARD_SIZE):
                if stones > 0:
                    stones -= 1
                    if currlane == 1:
                        self.Mancala.LANE_PLAYER1[fields] += 1
                    else:
                        self.Mancala.LANE_PLAYER2[fields] += 1

        # UPDATE BOARD
        for x in range(self.Mancala.BOARD_SIZE):
            self.buttons1[x].configure(text=self.Mancala.LANE_PLAYER1[x])
            self.buttons2[x].configure(text=self.Mancala.LANE_PLAYER2[self.Mancala.BOARD_SIZE-1-x])
        self.goal1.configure(text="Goal 1: " + str(self.Mancala.GOAL_PLAYER1))
        self.goal2.configure(text="Goal 2: " + str(self.Mancala.GOAL_PLAYER2))
        
        # UPDATES IF PLAYER 1 IS CURRENT PLAYER
        if self.Mancala.CURRENT_PLAYER == 1:
            self.goal1.configure(bg="white")      # REPAINT BOARD
            self.goal2.configure(bg="pink")  # REPAINT BOARD

            for buttons in self.buttons2:
                if buttons["text"] != 0:
                    buttons.configure(state=NORMAL)
            for buttons in self.buttons1:
                buttons.configure(state=DISABLED)

        # UPDATES IF PLAYER 2 IS CURRENT PLAYER
        else:
            self.goal1.configure(bg="lightblue")
            self.goal2.configure(bg="white")
            for buttons in self.buttons1:
                if buttons["text"] != 0:
                    buttons.configure(state=NORMAL)
            for buttons in self.buttons2:
                buttons.configure(state=DISABLED)
    def createboard(self, i, middleframe):
        left = Button(middleframe, text=self.Mancala.LANE_PLAYER1[i], bg="lightblue", height=2,\
                width=10, command=lambda i=i:self.makeMove(i))
        right = Button(middleframe, text=self.Mancala.LANE_PLAYER2[i], bg="pink",\
                state=DISABLED, height=2, width=10, command=lambda i=i: self.makeMove(5-i))
        left.grid(row=i, column=0)
        self.buttons1.append(left)
        right.grid(row=i, column=1)
        self.buttons2.append(right)

    def create_widgets(self):
        #middleframe handles grid for fields
        self.configure(bg="white")
        middleframe = Frame(self)
        middleframe.grid(row=3, column=0, rowspan=3, columnspan=2)
        #create goal for Player1
        self.goal2 = Label(self, text="Goal 2: " + str(self.Mancala.GOAL_PLAYER2), \
                     height=3, width=30, bg="white")
        self.goal2.grid(row=1, column=0, sticky=W+E+N+S)
        for i in range(self.Mancala.BOARD_SIZE):
            self.createboard(i, middleframe)
        #create goal for Player1
        self.goal1 = Label(self, text="Goal 1: " + str(self.Mancala.GOAL_PLAYER1), height=3, bg="lightblue")
        self.goal1.grid(row=7, column=0, sticky=W+E+N+S)

BASE = Tk()
BASE.geometry("210x350+400+400")
APP = Application(master=BASE)
APP.mainloop()