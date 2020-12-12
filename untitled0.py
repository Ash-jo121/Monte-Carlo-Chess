# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 21:51:25 2020

@author: Ashish
"""

import numpy as np


chess=np.array([
    [121,0,141,15,16,0,132,122],
    [0,72,73,74,0,76,77,78],
    [71,0,131,0,0,0,0,0],
    [0,0,142,0,75,0,0,0],
    [42,0,0,0,15,0,0,0],
    [0,0,0,0,0,32,0,0],
    [11,12,13,14,0,16,17,18],
    [21,31,41,5,6,0,0,22]
    ])
chess_board=np.array([
    ["/-","0","1","2","3","4","5","6","7"],
    ["0","hi","hi","hi","hi","hi","hi","hi","hi"],
    ["1","","","","","","","",""],
    ["2","","","","","","","",""],
    ["3","","","","","","","",""],
    ["4","","","","","","","",""],
    ["5","","","","","","","",""],
    ["6","","","","","","","",""],
    ["7","","","","","","","",""]
    ],dtype=str)

for i in range(0,8):
    for j in range(0,8):
        if chess[i][j]==121:
            chess_board[i+1][j+1]='R'+str(int(chess[i][j])-120)
        elif chess[i][j]==122:
            chess_board[i+1][j+1]='R'+str(chess[i][j]-120)
        elif chess[i][j]==131 or chess[i][j]==132:
            chess_board[i+1][j+1]='K'+str(chess[i][j]-130)
        elif chess[i][j]==141 or chess[i][j]==142:
            chess_board[i+1][j+1]='B'+str(chess[i][j]-140)
        elif chess[i][j]==15:
            chess_board[i+1][j+1]='K'
        elif chess[i][j]==16:
            chess_board[i+1][j+1]='Q'
        elif chess[i][j]==0:
            chess_board[i+1][j+1]='_'
        elif chess[i][j]==21 or chess[i][j]==22:
            chess_board[i+1][j+1]='r'+str(chess[i][j]-20)
        elif chess[i][j]==31 or chess[i][j]==32:
            chess_board[i+1][j+1]='k'+str(chess[i][j]-30)
        elif chess[i][j]==41 or chess[i][j]==42:
            chess_board[i+1][j+1]='b'+str(chess[i][j]-40)
        elif chess[i][j]==5:
            chess_board[i+1][j+1]='k'
        elif chess[i][j]==6:
            chess_board[i+1][j+1]='q'
        elif chess[i][j] in [71,72,73,74,75,76,77,78]:
            chess_board[i+1][j+1]='p'+str(chess[i][j]-70)
        elif chess[i][j] in [11,12,13,14,15,16,17,18]:
            chess_board[i+1][j+1]='p'+str(chess[i][j]-10)


print("Enter input as unit x y:")
unit,a,b=input().split()
#print(l_new)

#Checking portion to be updated
if unit=="r1":
    n_unit=21
elif unit=="r2":
    n_unit=22
elif unit=="k1":
    n_unit=31
elif unit=="k2":
    n_unit=32
elif unit=="b1":
    n_unit=41
elif unit=="b2":
    n_unit=42
elif unit=="k":
    n_unit=5
elif unit=="q":
    n_unit=6
elif unit=="p1":
    n_unit=11
elif unit=="p2":
    n_unit=12
elif unit=="p3":
    n_unit=13
elif unit=="p4":
    n_unit=14
elif unit=="p5":
    n_unit=15
elif unit=="p6":
    n_unit=16
elif unit=="p7":
    n_unit=17
elif unit=="p8":
    n_unit=18

print(n_unit)
a=int(a)
b=int(b)
print(a)
print(b)
print(chess[a][b])