#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 1 00:34:56 2019

@author: ojasbardiya
"""
import Tkinter as Tk # for python 2

class KnightsTourGame:
   def __init__(self, master, side_length):
       self.master = master
       self.side_length = side_length
       self.canvas = Tk.Canvas(master, width=500, height=500) #make constant height and width for canvas
       self.canvas.pack()
       self.canvas.bind("<Button-1>", self.Knight_move)
       self.curr_x, self.curr_y = 0,0
       self.visited = [(self.curr_x, self.curr_y)]
       self.array = []
       for i in range(self.side_length):             #create the chessboard
           self.array.append([])
           for j in range(self.side_length):
               curr_position = self.canvas.create_rectangle(i*500/side_length, j*500/side_length, (500 + 500*i)/side_length, (500 + 500*j)/side_length)
               self.array[i].append(curr_position) #store the current position in the array
       self.canvas.itemconfig(self.array[self.curr_x][self.curr_y], fill="orange")    
   
    
   def Knight_move(self, ev):
       pos_x, pos_y = ev.x // (500/self.side_length), ev.y // (500/self.side_length) #get the position of the click
       if (pos_x, pos_y) in self.all_valid_moves():
           self.canvas.itemconfig(self.array[self.curr_x][self.curr_y], fill="blue") #fill visited squares with blue
           self.curr_x, self.curr_y = pos_x, pos_y
           self.canvas.itemconfig(self.array[self.curr_x][self.curr_y], fill="orange") #current square is orange
           self.visited = set(list(self.visited) + [(pos_x, pos_y)])
           if len(self.visited) == self.side_length*self.side_length: #determine if the game has finished or not
               print "The Knight's tour has been completed!"
           
           
           
   def all_valid_moves(self):
       list_of_possible_moves = [(self.curr_x + 1, self.curr_y + 2),(self.curr_x + 1, self.curr_y - 2), (self.curr_x - 1, self.curr_y + 2), (self.curr_x - 1, self.curr_y - 2), (self.curr_x + 2, self.curr_y + 1), (self.curr_x + 2, self.curr_y - 1), (self.curr_x - 2, self.curr_y + 1), (self.curr_x - 2, self.curr_y - 1)]
       valid_moves = []
       for element in list_of_possible_moves: #select valid moves from possible moves
           if element[0] >= 0 and element[0] < self.side_length and element[1] >= 0 and element[1] < self.side_length:
               valid_moves.append(element)
       return valid_moves 
      
    
        
       
       
if __name__ == "__main__":
    root = Tk.Tk()
    gui=KnightsTourGame(root, 5)
    root.mainloop()
    

       

       
      
       
       