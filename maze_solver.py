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
    parent=[[Cell(-1, -1) for x in range(rows)] for y in range(cols)]
    
    
#check if it is a valid cell
def valid(x, y):
    return x>=0 and x<len(grid) and y>=0 and y<len(grid[0])

def solveMaze(rows, cols):

    initializeArrays(rows, cols)

    dist[0][0] = 0

    #Dijstra's algorithm using heap data structure
    heap = []
    heapq.heappush(heap, Distance(0, 0, 0))

    while(len(heap)):
        #take the minimum distance
        min = heapq.heappop(heap)

        #find it's adjacent cell
        for d in direction:
            x = min.x+d[0]
            y = min.y+d[1]
 
            #if the adjacent cell is valid and it is a path check it's distance and new distance
            if(valid(x, y) and grid[x][y]==1):
                #if the new distance is lesser than update the dist array and add it to the heap 
                if(min.dis+1<dist[x][y]):
                    dist[x][y] = min.dis+1
                    parent[x][y] = Cell(min.x, min.y)
                    heapq.heappush(heap, Distance(x, y, dist[x][y]))

    #Print the path if it exist's
    if(dist[rows-1][cols-1]==max):
        print("Path Not Found")
    else:
        finalPath=[[0 for x in range(rows)] for y in range(cols)]
        x = rows-1
        y = cols-1

        #to find the shortest path
        #we are travelling from the ending point to the starting point using the parent array
        while(not(x==0 and y==0)):
            finalPath[x][y] = 1
            par = parent[x][y]
            x = par.x
            y = par.y

        finalPath[0][0] = 1

        #print the finalpath array 
        for i in range(rows):
            for j in range(cols):
                print(finalPath[i][j], end=" ")
            print("\n")


solveMaze(11, 11)