# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 11:09:54 2015

@author: fabiomainardi
"""

from Tkinter import Frame, Canvas, Label, Button, LEFT,RIGHT, ALL, Tk
from random import randint
 
class main:
   
    def __init__(self,master):
        self.frame = Frame(master)
        self.frame.pack(fill="both", expand=True)
        self.canvas = Canvas(self.frame, width=600, height=600)
        self.canvas.pack(fill="both", expand=True)
        self.label=Label(self.frame, text='Tic Tac Toe', height=2, 
                         bg='white', fg='black')
        self.label.pack(fill="both", expand=True)
        self.frameb=Frame(self.frame)
        self.frameb.pack(fill="both", expand=True)
        self.Start2=Button(self.frameb, text='Two players',
                           height=4,command=self.start2,bg='yellow', fg='black')
        self.Start2.pack(fill="both", expand=True, side=RIGHT)
        self.Start1=Button(self.frameb, text='One player',
                           height=4,command=self.start1,bg='yellow', fg='black')
        self.Start1.pack(fill="both", expand=True, side=LEFT)
        self.whichPlayer=1
        self.computerPlays=False
     
      
    
    def start2(self):
        self.computerPlays=False
        self.canvas.delete(ALL)
        #initialize board
        self.board=[[0]*3 for i in range(3)]
        self.canvas.bind("<ButtonPress-1>", self.move)  
        #draw board
        self.drawGrid()
        self.rows=[0,0,0]
        self.cols=[0,0,0]
        self.diag1=0
        self.diag2=0
        self.label['text']='Tic Tac Toe'
        self.turns=1
        
    def start1(self):
        self.whichPlayer=1
        print('you (circle) vs computer (cross)')
        self.computerPlays=True
        self.canvas.delete(ALL)
        #initialize board
        self.board=[[0]*3 for i in range(3)]
        #draw board
        self.drawGrid()
        self.rows=[0,0,0]
        self.cols=[0,0,0]
        self.diag1=0
        self.diag2=0
        self.label['text']='Tic Tac Toe'       
        self.canvas.bind("<ButtonPress-1>", self.move)
        self.turns=1
     
    def computerMove(self):
        posx=randint(0,2)
        posy=randint(0,2)
        if(self.turns>8):
            self.label['text']='Draw!'
            self.endGame()
        #attack
        moved=False
        for i in range(3):
            if(self.rows[i]==-2):
                for j in range(3):
                    if(self.board[i][j]==0):
                        self.drawCross(j,i)
                        self.board[i][j]=-1
                        self.rows[i]-=1
                        self.cols[j]-=1
                        if(i==j):
                            self.diag1-=1
                        if(i+j==2):
                            self.diag2-=1
                        moved=True
        if(moved==False):
            for i in range(3):   
                if(self.cols[i]==-2):
                    for j in range(3):
                        if(self.board[j][i]==0):
                            self.drawCross(i,j)
                            self.board[j][i]=-1
                            self.rows[j]-=1
                            self.cols[i]-=1
                            if(i==j):
                                self.diag1-=1
                            if(i+j==2):
                                self.diag2-=1
                            moved=True
        if(moved==False):
            if(self.diag1==-2):
                for i in range(3):
                   if(self.board[i][i]==0): 
                      self.drawCross(i,i)
                      self.board[i][i]=-1
                      self.rows[i]-=1
                      self.cols[i]-=1
                      if(i==j):
                            self.diag1-=1
                      if(i+j==2):
                            self.diag2-=1
                      moved=True 
        if(moved==False):
            if(self.diag2==-2):
                for i in range(3):
                   if(self.board[i][2-i]==0): 
                      self.drawCross(2-i,i)
                      self.board[i][2-i]=-1
                      self.rows[i]-=1
                      self.cols[2-i]-=1
                      if(i==j):
                            self.diag1-=1
                      if(i+j==2):
                            self.diag2-=1
                      moved=True    
        #defense
        moved=False
        for i in range(3):
            if(self.rows[i]==2):
                for j in range(3):
                    if(self.board[i][j]==0):
                        self.drawCross(j,i)
                        self.board[i][j]=-1
                        self.rows[i]-=1
                        self.cols[j]-=1
                        if(i==j):
                            self.diag1-=1
                        if(i+j==2):
                            self.diag2-=1
                        moved=True
        if(moved==False):
            for i in range(3):   
                if(self.cols[i]==2):
                    for j in range(3):
                        if(self.board[j][i]==0):
                            self.drawCross(i,j)
                            self.board[j][i]=-1
                            self.rows[j]-=1
                            self.cols[i]-=1
                            if(i==j):
                                self.diag1-=1
                            if(i+j==2):
                                self.diag2-=1
                            moved=True
        if(moved==False):
            if(self.diag1==2):
                for i in range(3):
                   if(self.board[i][i]==0): 
                      self.drawCross(i,i)
                      self.board[i][i]=-1
                      self.rows[i]-=1
                      self.cols[i]-=1
                      self.diag1-=1
                      moved=True 
        if(moved==False):
            if(self.diag2==2):
                for i in range(3):
                   if(self.board[i][2-i]==0): 
                      self.drawCross(2-i,i)
                      self.board[i][2-i]=-1
                      self.rows[i]-=1
                      self.cols[2-i]-=1
                      self.diag2-=1
                      moved=True    
        
        if(moved==False):         
            while(self.board[posx][posy]!=0):#random choice
                posx=randint(0,2)
                posy=randint(0,2)
            if(self.board[posx][posy]==0):
                self.board[posx][posy]=-1
                self.rows[posx]-=1
                self.cols[posy]-=1
                if(posx==posy):
                    self.diag1-=1
                if(posx+posy==2):
                    self.diag2-=1
                self.drawCross(posy,posx)
                moved=True
        for i in range(3):
            if(self.rows[i]==-3 or self.cols[i]==-3 or self.diag1==-3 or self.diag2==-3):
                self.label['text']=('Computer wins!')
                self.endGame()
        self.whichPlayer=1
        self.turns+=1

        
                        
    def drawCross(self,row,col):
        lon=100
        offset=50
        self.canvas.create_line(row*200+offset, col*200+offset, 
                                                    row*200+offset+lon, 
                                                    col*200+offset+lon, 
                                                    width=4, fill="red")
        self.canvas.create_line(row*200+offset+lon, col*200+offset,
                                                    row*200+offset, 
                                                    col*200+offset+lon,
                                                    width=4, fill="red")
                    
    def drawGrid(self):
        self.canvas.create_rectangle(0,0,600,600, outline="black")
        self.canvas.create_rectangle(200,600,400,0, outline="black")
        self.canvas.create_rectangle(0,200,600,400, outline="black")
        
    def move(self,event):
        
        X=event.x/200
        Y=event.y/200
        cell=[X,Y]
        if(self.board[cell[1]][cell[0]]==0):
            if(self.whichPlayer==1):
                self.board[cell[1]][cell[0]]+=1
                self.rows[cell[1]]+=1
                self.cols[cell[0]]+=1
                if(cell[1]==cell[0]):
                    self.diag1+=1
                if(cell[1]+cell[0]==2):
                    self.diag2+=1    
                self.whichPlayer=2
                self.canvas.create_oval(X*200+150, Y*200+150, X*200+50, Y*200+50,
                                        width=4, outline="blue")
                if(self.computerPlays==True and self.turns<9):
                    self.computerMove()
            else:
                self.board[cell[1]][cell[0]]-=1
                self.rows[cell[1]]-=1
                self.cols[cell[0]]-=1
                if(cell[1]==cell[0]):
                    self.diag1-=1
                if(cell[1]+cell[0]==2):
                    self.diag2-=1 
                self.whichPlayer=1
                self.drawCross(X,Y)
 
        for i in range(3):
            if(self.rows[i]==3 or self.cols[i]==3 or self.diag1==3 or self.diag2==3):
                self.label['text']=('1st player wins!')
                self.endGame()
        for i in range(3):
            if(self.rows[i]==-3 or self.cols[i]==-3 or self.diag1==-3 or self.diag2==-3):
                self.label['text']=('2nd player wins!')
                self.endGame()
        if(self.turns>=9):
            self.label['text']='Draw!'
            self.endGame()
        self.turns+=1
        print(self.turns)
       
            
    def endGame(self):
        print('END GAME')
        self.canvas.unbind("<ButtonPress-1>")
        
    
root=Tk()
app=main(root)
root.mainloop()