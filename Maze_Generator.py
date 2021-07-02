#Generating a maze using Randomized Prim's algorithm
#https://en.wikipedia.org/wiki/Maze_generation_algorithm#Randomized_Prim's_algorithm

import random

#class Cell stores the coordinates of a cell (row, column)
class Cell:
    def __init__(self, x, y):
        self.x=int(x)
        self.y=int(y)

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __hash__(self):
        return hash(17*self.x+31*self.y)


directions = [[0, -2], [0, 2], [2, 0], [-2, 0]]
grid = []

#check if it is a valid cell
def valid(x, y):
    return x>=0 and x<len(grid) and y>=0 and y<len(grid[0])

#find's all the adjacent cells which are either 1->wall or 0->path according to the choice
def adjacentCells(cell, wall):
    adjCells = []

    for d in directions:
        x = cell.x+d[0]
        y = cell.y+d[1]
        if(valid(x, y) and grid[x][y]==wall):
            adjCells.append(Cell(x, y))

    return adjCells

#find's all adjacent walls
def adjacentWalls(cell):
        return adjacentCells(cell, 0)

#find's all adjacent paths
def adjacentPaths(cell):
    return adjacentCells(cell, 1)

#connect's the two cells making it a path (makes the cells in between the two cells a path)
def connect(cell1, cell2):
    grid[cell1.x][cell1.y] = 1
    grid[cell2.x][cell2.y] = 1
    x = (cell1.x+cell2.x)//2
    y = (cell1.y+cell2.y)//2
    grid[x][y] = 1

def createMaze(rows, cols):

    global grid
    # 0 -> wall 1 -> path
    
    grid=[[0 for x in range(rows)] for y in range(cols)]

    #Prim's Algorithm

    #starting point (1, 1)
    sp = Cell(1, 1)
    grid[1][1] = 1

    #stores a set of adjacent walls of the choosen paths
    unvisitedCells = set()
    unvisitedCells.update(adjacentWalls(sp))

    while len(unvisitedCells)>0:
        #randomly choose a wall from the set
        randomWall = random.choice(list(unvisitedCells))

        #list all the path adjacent to the wall
        neighbours = adjacentPaths(randomWall)

        #choose a random path adjacent to the wall and connect it 
        if(len(neighbours) != 0):
            randomNeighbour = random.choice(neighbours)
            connect(randomWall, randomNeighbour)
        
        #update the set of adjacent walls
        unvisitedCells.update(adjacentWalls(randomWall))

        #remove the choose wall since now it is a path
        unvisitedCells.remove(randomWall)

    #print the maze
    for i in range(rows):
        for j in range(cols):
            print(grid[i][j], end =" ")
        print(0)
        # print("\n")
    for i in range(rows+1):
        print(0, end =" ")

createMaze(10, 10)


    












