import numpy as np

#Pawn Sacrifice!!!!
def return_curr_position(unit):
    l = np.argwhere(chess==int(unit))
    l_new = l.flatten()
    return l_new


def pawn_move(x,y,unit,i,j):
    #print("Hello Pawn!")
    #print("Cf value:",cf)
    t=return_curr_position(unit)
    curr_pos_x = int(t[0])
    curr_pos_y = int(t[1])
    #print("X value=",x,"Y value=",y)
    #print("Current position:",curr_pos_x,' ',curr_pos_y)
    if x==int(curr_pos_x) and y==int(curr_pos_y):
        p_array[i][j]=0
    elif int(chess[x][y]) == 0:
        #unit 
        if int(curr_pos_x) == x-1 and int(curr_pos_y) == y:
            p_array[i][j]=1

            #print("Hello!")
        else:
            p_array[i][j]=0
    #Friend condition
    elif int(chess[x][y]) in [71,72,73,74,75,76,77,78,121,131,141,15,16,122,132,142]:
        p_array[i][j]=0
    else:
        #attack pawn move
        #if enemy present
        if x-1 == int(curr_pos_x):
            if y-1 == int(curr_pos_y) or y+1 == int(curr_pos_y):
                p_array[i][j]=1
                #print("Hello!")
            else:
                p_array[i][j]=0
        else:
            p_array[i][j]=0
            
            
def rook_move(x,y,unit,i,j):
    #print("Hello Rook!")
    #print("Cf value:",cf)
    t=return_curr_position(unit)
    curr_pos_x = int(t[0])
    curr_pos_y = int(t[1])
    #print("X value=",x,"Y value=",y)
    #print("Current position:",curr_pos_x,' ',curr_pos_y)
    if x==int(curr_pos_x) and y==int(curr_pos_y):
        p_array[i][j]=0
    #Friend condition
    elif int(chess[x][y]) in [71,72,73,74,75,76,77,78,121,131,141,15,16,122,132,142]:
        p_array[i][j]=0
    else:
        #rook move
        if x == int(curr_pos_x):
            p_array[i][j]=1
            for k in range(curr_pos_y+1,y):
                if chess[x][k]!=0:
                    p_array[i][j]=0
                    break
        elif y==int(curr_pos_y):
            p_array[i][j]=1
            for k in range(curr_pos_x+1,x):
                if chess[k][y]!=0:
                    p_array[i][j]=0
                    break
        else:
            p_array[i][j]=0
          
            
def knight_move(x,y,unit,i,j):
    #print("Hello Knight!")
    #print("Cf value:",cf)
    t=return_curr_position(unit)
    curr_pos_x = int(t[0])
    curr_pos_y = int(t[1])
    #print("X value=",x,"Y value=",y)
    #print("Current position:",curr_pos_x,' ',curr_pos_y)
    if x==int(curr_pos_x) and y==int(curr_pos_y):
        p_array[i][j]=0
    #Friend condition
    elif int(chess[x][y]) in [71,72,73,74,75,76,77,78,121,131,141,15,16,122,132,142]:
        p_array[i][j]=0
    else:
        #attack rook move
        #if enemy present
        if int(curr_pos_x) == x+1 and int(curr_pos_y) == y+2:
            p_array[i][j]=1
        elif int(curr_pos_x) == x-1 and int(curr_pos_y) == y+2:
            p_array[i][j]=1
            
        elif int(curr_pos_x) == x-2 and int(curr_pos_y) == y+1:
            p_array[i][j]=1
        
        elif int(curr_pos_x) == x-2 and int(curr_pos_y) == y-1:
            p_array[i][j]=1
        elif int(curr_pos_x) == x-1 and int(curr_pos_y) == y-2:
            p_array[i][j]=1

        elif int(curr_pos_x) == x+1 and int(curr_pos_y) == y-2:
            p_array[i][j]=1

        elif int(curr_pos_x) == x+2 and int(curr_pos_y) == y-1:
            p_array[i][j]=1
        
        elif int(curr_pos_x) == x-2 and int(curr_pos_y) == y+1:
            p_array[i][j]=1
    
        else:
            p_array[i][j]=0
            
def bishop_move(x,y,unit,i,j):
    #print("Hello Bishop!")
    #print("Cf value:",cf)
    t=return_curr_position(unit)
    curr_pos_x = int(t[0])
    curr_pos_y = int(t[1])
    #print("X value=",x,"Y value=",y)
    #print("Current position:",curr_pos_x,' ',curr_pos_y)
    if x==int(curr_pos_x) and y==int(curr_pos_y):
        p_array[i][j]=0
             
    #Friend condition
    elif int(chess[x][y]) in [71,72,73,74,75,76,77,78,121,131,141,15,16,122,132,142]:
        p_array[i][j]=0
    else:
        #unit 
        #flag=0      #there is no obstacle
        r=1
        #4 directions
        #north-east direction
        new_pos_x=int(curr_pos_x)
        new_pos_y=int(curr_pos_y)
        while new_pos_x < 8 or new_pos_y > 0:
            if int(new_pos_x) == x:
                if int(new_pos_y)==y:
                    p_array[i][j]=1
                    break
            elif int(new_pos_y) == y:
                if int(new_pos_x)==x:
                    p_array[i][j]=1
                    break  
            new_pos_x=new_pos_x+r
            new_pos_y=new_pos_y-r
            if chess[new_pos_x][new_pos_y]!=0:
                p_array[i][j]=0
                break
                
        #south-east direction
        r=1
        new_pos_x=int(curr_pos_x)
        new_pos_y=int(curr_pos_y)
        while curr_pos_x+r < 8 or curr_pos_y+r < 8:
            if int(new_pos_x) == x:
                if int(new_pos_y)==y:
                    p_array[i][j]=1
                    break
            elif int(new_pos_y) == y:
                if int(new_pos_x)==x:
                    p_array[i][j]=1
                    break
            
            new_pos_x=new_pos_x+r
            new_pos_y=new_pos_y+r
            if chess[new_pos_x][new_pos_y]!=0:
                p_array[i][j]=0
                break
                
        #south-west direction
        r=1
        new_pos_x=int(curr_pos_x)
        new_pos_y=int(curr_pos_y)
        while new_pos_x > 0 or new_pos_y < 8:
            if int(new_pos_x) == x:
                if int(new_pos_y)==y:
                    p_array[i][j]=1
                    break
            elif int(new_pos_y) == y:
                if int(new_pos_x)==x:
                    p_array[i][j]=1
                    break
            new_pos_x=new_pos_x-r
            new_pos_y=new_pos_y+r
            if chess[new_pos_x][new_pos_y]!=0:
                p_array[i][j]=0
                break
        #north-west direction
        r=1
        new_pos_x=int(curr_pos_x)
        new_pos_y=int(curr_pos_y)
        while curr_pos_x-r > 0 or curr_pos_y-r > 0:
            if int(new_pos_x) == x:
                if int(new_pos_y)==y:
                    p_array[i][j]=1
                    break
            elif int(new_pos_y) == y:
                if int(new_pos_x)==x:
                    p_array[i][j]=1
                    break
            new_pos_x=new_pos_x-r
            new_pos_y=new_pos_y-r
            if chess[new_pos_x][new_pos_y]!=0:
                p_array[i][j]=0
                break
                
def king_move(x,y,unit,i,j):
    #print("Hello King!")
    #print("Cf value:",cf)
    t=return_curr_position(unit)
    curr_pos_x = int(t[0])
    curr_pos_y = int(t[1])
    #print("X value=",x,"Y value=",y)
    #print("Current position:",curr_pos_x,' ',curr_pos_y)
    if x==int(curr_pos_x) and y==int(curr_pos_y):
        p_array[i][j]=0
                    
    #Friend condition
    elif int(chess[x][y]) in [71,72,73,74,75,76,77,78,121,131,141,15,16,122,132,142]:
        p_array[i][j]=0
    else:
        #attack king move
        #if enemy present
        if int(curr_pos_x)==x-1 and int(curr_pos_y) == y+1:
            p_array[i][j]=1
        elif int(curr_pos_x)==x-1 and int(curr_pos_y) == y:
            p_array[i][j]=1
        elif int(curr_pos_x)==x-1 and int(curr_pos_y) == y-1:
            p_array[i][j]=1
        elif int(curr_pos_x)==x and int(curr_pos_y) == y-1:
            p_array[i][j]=1
        elif int(curr_pos_x)==x+1 and int(curr_pos_y) == y-1:
            p_array[i][j]=1
        elif int(curr_pos_x)==x+1 and int(curr_pos_y) == y:
            p_array[i][j]=1
        elif int(curr_pos_x)==x-1 and int(curr_pos_y) == y-1:
            p_array[i][j]=1
        elif int(curr_pos_x)==x+1 and int(curr_pos_y) == y+1:
            p_array[i][j]=1
        elif int(curr_pos_x)==x and int(curr_pos_y) == y+1:
            p_array[i][j]=1
        else:
            p_array[i][j]=0

def queen_move(x,y,unit,i,j):
    #print("Hello Queen!")
    #print("Cf value:", cf)
    t=return_curr_position(unit)
    curr_pos_x = int(t[0])
    curr_pos_y = int(t[1])
    #print("X value=",x,"Y value=",y)
    #print("Current position:",curr_pos_x,' ',curr_pos_y)
    if x==int(curr_pos_x) and y==int(curr_pos_y):
        p_array[i][j]=0
                    
    #Friend condition
    elif int(chess[x][y]) in [71,72,73,74,75,76,77,78,121,131,141,15,16,122,132,142]:
        p_array[i][j]=0
    else:
        #bishop move
                #unit 
        #flag=0      #there is no obstacle
        r=1
        #4 directions
        #north-east direction
        new_pos_x=int(curr_pos_x)
        new_pos_y=int(curr_pos_y)
        while new_pos_x < 8 or new_pos_y > 0:
            if int(new_pos_x) == x:
                if int(new_pos_y)==y:
                    p_array[i][j]=1
                    break
            elif int(new_pos_y) == y:
                if int(new_pos_x)==x:
                    p_array[i][j]=1
                    break    
            new_pos_x=new_pos_x+r
            new_pos_y=new_pos_y-r
            if chess[new_pos_x][new_pos_y]!=0:
                p_array[i][j]=0
                break
                
        #south-east direction
        r=1
        new_pos_x=int(curr_pos_x)
        new_pos_y=int(curr_pos_y)
        while curr_pos_x+r < 8 or curr_pos_y+r < 8:
            if int(new_pos_x) == x:
                if int(new_pos_y)==y:
                    p_array[i][j]=1
                    break
            elif int(new_pos_y) == y:
                if int(new_pos_x)==x:
                    p_array[i][j]=1
                    break
            new_pos_x=new_pos_x+r
            new_pos_y=new_pos_y+r
            if chess[new_pos_x][new_pos_y]!=0:
                p_array[i][j]=0
                break
                
        #south-west direction
        r=1
        new_pos_x=int(curr_pos_x)
        new_pos_y=int(curr_pos_y)
        while new_pos_x > 0 or new_pos_y < 8:
            if int(new_pos_x) == x:
                if int(new_pos_y)==y:
                    p_array[i][j]=1
                    break
            elif int(new_pos_y) == y:
                if int(new_pos_x)==x:
                    p_array[i][j]=1
                    break
            new_pos_x=new_pos_x-r
            new_pos_y=new_pos_y+r
            if chess[new_pos_x][new_pos_y]!=0:
                p_array[i][j]=0
                break
        #north-west direction
        r=1
        new_pos_x=int(curr_pos_x)
        new_pos_y=int(curr_pos_y)
        while curr_pos_x-r > 0 or curr_pos_y-r > 0:
            if int(new_pos_x) == x:
                if int(new_pos_y)==y:
                    p_array[i][j]=1
                    break
            elif int(new_pos_y) == y:
                if int(new_pos_x)==x:
                    p_array[i][j]=1
                    break
            new_pos_x=new_pos_x-r
            new_pos_y=new_pos_y-r
            if chess[new_pos_x][new_pos_y]!=0:
                p_array[i][j]=0
                break
                
        if x == int(curr_pos_x):
            p_array[i][j]=1
            for k in range(curr_pos_y+1,y):
                if chess[x][k]!=0:
                    p_array[i][j]=0
                    break
        elif y==int(curr_pos_y):
            p_array[i][j]=1
            for k in range(curr_pos_x+1,x):
                if chess[k][y]!=0:
                    p_array[i][j]=0
                    break
        else:
            p_array[i][j]=0
        
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


print("------------------Welcome to Pawn Sacrifice!!!----------------")
print('')
print("This is a game where the probabilities of oppponents units are displayed at a particular state of the game.")
print('')
print('')
print("--------------------RULES-------------------")
print("1.You will be playing as white and opponent will be black")
print("2.Standard Chess rules ")
print("3.r1,r2,R1,R2 represent the rook units with capital letter for black side")
print("4.Similiarly for every unit......")
print("5.White has to play first and the probability for black will be printed")
print('')
print('')


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

print("---------The chessboard-----")
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in chess_board]))
        

print('')
print("Whites move:")
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

l = np.argwhere(chess==int(n_unit))
l_new = l.flatten()
x1=l_new[0]
x2=l_new[1]
a=int(a)
b=int(b)
chess[x1][x2]=0
chess[a][b]=n_unit
chess_board[x1+1][x2+1]="_"
chess_board[a+1][b+1]=unit

print("---------The chessboard-----")
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in chess_board]))


#generating random matrix of x,y values for black

out_arr = np.random.randint(0,8,(16,1000,2))
#print(out_arr)
p_array=np.zeros([1000,16],dtype = int) 
#print(p_array)
sum_array = np.zeros(16,dtype=int)
avg_array = np.zeros(16,dtype=int)
perc_array = np.zeros(16,dtype=float)
#print(avg_array)

#conditions
i=-1 #counter for sum_array
j=-1 # counter for unit array

for arr in out_arr:
    j=j+1
    i=-1
    #print(arr)
    for m in arr:
        i=i + 1    
        x=int(m[0])
        y=int(m[1])
        if j in [0,1,2,3,4,5,6,7]:
            #pawn unit
            new_unit=71+j
            #print("-------------------------Pawn-------------------------------- ")
            pawn_move(x,y,new_unit,i,j)
        elif j==8 or j==15:
            #rook unit
            if j==8:
                new_unit=121
            else:
                new_unit=122
            #print("-------------------------Rook-------------------------------- ")
            rook_move(x,y,new_unit,i,j)
        elif j==9 or j==14:
            #knight unit
            if j==9:
                new_unit=131
            else:
                new_unit=132
            #print("-------------------------Knight-------------------------------- ")
            knight_move(x,y,new_unit,i,j)
        elif j==10 or j==13:
            #Bishop unit
            if j==10:
                new_unit=141
            else:
                new_unit=142
            #print("-------------------------Bishop-------------------------------- ")
            bishop_move(x,y,new_unit,i,j)
            
        elif j==11:
            #King unit
            new_unit=15
            #print("-------------------------King-------------------------------- ")
            king_move(x,y,new_unit,i,j)
        elif j==12:
            #Queen unit
            new_unit=16
            #print("-------------------------Queen-------------------------------- ")
            queen_move(x,y,new_unit,i,j)
        
#Summation of p_array

for i in range(0,16):
    for j in range(0,1000):
        sum_array[i]=sum_array[i]+p_array[j][i]


for i in range(0,16):
    perc_array[i]=sum_array[i]/5

#print(sum_array)
#print(perc_array)
#print(p_array)
        
        #print("x value:",x)
        #print("y value:",y)
print('')
print('')
print('')
        
print("The probability that the opponent will choose a particular unit to move:")
print("Pawn P1:",perc_array[0],'%')
print("Pawn P2:",perc_array[1],'%')
print("Pawn P3:",perc_array[2],'%')
print("Pawn P4:",perc_array[3],'%')
print("Pawn P5:",perc_array[4],'%')
print("Pawn P6:",perc_array[5],'%')
print("Pawn P7:",perc_array[6],'%')
print("Pawn P8:",perc_array[7],'%')
print("Rook R1:",perc_array[8],'%')
print("Knight K1:",perc_array[9],'%')
print("Bishop B1:",perc_array[10],'%')
print("King K:",perc_array[11],'%')
print("Queen Q:",perc_array[12],'%')
print("Bishop B2:",perc_array[13],'%')
print("Knight K2:",perc_array[14],'%')
print("Rook R2:",perc_array[15],'%')


        

