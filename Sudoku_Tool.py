"""
SE-I Mini project - SUDOKU Validator/Solver
Name - Kimaya Abhyankar (111903041)
       Nishant Badgujar (111903053)
"""

from Sudoku_Testing import *


'''
board = [[1, 4, 7, 0, 0, 0, 0, 0, 3],
        [2, 5, 0, 0, 0, 1, 0, 0, 0],
        [3, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 2, 0, 0, 0, 4],
        [0, 0, 0, 4, 1, 0, 0, 2, 0],
        [9, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 9],
        [4, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 1, 0, 0, 8, 0, 0, 7]]

print(np.matrix(board))
valid_board(board)

'''

board = [[0, 0, 0, 0, 5, 0, 1, 4, 0],
        [7, 0, 0, 0, 0, 8, 0, 9, 0],
        [0, 0, 5, 2, 0, 0, 0, 7, 0],
        [0, 4, 0, 0, 0, 0, 6, 5, 9],
        [0, 0, 0, 6, 0, 2, 0, 0, 0],
        [6, 7, 3, 0, 0, 0, 0, 2, 0],
        [0, 9, 0, 0, 0, 1, 5, 0, 0],
        [0, 3, 0, 5, 0, 0, 0, 0, 8],
        [0, 2, 7, 0, 8, 0, 0, 0, 0]]

print("\nGiven Board is:\n")
print(np.matrix(board))
valid_board(board)
print("\n Solution is:\n-------------------------")



'''board = [[1, 4, 4, 0, 0, 0, 0, 0, 3],
         [2, 5, 0, 0, 0, 1, 0, 0, 0],
         [3, 0, 9, 0, 0, 0, 0, 0, 0],
         [0, 8, 0, 0, 2, 0, 0, 0, 4],
         [0, 0, 0, 4, 1, 0, 0, 2, 0],
         [9, 0, 0, 0, 0, 0, 6, 0, 0],
         [0, 0, 3, 0, 0, 0, 0, 0, 9],
         [4, 0, 0, 0, 0, 2, 0, 0, 9],
         [0, 0, 1, 0, 0, 8, 0, 0, 7]]

print(np.matrix(board))
valid_board(board)
'''

grid = board
def possible(x, y, n):
	global grid
	for i in range (0, 9):
		if grid[i][y] == n:
			return False
	for j in range (9):
		if grid[x][j] == n:
			return False

	x0 = (x // 3) * 3
	y0 = (y // 3) * 3

	for i in range(3):
		for j in range(3):
			if grid[x0 + i][y0 + i] == n:
				return False
	return True

def solve():
	global grid
	for i in range (0, 9):
		for j in range (0, 9):
			if grid[i][j] == 0:
				for _ in range(1,10):
					if possible(i, j, _):
						grid[i][j] = _
						solve()
						grid[i][j] = 0
				return
	print(np.matrix(grid))
	input ("More?")

solve()
