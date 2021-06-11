import numpy as np
'''
1.Check if board is full or not
2.Find first empty space 
3.Put number from 1-9 in it
3a.Check if it is only number in row column 3x3 subboard aka if number is valid
4.If number is not legal make place empty
5.Repeate 1,2,3.
'''
board = [[0 for x in range(1,10)] for y in range(1,10)] 
#board = [[3,0,6,5,0,8,4,0,0],
        #[5,2,0,0,0,0,0,0,0],
        #[0,8,7,0,0,0,0,3,1],
        #[0,0,3,0,1,0,0,8,0],
        #[9,0,0,8,6,3,0,0,5],
        #[0,5,0,0,9,0,6,0,0],
        #[1,3,0,0,0,0,2,5,0],
        #[0,0,0,0,0,0,0,7,4],
        #[0,0,5,2,0,6,3,0,0]]

def pretty_printed(board):
  for r in range(len(board)):
    if r%3==0 and r!=0:
      print('-------------------')
    for c in range(len(board[r])):
      if c%3==0 and c!=0:
        print('|',end='')
      if c == 8:
        print(board[r][c])
      else:
        print(str(board[r][c])+' ' ,end='')

def empty_space(board):
  for r in range(len(board)):
    for c in range(len(board[r])):
      if board[r][c] == 0:
        return (r,c)
  return None

def valid_n(board,n,r,c):
  for i in range(len(board)):
    #column
    if n == board[i][c]:
      return False
    #row
    if n == board[r][i]: 
      return False

  r_ = r//3
  c_ = c//3
  for r in range(r_*3,r_*3+3):
    for c in range(c_*3,c_*3+3):
      if n == board[r][c]:
        return False

  return True

def sudoku_solver(board):
    if not empty_space(board):  #if you dont find empty space return True because if function is true that mean  
        return True 
    else:                       #if you find empty space proceed to occupied it with number                         
        r,c = empty_space(board)
    for n in range(1,10):
        if valid_n(board,n,r,c):  #if number is safe put it in place.
            board[r][c] = n
            if sudoku_solver(board):
                return True
            board[r][c] = 0 
    return False

def random_zeros(board):
  counter = 0
  while counter <= 40:
    counter += 1
    r = int(np.random.choice(9,1))
    c = int(np.random.choice(9,1))
    board[r][c] = 0

sudoku_solver(board)
random_zeros(board)
pretty_printed(board)