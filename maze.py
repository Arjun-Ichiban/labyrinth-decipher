import tkinter as tk
from maze_generator import *
from maze_solver import *


# Set number of rows and columns
ROWS = 11
COLS = 11

# Create a grid of None to store the references to the tiles
tiles = [[None for _ in range(COLS)] for _ in range(ROWS)]

root = tk.Tk()
c = tk.Canvas(root, width=330, height=330, borderwidth=0, background='black')
c.pack()

col_width = 30
row_height = 30


grid = createMaze(11, 11, root, c, tiles, col_width, row_height)

grid[0][0] = grid[0][1] = 1
grid[10][10] = grid[10][9] = 1
# for i in range(11):
#     for j in range(11):
#         print(grid[i][j], end =" ")
#     print("\n")

root.mainloop()
# solveMaze(11, 11, grid)