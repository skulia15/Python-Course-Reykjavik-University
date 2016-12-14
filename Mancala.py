from tkinter import *

class Application(Frame):
    class Mancala:
        GOAL_PLAYER1 = 0
        GOAL_PLAYER2 = 0
        BOARD_SIZE = 6
        LANE_PLAYER1 = [4 for i in range(BOARD_SIZE)]
        LANE_PLAYER2 = [4 for i in range(BOARD_SIZE)]
        CURRENT_PLAYER = 2

    buttons1 = []
    buttons2 = []

    def __init__(self, master=None): #MAIN
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def getWhosTurn(self):
        if self.Mancala.CURRENT_PLAYER == 1:
            return 2
        return 1

    def scoregoal(self):
        if self.Mancala.CURRENT_PLAYER == 1:
            self.Mancala.GOAL_PLAYER1 += 1
        else: self.Mancala.GOAL_PLAYER2 += 1

    def makeMove(self, i):
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
                    if currlane == 1:
                        self.Mancala.LANE_PLAYER1[fields] += 1
                    else:
                        self.Mancala.LANE_PLAYER2[fields] += 1


        self.endstuff()
        self.updateboard()



    def endstuff(self):
        # IF EMPTY TAKE SUM OF OPPONENTS BOARD TO OPPONENT
        zeroboard = [0 for i in range(self.Mancala.BOARD_SIZE)]
        if self.Mancala.LANE_PLAYER1 == zeroboard:
            self.Mancala.GOAL_PLAYER2 += sum(self.Mancala.LANE_PLAYER2)
            self.Mancala.LANE_PLAYER2 = zeroboard
        elif self.Mancala.LANE_PLAYER2 == zeroboard:
            self.Mancala.GOAL_PLAYER1 += sum(self.Mancala.LANE_PLAYER1)
            self.Mancala.LANE_PLAYER1 = [0 for i in range(self.Mancala.BOARD_SIZE)]

    def updateboard(self):
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


    def createboard(self, i, middleframe):
        left = Button(middleframe, text=self.Mancala.LANE_PLAYER1[i], bg="lightblue", height=2,\
                width=10, command=lambda i=i:self.makeMove(i))
        right = Button(middleframe, text=self.Mancala.LANE_PLAYER2[i], bg="pink",\
                state=DISABLED, height=2, width=10, command=lambda i=i: self.makeMove(5-i))
        left.grid(row=i, column=0)
        self.buttons1.append(left)
        right.grid(row=i, column=1)
        self.buttons2.append(right)

    def create_everything(self):
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

    def create_widgets(self):
        def openrules():
            print("Rulezzz")
        def start_create_everything():
            start.destroy()
            rules.destroy()
            quitb.destroy()
            self.create_everything()
        start = Button(text="Start", width=30, height=5, command=lambda: start_create_everything())
        rules = Button(text="Rules", width=30, height=5, command=lambda: openrules())
        quitb = Button(text="Exit", width=30, height=5, bg= "red", command=lambda: BASE.destroy())
        start.pack()
        rules.pack()
        quitb.pack()

BASE = Tk()
#BASE.geometry("310x450+500+500")
APP = Application(master=BASE)
APP.mainloop()
