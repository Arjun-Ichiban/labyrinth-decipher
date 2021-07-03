# Generating a maze using Randomized Prim's algorithm
# https://en.wikipedia.org/wiki/Maze_generation_algorithm#Randomized_Prim's_algorithm

import random
import time

# class Cell stores the coordinates of a cell (row, column)
class Cell:
    def __init__(self, x, y):
        self.x=int(x)
        self.y=int(y)

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __hash__(self):
        return hash(17*self.x+31*self.y)


# left right top down the directions of adjacent cells which is at a distance 2
directions = [[0, -2], [0, 2], [2, 0], [-2, 0]]
grid = []

# check if it is a valid cell
def valid(x, y):
    return x>=0 and x<len(grid)-1 and y>=0 and y<len(grid[0])-1

# find's all the adjacent cells which are either 1->wall or 0->path according to the choice
def adjacentCells(cell, wall):
    adjCells = []

    for d in directions:
        x = cell.x+d[0]
        y = cell.y+d[1]
        if(valid(x, y) and grid[x][y]==wall):
            adjCells.append(Cell(x, y))

    return adjCells

# find's all adjacent walls
def adjacentWalls(cell):
        return adjacentCells(cell, 0)

# find's all adjacent paths
def adjacentPaths(cell):
    return adjacentCells(cell, 1)

# create the tile on the canvas
def draw(x, y, root, c, tiles, row_height, col_width):
    tiles[x][y] = c.create_rectangle(y*col_width, x*row_height, (y+1)*col_width, (x+1)*row_height, fill="white")
    root.update_idletasks()               
    root.update()

# connect's the two cells making it a path (makes the cells in between the two cells a path)
def connect(cell1, cell2, root, c, tiles, col_width, row_height):
    grid[cell1.x][cell1.y] = 1
    x = int((cell1.x+cell2.x)/2)
    y = int((cell1.y+cell2.y)/2)
    grid[x][y] = 1
    xx = cell1.x
    yy = cell1.y
    draw(x, y, root, c, tiles, row_height, col_width)
    draw(xx, yy, root, c, tiles,  row_height, col_width)
    time.sleep(0.1)

def createMaze(rows, cols, root, c, tiles,  row_height, col_width):

    global grid
    # 0 -> wall 1 -> path
    
    grid=[[0 for x in range(cols)] for y in range(rows)]

    #entry point make it as a path
    grid[0][0] = grid[0][1] = 1
    draw(0, 0, root, c, tiles, row_height, col_width)
    draw(0, 1, root, c, tiles, row_height, col_width)
    time.sleep(0.2)

    # ---Prim's Algorithm---

    # starting point of the algorithm (1, 1)
    x = 1
    y = 1
    sp = Cell(1, 1)
    grid[1][1] = 1

    # convert the tile on canvas to a path
    draw(x, y, root, c, tiles, row_height, col_width)
    time.sleep(0.1)

    # stores a set of adjacent walls of the choosen paths
    unvisitedCells = set()
    unvisitedCells.update(adjacentWalls(sp))

    while len(unvisitedCells)>0:
        # randomly choose a wall from the set
        randomWall = random.choice(list(unvisitedCells))

        # list all the path adjacent to the wall
        neighbours = adjacentPaths(randomWall)

        # choose a random path adjacent to the wall and connect it 
        if(len(neighbours) != 0):
            randomNeighbour = random.choice(neighbours)
            connect(randomWall, randomNeighbour, root, c, tiles, col_width, row_height)
        
        # update the set of adjacent walls
        unvisitedCells.update(adjacentWalls(randomWall))

        # remove the choose wall since now it is a path
        unvisitedCells.remove(randomWall)

    # exit point make it as a path
    grid[rows-1][cols-1] = grid[rows-1][cols-2] = 1
    draw(rows-1, cols-1, root, c, tiles, row_height, col_width)
    draw(rows-1, cols-2, root, c, tiles, row_height, col_width)
    time.sleep(0.1)

    return grid