#!/usr/bin/env python
# coding: utf-8

# In[7]:


board = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]


# In[8]:


def print_board(board):
    for i, row in enumerate(board):
        row_str = " "
        for j, value in enumerate(row):
            row_str += value
            if j != len(row) - 1:
                row_str += " | "
        
        print(row_str)
        if i != len(board) - 1:
            print('-----------')


# In[9]:


print_board(board)


# In[10]:


def get_move(turn, board):
    
    while True:
        row = input('row:' )
        col = input('col:' )

            
        try:
            rwint = int(row)
            if int(row) != rwint:
                #print('Invalid Entry! Please enter a number')
                continue
            clint = int(col)
            if int(col) != clint:
                #print('Invalid Entry! Please enter a number')
                continue
        except:
                print('Invalid Entry! Please enter a number')
                break

        row = int(row)
        col = int(col)
        
        if row < 1 or row > len(board):
            print('Invalid Row! Try again')
        elif col < 1 or col > len(board[row-1]):
            print('Invalid Column! Try again')
        elif board[row-1][col-1] != ' ':
            print('Already Full, enter another')
        else:
            break
    
    board[row-1][col-1] = turn


# In[11]:


def check_win(board, turn):
    lines = [[(0,0),(0,1),(0,2)], 
             [(1,0),(1,1),(1,2)], 
             [(2,0),(2,1),(2,2)],
             [(0,0),(1,0),(2,0)],
             [(0,1),(1,1),(2,1)],
             [(0,2),(1,2),(2,2)],
             [(0,0),(1,1),(2,2)],
             [(0,2),(1,1),(2,0)]
            ]
    
    for line in lines:
        win = True
        for pos in line:
            row, col = pos
            if board[row][col] != turn:
                win = False
                break
                
        if win:
            return True
        
    return False


# In[12]:




turn = 'X'
turn_number = 0
print_board(board)

while turn_number < 9:
    print()
    print('It is the', turn, 'players turn. Please select your move')
    
    get_move(turn, board)
    print_board(board)
    
    winner = check_win(board, turn)
    if winner:
        break
        
    if turn == 'X':
        turn = '0'
    else:
        turn = 'X'
    turn_number += 1
    
if turn_number == 9:
    print('Tied Game')
else:    
    print('The winner was', turn)
    


# 
