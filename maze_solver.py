# Solve a maze using Dijstra's Algorithm

import sys
import heapq
import time

# Distance class is stores the distance of the cell form the entry point (used in heap)
class Distance:
    def __init__(self, x, y, dis):
        self.x = x
        self.y = y
        self.dis = dis

    def __lt__(self, nxt):
        return self.dis < nxt.dis

# Stores the coordinates of the cell
class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

infinite = sys.maxsize

# the cells which can be reached from a given cell right left top down
direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

# the actual maze 0-> wall and 1-> path
grid = []
# dist array stores the minimum distance of each cell from the starting point 
dist = []
# parent array stores the cell from which it was connected to
parent = []

# we initialize the dist array to infinite since at the beginning every path cell is unvisited
# and parent as -1, -1
def initializeArrays(rows, cols):
    global dist, parent
    dist=[[infinite for x in range(cols)] for y in range(rows)]
    parent=[[Cell(-1, -1) for x in range(cols)] for y in range(rows)]
    
    
# check if it is a valid cell
def valid(x, y):
    return x>=0 and x<len(grid) and y>=0 and y<len(grid[0])

# create the tile on the canvas
def draw(x, y, root, c, tiles, row_height, col_width, colour):
    tiles[x][y] = c.create_rectangle(y*col_width, x*row_height, (y+1)*col_width, (x+1)*row_height, fill=colour)
    root.update_idletasks()               
    root.update()

# start_x and start_y is the starting point in the maze
# end_x and end_y is the ending point in the maze
# as choosen by the user

def solveMaze(rows, cols, grid1, root, c, tiles, row_height, col_width, start_x, start_y, end_x, end_y):
    global grid
    grid = grid1
    initializeArrays(rows, cols)

    dist[start_x][start_y] = 0

    # ---Dijstra's algorithm using heap data structure---
    
    heap = []
    heapq.heappush(heap, Distance(start_x, start_y, 0))

    while(len(heap)):
        # take the cell with the minimum distance
        min = heapq.heappop(heap)

        if not((min.x==start_x and min.y==start_y) or(min.x==end_x and min.y==end_y)):
            draw(min.x, min.y, root, c, tiles, row_height, col_width, "lawngreen")
            time.sleep(0.1)

        # find it's adjacent cell
        for d in direction:
            x = min.x+d[0]
            y = min.y+d[1]
 
            # if the adjacent cell is valid and it is a path check it's distance with the new distance
            if(valid(x, y) and grid[x][y]==1):
                # if the new distance is lesser, then update the dist array and add it to the heap 
                if(min.dis+1<dist[x][y]):
                    dist[x][y] = min.dis+1
                    parent[x][y] = Cell(min.x, min.y)
                    heapq.heappush(heap, Distance(x, y, dist[x][y]))

    # Print the path if it exist's
    if(dist[rows-1][cols-1]==max):
        print("Path Not Found")
    else:
        par = parent[end_x][end_y]
        x = par.x
        y = par.y

        # the shortest path
        # we are travelling from the ending point to the starting point using the parent array
        while(not(x==start_x and y==start_y)):
            par = parent[x][y]

            #draw the shortest path on the canvas (graphics)
            draw(x, y, root, c, tiles, row_height, col_width, "green4")
            time.sleep(0.1)

            x = par.x
            y = par.y

        time.sleep(0.1)
