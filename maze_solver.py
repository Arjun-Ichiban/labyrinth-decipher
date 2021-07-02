#Solve a maze using Dijstra's Algorithm

import sys
import heapq

#Distance class is stores the distance of the cell form the entry point (used in heap)
class Distance:
    def __init__(self, x, y, dis):
        self.x = x
        self.y = y
        self.dis = dis

    def __lt__(self, nxt):
        return self.dis < nxt.dis

#Stores the coordinates of the cell
class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

infinite = sys.maxsize

#the cell which can be reached from a given cell
direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

# grid = []
grid=[
[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
[0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
[0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
[0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
[0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
[0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
[0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0],
[0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
[0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
]

#dist array stores the minimum distance of each cell from the starting point 
dist = []
#parent array stores the cell from which it was connected to
parent = []

#we initialize the dist array to infinite since at the beginning every path cell is unvisited
#and parent as -1, -1
def initializeArrays(rows, cols):
    global dist, parent
    dist=[[infinite for x in range(rows)] for y in range(cols)]
    # for i in range(rows):
    #     for j in range(cols):
    #         dist[i][j] = infinite
    

    parent=[[Cell(-1, -1) for x in range(rows)] for y in range(cols)]
    # for i in range(rows):
    #     for j in range(cols):
    #         parent[i][j] = 
    
    

def valid(x, y):
    return x>=0 and x<len(grid) and y>=0 and y<len(grid[0])

def solveMaze(rows, cols):

    initializeArrays(rows, cols)

    dist[0][0] = 0

    heap = []
    heapq.heappush(heap, Distance(0, 0, 0))

    while(len(heap)):
        min = heapq.heappop(heap)

        for d in direction:
            x = min.x+d[0]
            y = min.y+d[1]

            if(valid(x, y) and grid[x][y]==1):
                if(min.dis+1<dist[x][y]):
                    dist[x][y] = min.dis+1
                    parent[x][y] = Cell(min.x, min.y)
                    heapq.heappush(heap, Distance(x, y, dist[x][y]))

    if(dist[rows-1][cols-1]==max):
        print("Path Not Found")
    else:
        finalPath=[[0 for x in range(rows)] for y in range(cols)]
        x = rows-1
        y = cols-1

        while(not(x==0 and y==0)):
            finalPath[x][y] = 1
            par = parent[x][y]
            x = par.x
            y = par.y

        finalPath[0][0] = 1

        for i in range(rows):
            for j in range(cols):
                print(finalPath[i][j], end=" ")
            print("\n")


solveMaze(11, 11)