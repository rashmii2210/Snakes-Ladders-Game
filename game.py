from pygame import mixer
mixer.init()
mixer.music.load('sky1.mp3')
mixer.music.play()
import mysql.connector
# global mydb
# mydb=mysql.connector.connect(host='localhost',user='root',password='2210',database='rashmi')
import tkinter as tk
from PIL import ImageTk,Image
import random

def start_game() :  

    global im
    global b1,b2

    # buttons for players

    # button for player 1
    # b1= tk.Button(root,text="Player-1",height=3 , width=20, fg="Red",bg="cyan", font=('Cursive',14,'bold'),activebackground='blue',command=roll_dice )
    b1.place(x=1200,y=400)

    # button for player 2
    # b2= tk.Button(root,text="Player-2",height=3 , width=20, fg="Red",bg="orange", font=('Cursive',14,'bold'),activebackground='red',command=roll_dice )
    b2.place(x=1200,y=550)



    # dice image to show
    im= Image.open("roll.jpg")
    im= im.resize((70,70))
    im= ImageTk.PhotoImage(im)
    b4= tk.Button(root,image=im,height=80, width=80)
    b4.place(x=1250,y=200)

    # exit button
    b3= tk.Button(root,text="Click here to End the Game",height=3 , width=20, fg="Red",bg="yellow", font=('Cursive',14,'bold'),activebackground='red',command=root.destroy )
    b3.place(x=1200,y=20)
# --------------------------------------------------------------------------------------------------------

def reset_coin() :

    global player_1,player_2
    global pos1,pos2

    player_1.place(x=0,y=700)
    player_2.place(x=50,y=700)

    pos1=0
    pos2=0


# -------------------------------------------------------------------------------------------------------------
def load_dice_images():
    global Dice
    names=["1.png","2.png","3.png","4.png","5.png","6.png"]
    for nam in names:
        im= Image.open(nam)
        im= im.resize((70,70))
        im= ImageTk.PhotoImage(im)
        Dice.append(im)

# ------------------------------------------------------------------------------------------------------------

def check_Ladder(Turn):
    global pos1,pos2
    global Ladder

    f=0  #no ladder
    if Turn==1:
        if pos1 in Ladder:
            pos1=Ladder[pos1]
            f=1
    else:
        if pos2 in Ladder:
            pos2=Ladder[pos2]
            f=1
    return f

# ------------------------------------------------------

def check_snack(Turn):
    global pos2,pos1
    global Snack

    if Turn==1:
        if pos1 in Snack:
            pos1=Snack[pos1]  #changing position to tail
    else:
        if pos2 in Snack:
            pos2=Snack[pos2]


def roll_dice() :

    global Dice
    global turn
    global pos1,pos2
    global b2,b1
    r= random.randint(1,6)
    
    b4= tk.Button(root,image=Dice[r-1],height=80, width=80)
    b4.place(x=1250,y=200)

    lad=0 #no ladder
    if turn==1:  
        if (pos1+r)<=100:
            pos1=pos1+r
        lad=check_Ladder(turn)
        check_snack(turn)
        move_coin(turn,pos1)
        if r!=6 and lad!=1:
            turn=2
            b1.configure(state='disabled')
            b2.configure(state='normal')
    else:
        if (pos2+r)<=100:
            pos2=pos2+r
        lad=check_Ladder(turn)
        check_snack(turn)
        move_coin(turn,pos2)
        if r!=6 and lad!=1:
            turn=1
            b2.configure(state='disabled')
            b1.configure(state='normal')

    is_winner()          

def is_winner():
    global pos1,pos2
    if pos1==100:
        print(p1name," is the WINNER!!")
        msg=" is the Winner"
        Lab=tk.Label(root,text= p1name+msg,height=2,width=20,bg='red',font=('Cursive',30,'bold'))
        Lab.place(x=300,y=300)
        reset_coin()
        # cur=mydb.cursor()
        # s1="insert into winner(name,coin) values(%s,%s)"
        # a1 = (p1name,100)
        # cur.execute(s1,a1)
        # mydb.commit()
        
        

    elif pos2==100:
        print(TerminalColors.MAGENTA,p2name," is the WINNER!!")
        msg=" is the Winner"
        Lab=tk.Label(root,text=p2name+msg,height=2,width=20,bg='red',font=('Cursive',30,'bold'))
        Lab.place(x=300,y=300)
        reset_coin()
        # cur=mydb.cursor()
        # s1="insert into winner(name,coin) values(%s,%s)"
        # a1 = (p2name,100)
        # cur.execute(s1,a1)
        # mydb.commit()
        
# --------------------------------------------


def move_coin(Turn,r):
    global player_1,player_2
    global Index

    if Turn==1:
        player_1.place(x=Index[r][0],y=Index[r][1])
    else:
        player_2.place(x=Index[r][0],y=Index[r][1])



# ----------------------------------------------------------------------------------
def get_index():

    global player_1,player_2
    Num=[100,99,98,97,96,95,94,93,92,91,81,82,83,84,85,86,87,88,89,90,80,79,78,77,76,75,74,73,72,71,61,62,63,64,65,66,67,68,69,70,60,59,58,57,56,55,54,53,52,51,41,42,43,44,45,46,47,48,49,50,40,39,38,37,36,35,34,33,32,31,21,22,23,24,25,26,27,28,29,30,20,19,18,17,16,15,14,13,12,11,1,2,3,4,5,6,7,8,9,10]
    
    # player_1.place(x=30,y=40)
    # player_2.place(x=30,y=180)
    
    row=40
    i=0
    for x in range(1,11):
        col=30
        for y in range(1,11):
            Index[Num[i]]=(col,row)
            col = col +90
            i=i+1
        row=row+70
    # print(Index)
class TerminalColors:
    RED = '\033[91m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'


print(TerminalColors.YELLOW,"\n\n\n\t********************************SNACK AND LADDER GAME*******************************************")
global p1name
global p2name
print(TerminalColors.BLUE,"\nEnter Player-1 Name:")
p1name=input()
print(TerminalColors.BLUE,"Enter Player-2 Name:")
p2name=input()


root = tk.Tk()

root.geometry("1200x800")
root.title("Snack And leader Game")

# tk.Button(text="Start Game",command=getval).grid()

F1 = tk.Frame(root,width=1200,height=800,relief='raised')
F1.place(x=0,y=0)


#  to store dice images
Dice=[]

# To store x & y co-ordinates of given number
Index={}

# Initial position of players
pos1=None
pos2=None

# Ladder bottom to top
Ladder={8:29,19:57,26:45,46:97,50:69,60:79,73:92}

# Snack Head to Tail
Snack = {99:43,94:66,85:55,70:13,63:25,48:6,39:3} 

# Set board 
img = Image.open("board.jpg")
# img = img.resize((1200,800))

img1 = ImageTk.PhotoImage(img)
Lab = tk.Label(F1,image=img1) 
Lab.place(x=0,y=0)
 
#player 1 - button
b1= tk.Button(root,text=p1name,height=3 , width=20, fg="Red",bg="cyan", font=('Cursive',14,'bold'),activebackground='blue',command=roll_dice )


#player 2 - button
b2= tk.Button(root,text=p2name,height=3 , width=20, fg="Red",bg="orange", font=('Cursive',14,'bold'),activebackground='red',command=roll_dice )


# player 1 coin
player_1 = tk.Canvas(root,width=30,height=30)
player_1.create_oval(10,10,30,30,fill='blue')
# player_1.place(x=120,y=740)

# player 2 coin
player_2 = tk.Canvas(root,width=30,height=30)
player_2.create_oval(10,10,30,30,fill='red')
# player_2.place(x=70,y=740)

# whose turn first by default player-1
turn = 1

# keep coins at intial position
reset_coin()

# get index of each NUM
get_index()

# load_dice_images
load_dice_images()

# setting all the buttons
mixer.music.play()
start_game()

root.mainloop()