#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eitan Cohen
#
# Created:     28/06/2013
# Copyright:   (c) Eitan 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random
import time
import timeit
from colorama import init
init()

from colorama import Fore, Back, Style


debug = 10 # type one (" 1 " ) for debug ("10" For speed) ("4" for input) ("7" is timer!)
# "0" for Normal Run


############## FOR DEBUG 7 ###############################
Counter = 1 # "1" for a counter Need to have with Debug 7

avg_time = .35 # averge time for User to solve cube (SPEED CHALLENGE)
start = 0
elapsed_time = 0 # for Timing
delayt = (avg_time+1/202)
#########################################################

moves_inputted=[]
new_move_input = []
set_count = 0
counter_check = 4
Start = 0 # Start runn


def Initialize():
    for r in range (54):
        New_Cube[r] = Original_Cube[r] # to not lose Cube Positions

    for q in range(54):
        To_Change_Cube[q] = New_Cube_Original_Colors[q]

    for t in range(54):
        Changed_Cube[t] = To_Change_Cube[(New_Cube[t])-1]

    for u in range(54):
        Cube[u] = Changed_Cube[u]
    if debug == 0:
        PrintCube(Cube) # ------------------------------------------ This one

    for v in range(54):
        To_Change_Cube[v] = Changed_Cube[v]

def PrintCube_old(a_list):

    return print("\n\n\n\t\t  0   0   0  %r %r %r  0   0   0" %(a_list[0], a_list[1], a_list[2]) ,
           ("\n\t\t  0   0   0  %r %r %r  0   0   0" %(a_list[3], a_list[4], a_list[5] )),
           ("\n\t\t  0   0   0  %r %r %r  0   0   0" %(a_list[6], a_list[7], a_list[8] )),
           ("\n\t\t %r %r %r %r %r %r %r %r %r" %(a_list[9], a_list[10], a_list[11], a_list[18],
           a_list[19], a_list[20], a_list[27], a_list[28], a_list[29] )),
            ("\n\t\t %r %r %r %r %r %r %r %r %r" %(a_list[12], a_list[13], a_list[14], a_list[21],
           a_list[22], a_list[23], a_list[30], a_list[31], a_list[32] )),
           ("\n\t\t %r %r %r %r %r %r %r %r %r" %(a_list[15], a_list[16], a_list[17], a_list[24],
           a_list[25], a_list[26], a_list[33], a_list[34], a_list[35] )),
          ("\n\t\t  0   0   0  %r %r %r  0   0   0" %(a_list[36], a_list[37], a_list[38])) ,
           ("\n\t\t  0   0   0  %r %r %r  0   0   0" %(a_list[39], a_list[40], a_list[41] )),
           ("\n\t\t  0   0   0  %r %r %r  0   0   0" %(a_list[42], a_list[43], a_list[44] )),
           ("\n\t\t  0   0   0  %r %r %r  0   0   0" %(a_list[45], a_list[46], a_list[47])) ,
           ("\n\t\t  0   0   0  %r %r %r  0   0   0" %(a_list[48], a_list[49], a_list[50] )),
           ("\n\t\t  0   0   0  %r %r %r  0   0   0\n\n\n" %(a_list[51], a_list[52], a_list[53] )))





########################
## Function for the PrintCube Function ##
def FUNCT(ch):

    if ch == 'W':
        return Fore.WHITE + 'W'
    elif ch == 'R':
        return Fore.RED + 'R'
    elif ch == 'B':
        return Fore.BLUE + 'B'
    elif ch == 'G':
        return Fore.GREEN + 'G'
    elif ch == 'O':
        return Fore.MAGENTA + 'O'
    elif ch == 'Y':
        return Fore.YELLOW + 'Y'

###########################



def PrintCube(a_list):

    return print(
Fore.RESET + "\n\n\n\t               ",
Fore.RESET, '%s' %FUNCT(a_list[0]),
Fore.RESET, "%s" %FUNCT(a_list[1]),
Fore.RESET, "%s" %FUNCT(a_list[2]),
Fore.RESET + "\n\t               ",
Fore.RESET, "%s" %FUNCT(a_list[3]),
Fore.RESET, "%s" %FUNCT(a_list[4]),
Fore.RESET, "%s" %FUNCT(a_list[5]),
Fore.RESET + "\n\t               ",
Fore.RESET, "%s" %FUNCT(a_list[6]),
Fore.RESET, "%s" %FUNCT(a_list[7]),
Fore.RESET, "%s" %FUNCT(a_list[8]),

# Fourth Row
Fore.RESET,"\n\t      ",
Fore.RESET, "%s"  %FUNCT(a_list[9]),
Fore.RESET, "%s" %FUNCT(a_list[10]),
Fore.RESET, "%s" %FUNCT(a_list[11]),
Fore.RESET, "%s" %FUNCT(a_list[18]),
Fore.RESET, "%s" %FUNCT(a_list[19]),
Fore.RESET, "%s" %FUNCT(a_list[20]),
Fore.RESET, "%s" %FUNCT(a_list[27]),
Fore.RESET, "%s" %FUNCT(a_list[28]),
Fore.RESET, "%s" %FUNCT(a_list[29]),

# Fifth Row
Fore.RESET,"\n\t      ",
Fore.RESET, "%s"  %FUNCT(a_list[12]),
Fore.RESET, "%s" %FUNCT(a_list[13]),
Fore.RESET, "%s" %FUNCT(a_list[14]),
Fore.RESET, "%s" %FUNCT(a_list[21]),
Fore.RESET, "%s" %FUNCT(a_list[22]),
Fore.RESET, "%s" %FUNCT(a_list[23]),
Fore.RESET, "%s" %FUNCT(a_list[30]),
Fore.RESET, "%s" %FUNCT(a_list[31]),
Fore.RESET, "%s" %FUNCT(a_list[32]),

# Sixth Row
Fore.RESET,"\n\t      ",
Fore.RESET, "%s" %FUNCT(a_list[15]),
Fore.RESET, "%s" %FUNCT(a_list[16]),
Fore.RESET, "%s" %FUNCT(a_list[17]),
Fore.RESET, "%s" %FUNCT(a_list[24]),
Fore.RESET, "%s" %FUNCT(a_list[25]),
Fore.RESET, "%s" %FUNCT(a_list[26]),
Fore.RESET, "%s" %FUNCT(a_list[33]),
Fore.RESET, "%s" %FUNCT(a_list[34]),
Fore.RESET, "%s" %FUNCT(a_list[35]),

# Bottom
Fore.RESET + "\n\t               ",
Fore.RESET, '%s' %FUNCT(a_list[36]),
Fore.RESET, "%s" %FUNCT(a_list[37]),
Fore.RESET, "%s" %FUNCT(a_list[38]),
Fore.RESET + "\n\t               ",
Fore.RESET, "%s" %FUNCT(a_list[39]),
Fore.RESET, "%s" %FUNCT(a_list[40]),
Fore.RESET, "%s" %FUNCT(a_list[41]),
Fore.RESET + "\n\t               ",
Fore.RESET, "%s" %FUNCT(a_list[42]),
Fore.RESET, "%s" %FUNCT(a_list[43]),
Fore.RESET, "%s" %FUNCT(a_list[44]),

# Back
Fore.RESET + "\n\t               ",
Fore.RESET, '%s' %FUNCT(a_list[45]),
Fore.RESET, "%s" %FUNCT(a_list[46]),
Fore.RESET, "%s" %FUNCT(a_list[47]),
Fore.RESET + "\n\t               ",
Fore.RESET, "%s" %FUNCT(a_list[48]),
Fore.RESET, "%s" %FUNCT(a_list[49]),
Fore.RESET, "%s" %FUNCT(a_list[50]),
Fore.RESET + "\n\t               ",
Fore.RESET, "%s" %FUNCT(a_list[51]),
Fore.RESET, "%s" %FUNCT(a_list[52]),
Fore.RESET, "%s" %FUNCT(a_list[53]), Fore.RESET,


"\n\n\n")

def Efficient():
    effiency_moves = []
    reduction = 0b0001
    red_rate = "Zero"
    global set_count
    global counter_check

    print("---------------------------------------------------------------------%d" %counter_check)
    counter_check += 1
    for r in range(4):
        effiency_moves.append(moves_inputted[-4+r])
    print("Efficient Move is: %s" %moves_inputted[-1])

    red = effiency_moves[0][0]

    for s in range(3):
        if effiency_moves[s+1][0] == red and (effiency_moves[s+1] != "CCW" or effiency_moves[s+1] != "CW" or effiency_moves[s+1] != "MU" or effiency_moves[s+1] != "MD" ):
            reduction = (reduction*2) + 1
        else:
            reduction = reduction*2

    reduction_bin = bin(reduction)
    if len(moves_inputted[0]) == 1 or moves_inputted[0][0] == "'" :
        if reduction_bin == '0b1100' or reduction_bin == '0b1101':
            red_rate = "Two"
            print("Reduction  = %s -------------------Two" %reduction_bin)
        elif reduction_bin == '0b1110':
            red_rate = "Three"
            print("Reduction  = %s ----------------------------------Three" %reduction_bin)
        elif reduction_bin == '0b1111':
            red_rate = "Four"
            print("Reduction  = %s ----------------------------------------------------Four" %reduction_bin)
        else:
            red_rate = "One"
            print("Reduction  = %s" %reduction_bin)
    else:
        red_rate = "One"
        print("Reduction  = %s" %reduction_bin)

    print("Moves = %s" %effiency_moves)

    set_count += 1

def Move(matrix):
    semi = 1
    naught = 0
    for q in range(53):
        semi = semi + (matrix[q] - 2)
        semi = semi - (2*matrix[q+1])
        semi = semi + matrix[4] - matrix[12] + matrix[18] + matrix[32] - matrix[41] - matrix[51]

   # print("Semi total is: %d" %semi)
    if semi == 1019:
        moves_inputted.append('B')
    elif semi == -3041:
        moves_inputted.append("B\'")
    elif semi == -1665:
        moves_inputted.append("CCW")
    elif semi == 2813:
        moves_inputted.append("CW")
    elif semi == 266:
        moves_inputted.append("C")
    elif semi == -2596:
        moves_inputted.append("C\'")
    elif semi == 107:
        moves_inputted.append("D")
    elif semi == -211:
        moves_inputted.append("D\'")
    elif semi == 213:
        moves_inputted.append("F")
    elif semi == 1:
        moves_inputted.append("F\'")
    elif semi == 3686:
        moves_inputted.append("FU")
    elif semi == -704:
        moves_inputted.append("L")
    elif semi == 3376:
        moves_inputted.append("L\'")
    elif semi == 2280:
        moves_inputted.append("MD")
    elif semi == 849:
        moves_inputted.append("MU")
    elif semi == -749:
        moves_inputted.append("R")
    elif semi == 964:
        moves_inputted.append("R\'")
    elif semi == 2548:
        moves_inputted.append("U")
    elif semi == 614:
        moves_inputted.append("U\'")
    elif semi == 2750:
        moves_inputted.append("UF")
    elif semi == 3881:
        moves_inputted.append("UL")
    elif semi == -1557:
        moves_inputted.append("UR")
    else:
        naught = 1
        #moves_inputted.append("NAUGHT") # Matrix_Naught -> Semi = -105

    #if debug == 3:
    #if naught == 0: #--------- This
     #   print("The move is %s" %moves_inputted[-1]) #----- This
#-----------------------------------------------------------------------
# Need to make this mor efficient

    if debug == 1:
        if len(moves_inputted) >= 4: #---- this one
            Efficient()  #------- this one

    #print("The new Moves are %s" %new_move_input)
#----------------------------------------------------------------------
#- Actual Move code

    for r in range (54):
        New_Cube[r] = Original_Cube[r] # to not lose Cube Positions

   # print("New Cube")
   # PrintCube(New_Cube)

   # print("Original Cube")
   # PrintCube(Original_Cube)

    for s in range (54):
        New_Cube[s] = New_Cube[s] + matrix[s] # Apply Matrix (or Move to (copy) Cube)

  #  print("New Cube w/Matrix Operator")
  #  PrintCube(New_Cube)
   # print(matrix)
  #  print("Cube")
  #  PrintCube(Cube)

    for q in range(54):
        To_Change_Cube[q] = Cube[q]

   # print("Pre-Changed Cube")
   # PrintCube(Changed_Cube)


    for t in range(54):
        Changed_Cube[t] = To_Change_Cube[(New_Cube[t])-1]

    same = 0
    for u in range(54):
        if Cube[u] == Changed_Cube[u]:
            same = same +1
##    if same == 54:
##        print("What Just Happened? Error 100")
##        PrintCube(Cube)   ##### The Naught Move
    else:
        for u in range(54):
            Cube[u] = Changed_Cube[u]
       #if naught == 0: #-------- This
           # PrintCube(Cube) #-------- This

    for v in range(54):

        To_Change_Cube[v] = Changed_Cube[v]


    if debug == 7 and Start == 1:
            time.sleep(delayt)
            if Counter == 1:
                elapsed_time = time.time() - start
                print("The program took %3.3f seconds" %elapsed_time)
                PrintCube(Cube)


def MoveT(move_input): # add a move of F" R" L" B" D" U"
    if (move_input == "U") or (move_input == "u"):
        move = Matrix_Up
    elif move_input == "U'" or move_input == "u'":
        move = Matrix_UpC
    elif move_input == "D" or move_input == "d":
        move = Matrix_Down
    elif move_input == "D'" or move_input == "d'":
        move = Matrix_DownC
    elif move_input == "L" or move_input == "l":
        move = Matrix_Left
    elif move_input == "L'" or move_input == "l'":
        move = Matrix_LeftC
    elif move_input == "R" or move_input == "r":
        move = Matrix_Right
    elif move_input == "R'" or move_input == "r'":
        move = Matrix_RightC
    elif move_input == "B" or move_input == "b":
        move = Matrix_Back
    elif move_input == "B'" or move_input == "b'":
        move = Matrix_BackC
    elif move_input == "F" or move_input == "f":
        move = Matrix_Front
    elif move_input == "F'" or move_input == "f'":
        move = Matrix_FrontC
    elif move_input == "M" or move_input == "m":
        move = Matrix_MiddleD
    elif move_input == "M'" or move_input == "m'":
        move = Matrix_MiddleU
    elif move_input == "C" or move_input == "c'":
        move = Matrix_Center
    elif move_input == "C'" or move_input == "c'":
        move = Matrix_CenterC
    else:
        print("You have typed an invalid Move!!")
        move = [0 for p in range(54)]
    return move


def Scrammble():
    Solution = [0 for i in range(22)]
    sol_move = [0 for i in range(22)]
    x = [0 for i in range(22)]
    #-----------#
    #---- random Number Generator --- #

    Scrammble = ['R\'','D','B','F\'','R\'','D\'','L','F','B','D\'','R\'','R','L\'','D','D','B\'','B\'','L','C','L','D','R']
    random.shuffle(Scrammble)
    for w in range(22):
        x[w] = Scrammble[w]
    #print("Your Scrammble Algorithm is: ")
    #print(Scrammble)

    for e in range(22):
        # You need to do an if No Counter, then Put a Counter.
        Solution[e] = Scrammble[-e-1]

    for q in range(22):
        Move(MoveT(Scrammble.pop(0)))
    if debug == 0 or debug == 7:
        print("\n\nThe Scrammble Algorithm is: %s" %",".join(x)) #------------------------------------ Put Back

    for d in range(22):
        if len(Solution[d]) == 2:
            sol_move[d] = Solution[d].replace("'","")
        elif len(Solution[d]) == 1:
            sol_move[d] =  Solution[d] + "'"

    if debug == 0:
        print("The Solution is:  %s" %",".join(sol_move)) #----------------------- Put Back



def bring_to_front(place):
    if place==1:
        Move(Matrix_Back)
        Move(Matrix_CenterC)
        Move(Matrix_BackC)
    elif place == 3:
        Move(Matrix_Left)
    elif place == 5:
        Move(Matrix_RightC)
    elif place == 7:
        Move(Matrix_Front)
        Move(Matrix_CenterC)
        Move(Matrix_FrontC)
    elif place == 10:
        Move(Matrix_Left)
        Move(Matrix_CenterC)
    elif place == 12 or place == 14:
        Move(Matrix_CenterC)
    elif place == 16 or place ==39:
        Move(Matrix_DownC)
    elif place == 19:
        Move(Matrix_Front)
        Move(Matrix_Front)
    elif place == 28:
        Move(Matrix_RightC)
        Move(Matrix_Center)
        Move(Matrix_Right)
    elif place == 30 or place==32:
        Move(Matrix_Center)
    elif place == 34 or place==41:
        Move(Matrix_Down)
    elif place == 43 or place == 46:
        Move(Matrix_Down)
        Move(Matrix_Down)
    elif place == 48:
        Move(Matrix_CenterC)
        Move(Matrix_CenterC)
    elif place == 50:
        Move(Matrix_Center)
        Move(Matrix_Center)
    elif place == 52:
        Move(Matrix_Back)
        Move(Matrix_Center)
        Move(Matrix_Center)
        Move(Matrix_BackC)
    else:
        Move(Matrix_Naught)

def bring_to_fronttc(place):
    if place==0 or place==51 or place == 9:
        Move(Matrix_Back)
        Move(Matrix_Down)
        Move(Matrix_Down)
        Move(Matrix_BackC)
    elif place==2 or place==53 or place == 29:
        Move(Matrix_BackC)
        Move(Matrix_DownC)
        Move(Matrix_Back)
    elif place==6 or place==18 or place == 11:
        Move(Matrix_Left)
        Move(Matrix_Down)
        Move(Matrix_LeftC)
    elif place==8 or place==20 or place == 27:
        Move(Matrix_RightC)
        Move(Matrix_DownC)
        Move(Matrix_Right)
        Move(Matrix_Down)
    elif place==36 or place==24 or place == 17:
        Move(Matrix_Down)
    elif place==38 or place==26 or place == 33:
        Move(Matrix_Naught)
    elif place==42 or place==45 or place == 15:
        Move(Matrix_Down)
        Move(Matrix_Down)
    elif place==44 or place==47 or place == 35:
        Move(Matrix_DownC)
    else:
        print("THERE IS KINDA A PROBLEMMM *******************************************************************")


def bring_to_frontsl(place):
    if place==34 or place==41 :
        Move(Matrix_DownC)
    elif place==16 or place==39 :
        Move(Matrix_Down)
    elif place == 46 or place == 43:
        Move(Matrix_Down)
        Move(Matrix_Down)
    elif place == 25 or place == 37:
        Move(Matrix_Naught)
    elif place == 21 or place == 14:
        Move(Matrix_Down)
        Move(Matrix_Left)
        Move(Matrix_DownC)
        Move(Matrix_LeftC)
        Move(Matrix_DownC)
        Move(Matrix_FrontC)
        Move(Matrix_Down)
        Move(Matrix_Front) # this is to put in to left on second layer
        Move(Matrix_Down)
        Move(Matrix_Down)
    elif place == 23 or place == 30 :
        Move(Matrix_DownC)
        Move(Matrix_RightC)
        Move(Matrix_Down)
        Move(Matrix_Right)
        Move(Matrix_Down)
        Move(Matrix_Front)
        Move(Matrix_DownC)
        Move(Matrix_FrontC) # this is to put in to right on second layer
        Move(Matrix_Down)
        Move(Matrix_Down)
    elif place == 32 or place == 50:
        Move(Matrix_Center) # Rotate center
        Move(Matrix_DownC)
        Move(Matrix_RightC)
        Move(Matrix_Down)
        Move(Matrix_Right)
        Move(Matrix_Down)
        Move(Matrix_Front)
        Move(Matrix_DownC)
        Move(Matrix_FrontC) # this is to put in to right on second layer
        Move(Matrix_Down)
        Move(Matrix_Down)
        Move(Matrix_CenterC)
    elif place == 48 or place == 12:
        Move(Matrix_CenterC) # rotate Center
        Move(Matrix_Down)
        Move(Matrix_Left)
        Move(Matrix_DownC)
        Move(Matrix_LeftC)
        Move(Matrix_DownC)
        Move(Matrix_FrontC)
        Move(Matrix_Down)
        Move(Matrix_Front) # this is to put in to left on second layer
        Move(Matrix_Down)
        Move(Matrix_Down)
        Move(Matrix_Center)
    else:
        print("THERE IS KINDA A PROBLEMMM *******************************************************************")

def Check_Parity():

    Bool = False
    face_count= 0
    Check = ['W', 'B', 'R', 'G', 'O', 'Y']
    count = 0

    while face_count < 6 :
        for i in range(54):
            if Cube[i] == Check[0]:
                count += 1

        if count == 9:
            face_count += 1
            Check.pop(0)
            count = 0
        else:
            Bool = False
            break


    if face_count == 6:
        Bool = True

    return Bool



def FURURF():
    Move(Matrix_Front)
    Move(Matrix_Up)
    Move(Matrix_Right)
    Move(Matrix_UpC)
    Move(Matrix_RightC)
    Move(Matrix_FrontC)

def FRURUF():
    Move(Matrix_Front)
    Move(Matrix_Right)
    Move(Matrix_Up)
    Move(Matrix_RightC)
    Move(Matrix_UpC)
    Move(Matrix_FrontC)

def Center_Cross_Alg():
    Move(Matrix_Up)
    Move(Matrix_RightC)
    Move(Matrix_Up)
    Move(Matrix_Up)
    Move(Matrix_Right)
    Move(Matrix_Up)
    Move(Matrix_RightC)
    Move(Matrix_Up)
    Move(Matrix_Right)

def Down_Cross():
    Move(Matrix_RightC)
    Move(Matrix_Up)
    Move(Matrix_Left)
    Move(Matrix_UpC)
    Move(Matrix_Right)
    Move(Matrix_Up)
    Move(Matrix_LeftC)
    Move(Matrix_UpC)

def Cross_Cross():
    Move(Matrix_Up)
    Move(Matrix_Left)
    Move(Matrix_UpC)
    Move(Matrix_RightC)
    Move(Matrix_Up)
    Move(Matrix_LeftC)
    Move(Matrix_UpC)
    Move(Matrix_Right)

def Side_Corner_Flip():
    Move(Matrix_RightC)
    Move(Matrix_Down)
    Move(Matrix_Down)
    Move(Matrix_Right)
    Move(Matrix_Front)
    Move(Matrix_Down)
    Move(Matrix_Down)
    Move(Matrix_FrontC)

def Front_Corner_Flip():
    Move(Matrix_Front)
    Move(Matrix_Down)
    Move(Matrix_Down)
    Move(Matrix_FrontC)
    Move(Matrix_RightC)
    Move(Matrix_Down)
    Move(Matrix_Down)
    Move(Matrix_Right)

def opp(string):
    if len(string) == 2:
            string = string.replace("'","")
    elif len(string) == 1:
            string =  string + "'"

    return string
#--------------------------------------------------------------
string = ""
moves = []

Original_Cube = [0 for i in range(54)]

for d1 in range(54):
    Original_Cube[d1] = d1+1  # give array values of 1 to 54

New_Cube= [0 for i in range(54)]
move = [0 for i in range(54)]
To_Change_Cube= [0 for i in range(54)]
Changed_Cube= [0 for i in range(54)]
Cube = [0 for i in range(54)] # cube that is changing colors



Cube_Original_Colors = [['X','X','X','W','W','W','X','X','X'],
                        ['X','X','X','W','W','W','X','X','X'],
                        ['X','X','X','W','W','W','X','X','X'],
                        ['G','G','G','R','R','R','B','B','B'],
                        ['G','G','G','R','R','R','B','B','B'],
                        ['G','G','G','R','R','R','B','B','B'],
                        ['X','X','X','Y','Y','Y','X','X','X'],
                        ['X','X','X','Y','Y','Y','X','X','X'],
                        ['X','X','X','Y','Y','Y','X','X','X'],
                        ['X','X','X','O','O','O','X','X','X'],
                        ['X','X','X','O','O','O','X','X','X'],
                        ['X','X','X','O','O','O','X','X','X']]

New_Cube_Original_Colors = ['W','W','W','W','W','W','W','W','W','G','G','G',
'G','G','G','G','G','G','R','R','R','R','R','R','R','R','R','B','B','B',
'B','B','B','B','B','B','Y','Y','Y','Y','Y','Y','Y','Y','Y','O','O','O','O','O'
,'O','O','O','O']

#----------------------------------------------------------


Cube_After_UP = [7,4,1,8,5,2,9,6,3,19,20,21,13,14,15,16,17,18,28,29,30,22,23,
24,25,26,27,46,47,48,31,32,33,34,35,36,37,38,39,
40,41,42,43,44,45,46,47,48,49,50,51,10,11,12]

white_look=[0,52,2,10,4,28,6,19,8,9,3,11,48,13,21,15,39,17,18,7,20,14,22,30,24,37,26,27,5,29,23
,31,50,33,41,35,36,25,38,16,40,34,42,46,44,45,43,47,12,49,32,51,1,53]

white_looktc=[51,1,53,3,4,5,18,7,20,0,10,6,12,13,14,42,16,36,11,19,27,21,22,23,17,25,33,8,28,2
,30,31,32,38,34,44,24,37,26,39,40,41,45,43,47,15,46,35,48,49,50,9,52,29]

white_lookytc=[51,1,53,3,4,5,18,7,20,0,10,6,12,13,14,15,16,17,11,19,27,21,22,23,24,25,26,8,28,2
,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,9,52,29]

second_layer_look = [0,1,2,3,4,5,6,7,8,9,10,11,48,13,21,15,39,17,18,19,20,14,22,30,24,37,26,27,28,29,23
,31,50,33,41,35,36,25,38,16,40,34,42,46,44,45,43,47,12,49,32,51,52,53]

#------------------- Matrix Operators ----------------#
#----------------------------------------------------#
#

Matrix_Naught = [0 for r in range(54)]

Matrix_Up = [6,2,-2,4,0,-4,2,-2,-6,9,9,9,0,0,0,0,0,0,9,9,9,0,0,0,0,
0,0,26,24,22,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-40,-42,-44]

Matrix_UpC= [2,4,6,-2,0,2,-6,-4,-2,44,42,40,0,0,0,0,0,0,-9,-9,-9,0,0,0,0,0,0,-9,
-9,-9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-22,-24,-26]

Matrix_Down= [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,32,30,28,0,0,0,0,0,0,-9,-9,-9,0,0,0,0,
0,0,-9,-9,-9,6,2,-2,4,0,-4,2,-2,-6,-10,-12,-14,0,0,0,0,0,0]

Matrix_DownC= [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,9,9,0,0,0,0,0,0,9,9,9,0,0,0,0,0,0,
14,12,10,2,4,6,-2,0,2,-6,-4,-2,-28,-30,-32,0,0,0,0,0,0]

Matrix_Right= [0,0,18,0,0,18,0,0,18,0,0,0,0,0,0,0,0,0,0,0,18,0,0,18,0,0,18,6,2,-2,
4,0,-4,2,-2,-6,0,0,9,0,0,9,0,0,9,0,0,-45,0,0,-45,0,0,-45]

Matrix_RightC=[0,0,45,0,0,45,0,0,45,0,0,0,0,0,0,0,0,0,0,0,-18,0,0,-18,0,0,-18,
2,4,6,-2,0,2,-6,-4,-2,0,0,-18,0,0,-18,0,0,-18,0,0,-9,0,0,-9,0,0,-9]

Matrix_Left = [45,0,0,45,0,0,45,0,0,6,2,-2,4,0,-4,2,-2,-6,-18,0,0,-18,0,0,-18,0,
0,0,0,0,0,0,0,0,0,0,-18,0,0,-18,0,0,-18,0,0,-9,0,0,-9,0,0,-9,0,0]

Matrix_LeftC= [18,0,0,18,0,0,18,0,0,2,4,6,-2,0,2,-6,-4,-2,18,0,0,18,0,0,18,0,0,0,
0,0,0,0,0,0,0,0,9,0,0,9,0,0,9,0,0,-45,0,0,-45,0,0,-45,0,0]

Matrix_Front= [0,0,0,0,0,0,11,7,3,0,0,25,0,0,23,0,0,21,6,2,-2,4,0,-4,2,-2,-6,-21,
0,0,-23,0,0,-25,0,0,-3,-7,-11,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

Matrix_FrontC= [0,0,0,0,0,0,21,23,25,0,0,-3,0,0,-7,0,0,-11,2,4,6,-2,0,2,-6,-4,-2,
11,0,0,7,0,0,3,0,0,-25,-23,-21,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

Matrix_Back = [29,31,33,0,0,0,0,0,0,-7,0,0,-11,0,0,-15,0,0,0,0,0,0,0,0,0,0,0,0,0,
15,0,0,11,0,0,7,0,0,0,0,0,0,-33,-31,-29,6,2,-2,4,0,-4,2,-2,-6]

Matrix_BackC = [15,11,7,0,0,0,0,0,0,33,0,0,31,0,0,29,0,0,0,0,0,0,0,0,0,0,0,0,0,
-29,0,0,-31,0,0,-33,0,0,0,0,0,0,-7,-11,-15,2,4,6,-2,0,2,-6,-4,-2]

Matrix_MiddleD=[0,45,0,0,45,0,0,45,0,0,0,0,0,0,0,0,0,0,0,-18,0,0,-18,0,0,-18,0,
0,0,0,0,0,0,0,0,0,0,-18,0,0,-18,0,0,-18,0,0,-9,0,0,-9,0,0,-9,0]

Matrix_MiddleU=[0,18,0,0,18,0,0,18,0,0,0,0,0,0,0,0,0,0,0,18,0,0,18,0,0,18,0,
0,0,0,0,0,0,0,0,0,0,9,0,0,9,0,0,9,0,0,-45,0,0,-45,0,0,-45,0]

Matrix_Center=[0,0,0,0,0,0,0,0,0,0,0,0,9,9,9,0,0,0,0,0,0,9,9,9,0,0,0,0,0,0,
20,18,16,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-34,-36,-38,0,0,0]

Matrix_CenterC=[0,0,0,0,0,0,0,0,0,0,0,0,38,36,34,0,0,0,0,0,0,-9,-9,-9,0,0,0,0,0,0,
-9,-9,-9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-16,-18,-20,0,0,0]

Matrix_UpFront=[45,45,45,45,45,45,45,45,45,6,2,-2,4,0,-4,2,-2,-6,-18,-18,-18,-18,
-18,-18,-18,-18,-18,2,4,6,-2,0,2,-6,-4,-2,-18,-18,-18,-18,-18,-18,-18,-18,-18,
-9,-9,-9,-9,-9,-9,-9,-9,-9]

Matrix_FrontUp=[18,18,18,18,18,18,18,18,18,2,4,6,-2,0,2,-6,-4,-2,18,18,18,18,18,18,
18,18,18,6,2,-2,4,0,-4,2,-2,-6,9,9,9,9,9,9,9,9,9,-45,-45,-45,-45,-45,-45,-45,-45,-45]

Matrix_UpRight=[15,11,7,13,9,5,11,7,3,33,29,25,31,27,23,29,25,21,6,2,-2,4,0,-4,2,-2,-6,
-21,-25,-29,-23,-27,-31,-25,-29,-33,-3,-7,-11,-5,-9,-13,-7,-11,-15,2,4,6,-2,0,
2,-6,-4,-2]

Matrix_UpLeft= [29,31,33,25,27,29,21,23,25,-7,-5,-3,-11,-9,-7,-15,-13,-11,2,4,
6,-2,0,2,-6,-4,-2,11,13,15,7,9,11,3,5,7,-25,-23,-21,-29,-27,-25,-33,-31,-29,
6,2,-2,4,0,-4,2,-2,-6]

Matrix_CWTwist= [6,2,-2,4,0,-4,2,-2,-6,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,26,24,22,
20,18,16,14,12,10,2,4,6,-2,0,2,-6,-4,-2,-28,-30,-32,-34,-36,-38,-40,-42,-44]

Matrix_CCWTwist= [2,4,6,-2,0,2,-6,-4,-2,44,42,40,38,36,34,32,30,28,-9,-9,-9,
-9,-9,-9,-9,-9,-9,-9,-9,-9,-9,-9,-9,-9,-9,-9,6,2,-2,4,0,-4,2,-2,-6,-10,-12,-14,-16,
-18,-20,-22,-24,-26]


########################
##To_Change_Cube[i] = Cube[i] # Not to lose Cube colors
##New_Cube[i] = New_Cube[i] + Matrix_Up[i] # Apply Matrix (or Move to (copy) Cube)
##Change_Cube[i] = To_Changed_Cube[New_Cube[i]] # move Colors based on index
##Cube[i] = Changed_Cube[i] # New Cube takes colors at positions
##############################
counting = 0
Good_sets = 0
bad = []
bad_set = 0
count_moves = 0


#------ Start Code ------- #
while counting < 100:

    Solution = [0 for q in range(22)]



    Initialize()

    Solution = Scrammble()

    if debug == 7:
        PrintCube(Cube)
        #from timeit import default_timer as time
        while Start == 0:
            Start = int(input("Enter 1 to start "))
    start = time.time()
    if debug == 4: # input test of any cube
        for r in range(54):
            Cube[r] = input("What is the color at %d" %r)

    if debug == 0:
        PrintCube(Cube) # -------------- This one
        print("Cube is Scrammbled. Start Solving Top Layer Cross\n\n") # ---- This one
    ##move_i = input("Which move would you like to do:")
    ##
    ##Move(MoveT(move_i))
    ##moves.append(move_i)
    ##print (moves)
    ##Move(move)
    ##
    ##
    ##while Cube != New_Cube_Original_Colors:
    ##    move_i = input("Which move would you like to do:")
    ##    Move(MoveT(move_i))
    ##
    ##    moves.append(move_i)
    ##    print (moves)
    ##    Move(move)
    ##
    ##
    ##print("YOU SOLVED THE RUBIX CUBE!!!!!!!")





    #------ pseudo code ----- #


    # scrammble the cube using random number generator to spin the cube 20 random moves

    # Turn the cube so that the White Side is ontop
    # find how many whites are on the top - iff there are any on the cross find out which ones there are
    # look for any whites on the bottom layer on the front facing sides ( for centers)
    #   Line up the pieces and put them into the top
    # find the corner pieces
    # do Center Layer
    # do bottom layer








    # ------------- Cube Sides ------------ #

    #--------------------------------(index)-----#
    #   White side = 1 through 9 ( Up ) 4
    #   Green Side = 10 through 18 ( Left ) 13
    #   Red Side = 19 through 27 ( Front ) 22
    #   Blue Side = 28 through 36 ( Right ) 31
    #   Yellow Side = 37 through 45 ( Down ) 40
    #   Orange Side = 46 through 54 ( Back ) 49




    #-----------------------------------------------------

    upcolor = Cube[4]
    frontcolor = Cube[22]
    cube_oriented_up = False


    while cube_oriented_up == False:
        upcolor = Cube[4]
        frontcolor = Cube[22]
        if upcolor == 'W':
            if frontcolor == 'B':
                Move(Matrix_CCWTwist) #Twist Cube CCW
            elif frontcolor == 'G':
                Move(Matrix_CWTwist) #Twist Cube CW
            elif frontcolor == 'O':
                 Move(Matrix_CWTwist) #Twist Cube Twice either direction
            elif frontcolor == 'R':
                cube_oriented_up = True
                #Do nothing....
                # make it so that variable Oriented is High!! (cube_oriented_up =1)
                #( Therefore after Scrammble and any rotation, orient when needed)
        elif upcolor == 'G':
            if frontcolor == 'W':
                Move(Matrix_FrontUp) #Twist FrontUP
            elif frontcolor == 'O':
                Move(Matrix_UpRight) #Twist UpRight
            elif frontcolor == 'Y':
                Move(Matrix_UpFront) #Twist UpFront
            elif frontcolor == 'R':
                Move(Matrix_UpLeft) #Twist UpLeft
        elif upcolor == 'R':
            if frontcolor == 'W':
                Move(Matrix_FrontUp) #Twist FrontUP
            elif frontcolor == 'G':
                Move(Matrix_UpRight) #Twist UpRight
            elif frontcolor == 'Y':
                Move(Matrix_UpFront) #Twist UpFront
            elif frontcolor == 'B':
                Move(Matrix_UpLeft) #Twist UpLeft
        elif upcolor == 'B':
            if frontcolor == 'W':
                Move(Matrix_FrontUp) #Twist FrontUP
            elif frontcolor == 'R':
                Move(Matrix_UpRight) #Twist UpRight
            elif frontcolor == 'Y':
                Move(Matrix_UpFront) #Twist UpFront
            elif frontcolor == 'O':
                Move(Matrix_UpLeft) #Twist UpLeft
        elif upcolor == 'Y':
            Move(Matrix_UpFront)
            #Whatever it is, just spin FrontUp or UpFront
        elif upcolor == 'O':
            if frontcolor == 'W':
                Move(Matrix_FrontUp) #Twist FrontUP
            elif frontcolor == 'B':
                Move(Matrix_UpRight) #Twist UpRight
            elif frontcolor == 'Y':
                Move(Matrix_UpFront) #Twist UpFront
            elif frontcolor == 'G':
                Move(Matrix_UpLeft) #Twist UpLeft
        else:
            print("Error 422")



    #print("1- The Cube is Oriented Up")
    #Start to solve
    #TopLayer_Cross()

    Need = [1,3,5,7] # These are the centers that are being looked for
    search=0 # need to go find piece
    rescue = 0 # means it was found
    to_search = 1
    see_if_it_works = 0
    bool = False

    wwalf=['O','O','G','G','B','B','R','R']


    while len(Need) != 0:
       # print("2- We are looking again *************************************************")
        length_need = len(Need)
        for i in range(1,8,2): #---------------------- Check the top!
           # print("3- Searching the Top Layer")
           # print("4- We are looking at the white piece %d" %i)

            if Cube[i] == 'W':
                for r in range(len(Need)):
                    if Need[r-1] == i:
                       # print("5- we are looking through the cube at piece %d" %i)
                        if i==1 and Cube[52]=='O':
                            Need.remove(1)
                            #print("Need minus 1: %s" %Need)
                        elif i==3 and Cube[10]=='G':
                            Need.remove(3)
                            #print("Need minus 3: %s" %Need)
                        elif i==5 and Cube[28]=='B':
                            Need.remove(5)
                            #print("Need minus 5: %s" %Need)
                        elif i==7 and Cube[19]=='R':
                            Need.remove(7)
                            #print("Need minus 7: %s" %Need)
                        else:
                            #print("Though White, now Search is: %d" %search)
                            search=1
                           # print("Now Search is %d:" %search)
                            to_search = Need[0]

                       # print("6 -Need looks like this: %s" %Need)

    ##            if len(Need)-1==0:
    ##                    if i==7 and Cube[19]=='R':
    ##                        Need.remove(7)
    ##                        print("Need minus 7: %s" %Need)
    ##
    ##                    print("Though White, now Search is: %d" %search)
    ##                    search=1
    ##                    print("Now Search is %d:" %search)
    ##                    to_search = Need[0]




            else:
               # print("6- Search is: %d" %search)
                search=1
               # print("7 -Now Search is %d:" %search)
                to_search = Need[0]

            #print("8 - Looking for piece: %d" %i)


            if search == 1:
                #print("9 -Are we looking for the piece?")
                for i in range(54): # Find the piece and put it in the Front Face
                    if Cube[i]=='W' and i !=4:
                        #print("10 -Looking at: %d" %i)
                        if Cube[white_look[i]]== wwalf[to_search]:
                            #print("11 -White Look index is %d" %white_look[i])
                           # print("12 - The location of the piece is at %d" %i)
                            bring_to_front(i)
                           # print("13********************************************************************************************************* - the piece should be infront")
                            break


                for i in range(54): # Put the piece in the correct location
                   #print("14 - Putting Piece in, this should be looking at %d " %i)
                    if Cube[i] == 'W' and i !=4:
                       # print("15- The front looking for the piece infront to put in: %d: " %i)
                        if Cube[white_look[i]] == wwalf[to_search]: # based on which cube we are looking for, is the other side of the 2-sided cube we are looking at the one?

                            if i == 21:
                                if to_search == 1:
                                    Move(Matrix_UpC)
                                elif to_search == 3:
                                    Move(Matrix_Naught)
                                elif to_search == 5:
                                    Move(Matrix_Up)
                                    Move(Matrix_Up)
                                elif to_search == 7:
                                    Move(Matrix_Up)


                                Move(Matrix_CenterC)
                                Move(Matrix_Left)
                                Move(Matrix_Center)
                                Move(Matrix_LeftC)

                                if to_search == 1:
                                    Move(Matrix_Up)
                                elif to_search == 3:
                                    Move(Matrix_Naught)
                                elif to_search == 5:
                                    Move(Matrix_Up)
                                    Move(Matrix_Up)
                                elif to_search == 7:
                                    Move(Matrix_UpC)



                            elif i == 23:
                                if to_search == 1:
                                    Move(Matrix_Up)
                                elif to_search == 3:
                                    Move(Matrix_Up)
                                    Move(Matrix_Up)
                                elif to_search == 5:
                                    Move(Matrix_Naught)
                                elif to_search == 7:
                                    Move(Matrix_UpC)


                                Move(Matrix_Center)
                                Move(Matrix_RightC)
                                Move(Matrix_CenterC)
                                Move(Matrix_Right)

                                if to_search == 1:
                                    Move(Matrix_UpC)
                                elif to_search == 3:
                                    Move(Matrix_Up)
                                    Move(Matrix_Up)
                                elif to_search == 5:
                                    Move(Matrix_Naught)
                                elif to_search == 7:
                                    Move(Matrix_Up)


                            elif i == 25:
                                if to_search == 1:
                                    Move(Matrix_Up)
                                    Move(Matrix_Up)
                                elif to_search == 3:
                                    Move(Matrix_UpC)
                                elif to_search == 5:
                                    Move(Matrix_Up)
                                elif to_search == 7:
                                    Move(Matrix_Naught)


                                Move(Matrix_Down)
                                Move(Matrix_MiddleD)
                                Move(Matrix_DownC)
                                Move(Matrix_MiddleU)

                                if to_search == 1:
                                    Move(Matrix_Up)
                                    Move(Matrix_Up)
                                elif to_search == 3:
                                    Move(Matrix_Up)
                                elif to_search == 5:
                                    Move(Matrix_UpC)
                                elif to_search == 7:
                                    Move(Matrix_Naught)

                            elif i == 37:
                                if to_search == 1:
                                    Move(Matrix_Up)
                                    Move(Matrix_Up)
                                elif to_search == 3:
                                    Move(Matrix_UpC)
                                elif to_search == 5:
                                    Move(Matrix_Up)
                                elif to_search == 7:
                                    Move(Matrix_Naught)


                                Move(Matrix_MiddleD)
                                Move(Matrix_Down)
                                Move(Matrix_Down)
                                Move(Matrix_MiddleU)

                                if to_search == 1:
                                    Move(Matrix_Up)
                                    Move(Matrix_Up)
                                elif to_search == 3:
                                    Move(Matrix_Up)
                                elif to_search == 5:
                                    Move(Matrix_UpC)
                                elif to_search == 7:
                                    Move(Matrix_Naught)

                            #else:
                                #print("The i is %d" %i)


                            search = 0
                            #print("16- If we got here, WE SHOULD HAVE PUT SOMETHING IN THE TOP!!! **********************************")
                            for i in range(1,8,2): #---------------------- Check the top!
                                if Cube[i] == 'W':
                                    for r in range(len(Need)): #for r in range(len(Need)-1):
                                         if Need[r-1] == i: # or len(Need)-1==0:
                                            if i==1 and Cube[52]=='O':
                                                Need.remove(1)
                                            elif i==3 and Cube[10]=='G':
                                                Need.remove(3)
                                            elif i==5 and Cube[28]=='B':
                                                Need.remove(5)
                                            elif i==7 and Cube[19]=='R':
                                                Need.remove(7)

    ##                               if len(Need)-1 == 0:
    ##                                    if i==7 and Cube[19]=='R':
    ##                                        Need.remove(7)
    ##                                        print("Need minus 7: %s" %Need)


                            break






    #print("TOP LAYER Cross is Complete\nYEYEYEYYEYEYEYEYEYEYEYYEY")

    # Orient the Center faces

    if Cube[22] == 'B':
        Move(Matrix_CenterC)
    elif Cube[22] == 'G':
        Move(Matrix_Center)
    elif Cube[22] == 'O':
        Move(Matrix_Center)
        Move(Matrix_Center)

    if debug == 0:
        PrintCube(Cube) #--------- This One
        print("Top Layer Cross Solved. Now Solve Edges\n\n") #--------- This One


    bool = Check_Parity()
    #print("Parity Check: %s " %bool)

    Needtc = [0,2,6,8] # These are the corners that are being looked for
    searchtc=0 # need to go find piece
    rescuetc = 0 # means it was found
    to_searchtc = 0



    wwalftc1=['O','G','O','B','X','X','R','G','R','B']
    wwalftc2=['G','O','B','O','X','X','G','R','B','R']


    while len(Needtc) != 0:
        #print("17- We are looking again *************************************************")

        for i in range(0,9,2): #---------------------- Check the top!
            if i != 4: # Not the Center
                #print("18- Searching the Top Layer Corner")
                #print("19- We are looking at the white piece %d" %i)

                if Cube[i] == 'W':
                    for r in range(len(Needtc)):
                        if Needtc[r-1] == i:
                            #print("20- we are looking through the cube at piece %d" %i)
                            if i==0 and Cube[51]=='O' and Cube[9] == 'G':
                                Needtc.remove(0)
                               # print("Need minus 1: %s" %Needtc)
                            elif i==6 and Cube[11]=='G'and Cube[18] == 'R':
                                Needtc.remove(6)
                                #print("Need minus 3: %s" %Needtc)
                            elif i==2 and Cube[29]=='B'and Cube[53]=='O':
                                Needtc.remove(2)
                                #print("Need minus 5: %s" %Needtc)
                            elif i==8 and Cube[20]=='R' and Cube[27] == 'B':
                                Needtc.remove(8)
                                #print("Need minus 7: %s" %Needtc)
                            else:
                               # print("Though White, now Search is: %d" %searchtc)
                                searchtc=1
                               # print("Now Search is %d:" %searchtc)
                                to_searchtc = Needtc[0]

                            #print("21 -Need looks like this: %s" %Needtc)
                        else:
                            #print("21- Search is: %d" %searchtc)
                            searchtc=1
                            #print("22 -Now Search is %d:" %searchtc)
                            to_searchtc = Needtc[0]

                else:
                    #print("21- Search is: %d" %searchtc)
                    searchtc=1
                   # print("22 -Now Search is %d:" %searchtc)
                    to_searchtc = Needtc[0]

               # print("23 - Looking for piece: %d" %i)


                if searchtc == 1:
                    #print("24 -Are we looking for the piece?")
                    for i in range(54): # Find the piece and put it in the Front Face
                        if Cube[i]=='W' and i !=4:
                            #print("25 -Looking at: %d" %i)
                            if Cube[white_looktc[i]]== wwalftc1[to_searchtc] or Cube[white_looktc[i]]== wwalftc2[to_searchtc] :
                                if Cube[white_looktc[white_looktc[i]]] == wwalftc1[to_searchtc+1] or Cube[white_looktc[white_looktc[i]]] == wwalftc2[to_searchtc+1]:
                                   # print("26 -White Look index is %d and the white look index corresponding is %d" %(white_looktc[i],white_looktc[white_looktc[i]]))
                                   # print("27 - The location of the piece is at %d" %i)
                                    bring_to_fronttc(i) # still need to make
                                    #print("28********************************************************************************************************* - the piece should be infront")
                                    break


                    if to_searchtc == 0:
                        Move(Matrix_Up)
                        Move(Matrix_Up)
                    elif to_searchtc == 2:
                        Move(Matrix_Up)
                    elif to_searchtc == 6:
                        Move(Matrix_UpC)
                    elif to_searchtc == 8:
                        Move(Matrix_Naught)

                    if Cube[26] == 'W':
                        Move(Matrix_Front)
                        Move(Matrix_Down)
                        Move(Matrix_FrontC)


                    elif Cube[33] == 'W':
                        Move(Matrix_RightC)
                        Move(Matrix_DownC)
                        Move(Matrix_Right)


                    elif Cube[38] == 'W':
                        Move(Matrix_RightC)
                        Move(Matrix_DownC)
                        Move(Matrix_DownC)
                        Move(Matrix_Right)
                        Move(Matrix_Down)
                        Move(Matrix_RightC)
                        Move(Matrix_DownC)
                        Move(Matrix_Right)


                    if to_searchtc == 0:
                        Move(Matrix_Up)
                        Move(Matrix_Up)
                    elif to_searchtc == 2:
                        Move(Matrix_UpC)
                    elif to_searchtc == 6:
                        Move(Matrix_Up)
                    elif to_searchtc == 8:
                        Move(Matrix_Naught)


                    search = 0
                    #print("29- If we got here, WE SHOULD HAVE PUT SOMETHING IN THE TOP!!! **********************************")
                    for i in range(0,9,2): #---------------------- Check the top!
                        if i != 4: # Not the Center
                            if Cube[i] == 'W':
                                for r in range(len(Needtc)):
                                    if Needtc[r-1] == i:
                                        if i==0 and Cube[51]=='O' and Cube[9] == 'G':
                                            Needtc.remove(0)
                                        elif i==6 and Cube[11]=='G'and Cube[18] == 'R':
                                            Needtc.remove(6)
                                        elif i==2 and Cube[29]=='B'and Cube[53]=='O':
                                            Needtc.remove(2)
                                        elif i==8 and Cube[20]=='R' and Cube[27] == 'B':
                                            Needtc.remove(8)

                    break






    #print("TOP LAYER IS Donneee\nYEYEYEYYEYEYEYEYEYEYEYYEY")
    if debug == 0:
        PrintCube(Cube) #--------- This One
        print("1st Layer Complete!!\n\n") #--------- This One



    # Start of second layer

    Needsl = [21,23,50,48] # These are the centers that are being looked for
    searchsl=0 # need to go find piece
    rescuesl = 0 # means it was found
    to_searchsl = 21
    see_if_it_works = 0
    bool = False

    searchingsl = [21,14,23,30,50,32,48,12]
    searchingsl2 = [12,14,16,21,23,25,30,32,34,37,39,41,43,46,48,50]
    wwalfsl=['R','G','R','B','O','B','O','G']
    wwalfsl2 = ['G','R','B','R','B','O','G','O']
    infinite_loop =0
    il = 0



    while len(Needsl) != 0 and il == 0:
        if infinite_loop > 1000 and il == 0:
            il = 1
            PrintCube(Cube)
            print("There is an Error!!")
        else:
            for y in range(4):
                infinite_loop += 1
                u =searchingsl[2*y]
                if Cube[u] == wwalfsl[2*y]:
                    if Cube[second_layer_look[u]] == wwalfsl[2*y+1]:
                        if ((u == 21 or u == 23) and Cube[22] == 'R') or ((u == 50 or u == 48) and Cube[49] == 'O'):
                            if u == 21 and Needsl[0] == u :
                                Needsl.remove(21)
                            elif u == 23 and Needsl[0] == u:
                                Needsl.remove(23)
                            elif u == 50 and Needsl[0] == u:
                                Needsl.remove(50)
                            elif u == 48 and Needsl[0] == u:
                                Needsl.remove(48)
                            else:
                                searchsl=1
                                to_searchsl = Needsl[0]
                        elif len(Needsl)-1==0:
                            if u == 48 and Needsl[0] == u:
                                Needsl.remove(48)
                            searchsl=1
                            to_searchsl = Needsl[0]

                    elif len(Needsl)-1==0:
                        if u == 48 and Needsl[0] == u:
                            Needsl.remove(48)
                        searchsl=1

                       # to_searchsl = Needsl[0]


                    else:
                        searchsl=1
                        to_searchsl = Needsl[0]

                else:
                    searchsl=1
                    to_searchsl = Needsl[0]




                if searchsl == 1:
                   # print("6??????????????666666666666?????????????????????????????????????????")
                    # based on search, look at all the pieces needed to be checked, then check adjacent,
                    # if it is in certain location, do certain moves to bring it to the front
                    # at that point, if piece 25 corresponds to 22 then do right move, otherwise do left move.

                    if to_searchsl == 21:
                        slc= 0
                    elif to_searchsl == 23:
                        slc = 2
                    elif to_searchsl == 50:
                        slc = 4
                    elif to_searchsl == 48:
                        slc = 6
                    else:
                        print("Error 410")



                    for i in range(16):
                       # print("We are looking at piece %d" %(searchingsl2[i]))
                        if Cube[searchingsl2[i]]==wwalfsl[slc] or Cube[searchingsl2[i]] == wwalfsl2[slc]:
                            if Cube[second_layer_look[searchingsl2[i]]]==wwalfsl[slc+1] or Cube[second_layer_look[searchingsl2[i]]] == wwalfsl2[slc+1]:
                                bring_to_frontsl(searchingsl2[i])
                                #print("This is the piece to go in")
                               #PrintCube(Cube)
                                break


                    if to_searchsl == 21:
                        Move(Matrix_Naught)
                    elif to_searchsl == 23:
                        Move(Matrix_Center)
                    elif to_searchsl == 50:
                        Move(Matrix_Center)
                        Move(Matrix_Center)
                    elif to_searchsl == 48:
                        Move(Matrix_CenterC)

                    if Cube[25] == Cube[22]:
                        Move(Matrix_Down)
                        Move(Matrix_Left)
                        Move(Matrix_DownC)
                        Move(Matrix_LeftC)
                        Move(Matrix_DownC)
                        Move(Matrix_FrontC)
                        Move(Matrix_Down)
                        Move(Matrix_Front)

                    elif Cube[25] == Cube[13]:
                        Move(Matrix_DownC)
                        Move(Matrix_DownC)
                        Move(Matrix_FrontC)
                        Move(Matrix_Down)
                        Move(Matrix_Front)
                        Move(Matrix_Down)
                        Move(Matrix_Left)
                        Move(Matrix_DownC)
                        Move(Matrix_LeftC)

                    else:
                        print("Uhhhhhh, what just happpened??")


                    if to_searchsl == 21:
                        Move(Matrix_Naught)
                    elif to_searchsl == 23:
                        Move(Matrix_CenterC)
                    elif to_searchsl == 50:
                        Move(Matrix_Center)
                        Move(Matrix_Center)
                    elif to_searchsl == 48:
                        Move(Matrix_Center)


                    #PrintCube(Cube)
                    searchsl = 0
                    for y in range(4):

                        u = searchingsl[2*y]
                        if len(Needsl) == 0:
                            break
                        elif Cube[u] == wwalfsl[2*y]:
                            if Cube[second_layer_look[u]] == wwalfsl[2*y+1]:
                                if ((u == 21 or u == 23) and Cube[22] == 'R') or((u == 50 or u == 48) and Cube[49] == 'O'):
                                    if u == 21 and Needsl[0] == u:
                                        Needsl.remove(21)
                                    elif u == 23 and Needsl[0] == u:
                                        Needsl.remove(23)
                                    elif u == 50 and Needsl[0] == u:
                                        Needsl.remove(50)
                                    elif u == 48 and Needsl[0] == u:
                                        Needsl.remove(48)
                    break




    if debug == 0:
        print("\n\nNow Solve the Second layer") #--------- This One
        PrintCube(Cube) #--------- This One
        print("2nd Layer Complete!!") #--------- This One
        print("Lets start on the bottom Layer.\n\n") #--------- This One



    Move(Matrix_UpFront)
    Move(Matrix_UpFront)

    if debug == 0:
        PrintCube(Cube) #--------- This One
        print("Solve for the yellow Cross\n")

    yellows1 = 0
    yellows3 = 0
    wym = 0 # which yellow move
    crosstl = 0 # Cross top left switch
    adjacent = 2 # For top cross adjacency
    county=0 # which opp to look at

    for w in range(1,8,6): # 1 and 7
        if Cube[w] == 'Y':
            yellows1 += 1

    for x in range(3,6,2): # 3 and 5
        if Cube[x] == 'Y':
            yellows3 += 1

    if yellows1 == 0 and yellows3 == 0:
       # print("There is a single yellow in the center")
        wym = 1
    elif yellows1 == 0 and yellows3 == 2:
       # print("There is a line of yellows, do F,R,U,R\',U\',F\'")
        wym=2
    elif yellows1 == 1 and yellows3 == 1 :
       # print("There is an \'L\' of yellows, find rotation and do F,U,R,U\',R\',F\' ")
        wym=3
    elif yellows1 == 2 and yellows3 == 0 :
      #  print("There is a line of yellows, do Up rotation and do F,R,U,R\',U\',F\'")
        wym=4
    elif yellows1 == 2 and yellows3 == 2 :
     #   print("There is a cross of yellows, skip to next alg")
        wym=5

    if wym == 0:
        print("Error 412") # because there are no yellows on top
    elif wym == 1:
        FURURF()
        Move(Matrix_Up)
        FRURUF()
    elif wym == 2:
        FRURUF()
    elif wym == 3:
        if crosstl == 0:
            if Cube[1] == 'Y' and Cube[5] == 'Y':
                Move(Matrix_UpC)
            elif Cube[3] == 'Y' and Cube[7] == 'Y':
                Move(Matrix_Up)
            elif Cube[5] == 'Y' and Cube[7] == 'Y':
                Move(Matrix_Up)
                Move(Matrix_Up)
            else:
                crosstl = 1

        FURURF()
    elif wym == 4:
        Move(Matrix_Up)
        FRURUF()
    elif wym == 5:
        Move(Matrix_Naught)
        #adjacent = 0
    else:
        print("Error 411")


    if debug == 0:
        PrintCube(Cube) #--------- This One
        print("We should have the cross on the top") #--------- This One
        print("Now solve for correct cross locations\n\n") #--------- This One

    counter = 0
    move_done =0

    crosspairs = ['R','G','B','R','O','B','G','O','R','B','B','O','O','G','G','R'
    ,'O','G','G','R','R','B','B','O','O','B','G','O','R','G','B','R']
    correct_centers = ['R','G','B','O','B','R','O','G','O','B','G','R','G','O','R','B']

    for x in range(1,8,2): # Check if the top is in the correct order
        if Cube[52] == 'R':
            if Cube[white_look[x]] == correct_centers[int(((x-1))/2)]:
                counter += 1
        elif Cube[52] == 'B':
            if Cube[white_look[x]] == correct_centers[int(((x-1)/2))+4]:
                counter += 1
        elif Cube[52] == 'O':
            if Cube[white_look[x]] == correct_centers[int(((x-1)/2))+8]:
                counter += 1
        elif Cube[52] == 'G':
            if Cube[white_look[x]] == correct_centers[int(((x-1)/2)) + 12]:
               counter += 1

    if counter == 4:
        adjacent = 0

    if adjacent == 2:
        for b in range(1,8,6):
            for c in range(3,6,2):
                county += 1
                for d in range(4):
                    if (((Cube[white_look[b]] == crosspairs[2*d] and Cube[white_look[c]] == crosspairs[2*d+1] and county == 1)
                    or (Cube[white_look[b]] == crosspairs[2*d+8] and Cube[white_look[c]] == crosspairs[2*d+9] and county == 2)
                    or (Cube[white_look[b]] == crosspairs[2*d+16] and Cube[white_look[c]] == crosspairs[2*d+17] and county == 3)
                    or (Cube[white_look[b]] == crosspairs[2*d+24] and Cube[white_look[c]] == crosspairs[2*d+25] and county == 4))) and move_done == 0:
                        if b == 1 and c == 3:
                            Move(Matrix_Up)
                            Move(Matrix_Up)
                        elif b == 1 and c == 5:
                            Move(Matrix_Up)
                        elif b== 7 and c == 3:
                            Move(Matrix_UpC)
                        elif b == 7 and c == 5:
                            Move(Matrix_Naught)

                        adjacent = 1
                        move_done =1
                        break
                        #turn on to say something that it is an adjacent pair

   # PrintCube(Cube)
    if adjacent == 1:
        #print("We should do Center Cross Alg")
        Center_Cross_Alg()
    elif adjacent ==2:
        #print("Now find where the cross center pairs are and do algorithm")
        while Cube[19] != Cube[22]:
            Move(Matrix_Up)

        Center_Cross_Alg()
        Move(Matrix_Up)
        Move(Matrix_CWTwist)
        Center_Cross_Alg()
        Move(Matrix_CCWTwist)
     # elif check so that the Cube[19]  == Cube[22] otherwise keep rotating.
        #then do Center Cross, Up, Clockwise Rotation of Cube, then Center Cross
    else:
       # print("We are goood!!! you dont neeed to do anything")
        Move(Matrix_Naught) # do nothing?




    if Cube[19] == 'O':
        Move(Matrix_Naught)
    elif Cube[19] == 'B':
        Move(Matrix_UpC)
    elif Cube[19] == 'R':
        Move(Matrix_Up)
        Move(Matrix_Up)
    elif Cube[19] == 'G':
        Move(Matrix_Up)

    if debug == 0:
        PrintCube(Cube)
        print("We should have the centers in the right place")
        print("Now get the corners in the right place\n\n")




    # Corner placement
    Needytc = [0,2,6,8] # These are the corners that are being looked for
    top_right = [2,29,53]
    searchytc=0 # need to go find piece
    rescueytc = 0 # means it was found
    to_searchytc = 0
    piece = 4
    top_left = 10
    found = 0
    tlfound = 0
    did_it = 0 # bit to identify if u did the move

    wyalftc1=['R','G','R','B','X','X','O','G','O','B']
    wyalftc2=['G','R','B','R','X','X','G','O','B','O']


    while tlfound != 1:
        for r in range(4):
            to_searchytc = Needytc[r]
            for i in range(54): # Find the piece and put it in the Front Face
                if Cube[i]=='Y' and found == 0:
                    #print("25 -Looking at: %d" %i)
                    if Cube[white_lookytc[i]]== wyalftc1[to_searchytc] or Cube[white_lookytc[i]]== wyalftc2[to_searchytc] :
                        if Cube[white_lookytc[white_lookytc[i]]] == wyalftc1[to_searchytc+1] or Cube[white_lookytc[white_lookytc[i]]] == wyalftc2[to_searchytc+1]:
                           # print("26 -White Look index is %d and the white look index corresponding is %d" %(white_looktc[i],white_looktc[white_looktc[i]]))
                           # print("27 - The location of the piece is at %d" %i)
                            if i < 9:
                                piece = i
                            elif white_lookytc[i] < 9:
                                piece = white_lookytc[i]
                            else:
                                piece = white_lookytc[white_lookytc[i]]

                           # print("The location of the piece is at %d" %piece)

                            if piece == Needytc[r]:
                                top_left = piece
                                found = 1
                            else:
                                continue

            if found == 1:
               # print("The top left piece should be %d" %top_left)
                tlfound = 1
                # bring the piece to the top left by
                break

        if found == 0:
           # print("Do a move anyways and go back...")
            Down_Cross()
           # print("Do the Down Cross Move")
            #PrintCube(Cube)


    if top_left == 0:
        Move(Matrix_Naught)
    elif top_left == 2:
        Move(Matrix_CCWTwist)
    elif top_left == 6:
        Move(Matrix_CWTwist)
    elif top_left == 8:
        Move(Matrix_CWTwist)
        Move(Matrix_CWTwist)
    elif top_left == 10:
        Move(Matrix_Naught) # All the pieces are in their place
    else:
        print("Error 413")

    #PrintCube(Cube)

    # look at piece 2, 53 and 29
    # if it should go down then Down_Cross()
    # if it should cross and down Cross_Cross()
    # if it should go it its place, then dont do anything
    # if it should go to the left, Then there was a problem with the last algorithm
    if top_left != 10:
        for a in range(3):
            if Cube[top_right[a]]== 'Y' and did_it == 0:
                if Cube[white_lookytc[top_right[a]]] == Cube[31] or Cube[white_lookytc[white_lookytc[top_right[a]]]] == Cube[31]:
                    if Cube[white_lookytc[top_right[a]]] == Cube[49] or Cube[white_lookytc[white_lookytc[top_right[a]]]] == Cube[49]:
                        did_it =1 # we are good, just need to rotate
                    else:
                        Down_Cross()
                        #print("I did the down cross corner move")
                        did_it = 1
                elif Cube[white_lookytc[top_right[a]]] == Cube[13] or Cube[white_lookytc[white_lookytc[top_right[a]]]] == Cube[13]:
                    if Cube[white_lookytc[top_right[a]]] == Cube[49] or Cube[white_lookytc[white_lookytc[top_right[a]]]] == Cube[49]:
                        did_it =1 # we are good, just need to rotate
                    else:
                        Cross_Cross()
                        #print("I just did the cross cross corner move")
                        did_it = 1
                else:
                    print("Error 414")


    if debug == 0:
        PrintCube(Cube)
        print("Pieces should be in the correct places")
        print("Now just flip the corners to finish\n\n")
        #--------- This One

    #Flipping the corners
    num_yellows = 0 # number of yellows on top
    rotations = 0
    ffts = 2 # First front then side

    for e in range(9):
        if Cube[e] == 'Y':
            num_yellows = num_yellows + 1

    if num_yellows == 5: # every corner needs to be flipped
        rotations = 4
    elif num_yellows == 6: # Only 3 need to be flipepd
        rotations = 3
    elif num_yellows == 7: # only 2
        rotations = 2
    elif num_yellows == 9: # you're done...
        rotations = 0

  #  print("The number of yellows on top are: %d" %num_yellows)
   # print("Number of Rotations is :%d" %rotations)

    if rotations != 0: # if ur not completed
        while Cube[8] == 'Y': # check to see if bottom right needs to be rotated
            Move(Matrix_CCWTwist) # if not then twist cube to find piece
          #  print("Need to Rotate until the piece is at the bottom Right")
          #  PrintCube(Cube)

        if rotations == 4:
            for y in range(4):
                if Cube[20] == 'Y':
                    Front_Corner_Flip()

                 #   print("Just Did Front")
                 #   PrintCube(Cube)
                    ffts = 1
                elif Cube[27] == 'Y':
                    Side_Corner_Flip()

               #     print("Just Did Side ")
               #     PrintCube(Cube)
                    ffts = 0
                else:
                    print("Error 415 - 1")

                #After the first one, Rotate UP Counter for the next piece
                Move(Matrix_UpC)
        elif rotations == 3:
            #print("Rotations 3")
            #PrintCube(Cube)
            if Cube[20] == 'Y':
                Front_Corner_Flip()

                #print("Just Did Front ")
               # PrintCube(Cube)
                ffts = 1
            elif Cube[27] == 'Y':
                Side_Corner_Flip()

                #print("Just Did Side")
                #PrintCube(Cube)
                ffts = 0
            else:
                print("Error 415 - 2")


            while Cube[8] == 'Y':
                Move(Matrix_UpC)
               # PrintCube(Cube)

            if ffts == 1:
                for q in range(2):
                    Side_Corner_Flip()

            elif ffts == 0:
                for q in range(2):
                    Front_Corner_Flip()

            for t in range(3):
                if Cube[8] == 'Y':
                    Move(Matrix_UpC)


            if Cube[20] == 'Y':
                Front_Corner_Flip()
                ffts = 1
            elif Cube[27] == 'Y':
                Side_Corner_Flip()
                ffts = 0
            else:
                print("Error 415 -3")
                PrintCube(Cube)

            #After the first one, Rotate UP Counter for the next piece
            Move(Matrix_UpC)
           # print("Just rotated up counter")
           # PrintCube(Cube)

        elif rotations ==2 :
            for y in range(2):
                if Cube[8] == 'Y':
                    Move(Matrix_UpC)
                if Cube[20] == 'Y':
                    Front_Corner_Flip()

                   # print("Just Did Front")
                    ffts = 1
                elif Cube[27] == 'Y':
                    Side_Corner_Flip()

                  #  print("Just Did Side ")
                    ffts = 0
                else:
                    print("Error 415 -4 ")

                #After the first one, Rotate UP Counter for the next piece
                for pr in range(4):
                    if Cube[8] == 'Y':
                        Move(Matrix_UpC)



    while Cube[19] != Cube[22]:
        Move(Matrix_UpC)


    #PrintCube(Cube)


    #print("You should be done....")



## --- Just for testing and debugging

    Good_set = 0

    upcolor = Cube[4]
    frontcolor = Cube[22]
    cube_oriented_up = False

   # PrintCube(Cube)
    while cube_oriented_up == False:
        upcolor = Cube[4]
        frontcolor = Cube[22]
        if upcolor == 'W':
            if frontcolor == 'B':
                Move(Matrix_CCWTwist) #Twist Cube CCW
            elif frontcolor == 'G':
                Move(Matrix_CWTwist) #Twist Cube CW
            elif frontcolor == 'O':
                 Move(Matrix_CWTwist) #Twist Cube Twice either direction
            elif frontcolor == 'R':
                cube_oriented_up = True
                #Do nothing....
                # make it so that variable Oriented is High!! (cube_oriented_up =1)
                #( Therefore after Scrammble and any rotation, orient when needed)
        elif upcolor == 'G':
            if frontcolor == 'W':
                Move(Matrix_FrontUp) #Twist FrontUP
            elif frontcolor == 'O':
                Move(Matrix_UpRight) #Twist UpRight
            elif frontcolor == 'Y':
                Move(Matrix_UpFront) #Twist UpFront
            elif frontcolor == 'R':
                Move(Matrix_UpLeft) #Twist UpLeft
        elif upcolor == 'R':
            if frontcolor == 'W':
                Move(Matrix_FrontUp) #Twist FrontUP
            elif frontcolor == 'G':
                Move(Matrix_UpRight) #Twist UpRight
            elif frontcolor == 'Y':
                Move(Matrix_UpFront) #Twist UpFront
            elif frontcolor == 'B':
                Move(Matrix_UpLeft) #Twist UpLeft
        elif upcolor == 'B':
            if frontcolor == 'W':
                Move(Matrix_FrontUp) #Twist FrontUP
            elif frontcolor == 'R':
                Move(Matrix_UpRight) #Twist UpRight
            elif frontcolor == 'Y':
                Move(Matrix_UpFront) #Twist UpFront
            elif frontcolor == 'O':
                Move(Matrix_UpLeft) #Twist UpLeft
        elif upcolor == 'Y':
            Move(Matrix_UpFront)
            #Whatever it is, just spin FrontUp or UpFront
        elif upcolor == 'O':
            if frontcolor == 'W':
                Move(Matrix_FrontUp) #Twist FrontUP
            elif frontcolor == 'B':
                Move(Matrix_UpRight) #Twist UpRight
            elif frontcolor == 'Y':
                Move(Matrix_UpFront) #Twist UpFront
            elif frontcolor == 'G':
                Move(Matrix_UpLeft) #Twist UpLeft
        else:
            print("Error 422")

   # print("Rotate Cube UP")
    if debug == 0:
        PrintCube(Cube)
        print("You are Done!")

    for p in range(53):
        if Cube[p] ==  New_Cube_Original_Colors[p]:
            Good_set += 1

    if Good_set == 53:
        Good_sets += 1
      #  print("Good Set")
       # PrintCube(Cube)
    else:
        Good_set += 0
        print("Bad SET!!!!")
        PrintCube(Cube)
        bad_set = counting + 1
        bad.append(bad_set)




    counting += 1
    if debug != 11:
        elapsed_time = time.time() - start
        print("\nThe program FINISHED and took a total of %3.3f seconds" %elapsed_time)
        print("This is how many good ones were:  %d / %d  " %(Good_sets,counting))

    how_many =len(moves_inputted)

    total = 0

    if debug == 3:
        print("The amount of moves this algorithm gave is: %d" %how_many)

    total = total + how_many

    count = 0

    for r in range(len(moves_inputted)-1):
        if moves_inputted[r] == moves_inputted[r+1]:
            count = count + 1

    count = count  + 23
    count = len(moves_inputted) - count
    #print("The New Count is %d" %count)
    new_total = 0
    new_total = new_total + count


if len(bad) != 0:
    print("The bad sets were: %s" %bad)

average = total/counting
print("The average of the %d runs was: %d" %(counting,average))
average = new_total/counting
print("The new average of the %d runs was: %d" %(counting,average))
print("The Set Count and the first Three moves = %d" %(set_count))


time.sleep(5)

#print("The moves to solve this cube are %s" %moves_inputted)

#-------------------- ERROR CODES -----------------#

# Error 422 ==>  During Orienting the Cube so that White is up
#               And the Red face is forward, the program could not
#               Identify what the color of the face was for the top.
#
# Error 408 => Top Layer has an invalid color attached to a white cross peice
#
# Error 409 => Top layer cross has too many pieces?
# Error 410 => Searching for something that you shouldnt in the second layer
# Error 411 => Which Yellow Move ( WYM ) is bugging....
# Error 412 => There is a situation at the bottom that should not be happening when trying to get the cross
# Error 413 => Cant find placement of bottom layer corners?
# Error 414 => Down know how to rotate corner pieces to allign
# Error 415 => The Bottom Layer, Corner Flip Algorithm, yea, somethings wrong...