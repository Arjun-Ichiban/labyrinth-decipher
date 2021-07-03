import tkinter as tk
from maze_generator import *
from maze_solver import *

# ---input rows and columns from the user---

# create the graphics window  
root = tk.Tk()
root.title("Labyrinth Decipher")
root.geometry("300x100")

# declaring int variable for storing rows and cols
ROWS = tk.StringVar()
COLS = tk.StringVar()

def submit():
    root.destroy()

# creating a label for rows using widget Label
rows_label = tk.Label(root, text = 'Number Of Rows', font=('calibre',10, 'bold'))

# creating a entry for input rows using widget Entry
rows_entry = tk.Entry(root,textvariable = ROWS, font=('calibre',10,'normal'))
  
# creating a label for columns
cols_label = tk.Label(root, text = 'Number Of Columns', font = ('calibre',10,'bold'))
  
# creating a entry for password
cols_entry = tk.Entry(root, textvariable = COLS, font = ('calibre',10,'normal'))
  
# creating a button using the widget
# Button that will call the submit function
sub_btn = tk.Button(root, text = 'Submit', command = submit)


# placing the label and entry in the required position using grid method
rows_label.grid(row=0,column=0, sticky='w')
rows_entry.grid(row=0,column=1)
cols_label.grid(row=1,column=0)
cols_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1) 

root.mainloop()

# ---end of input of rows and colums---


# ---Creat and Solve the maze---

#rows and cols in int type
rows = int(ROWS.get())
cols = int(COLS.get())

#we need the rows and cols to be odd
if rows%2==0:
    rows+=1

if cols%2==0:
    cols+=1

#size of each tile
col_width = 20
row_height = 20

# Create a grid of None to store the references to the tiles
tiles = [[None for _ in range(cols)] for _ in range(rows)]

# window for the maze generation
root = tk.Tk()
root.title("Labyrinth Decipher")

# canvas to draw the maze
c = tk.Canvas(root, width=cols*col_width, height=rows*row_height, borderwidth=0, background='black')
c.pack()

# maze is generated
grid = createMaze(rows, cols, root, c, tiles,  row_height, col_width)

# get the starting and ending point from the user through the graphics
start_x = 0
start_y = 0
end_x = rows-1
end_y = cols-1

# to keep track so that the user can select only 2 points
count  = 0

def callback(event):
    global count
    global start_x, start_y, end_x, end_y
    
    # Calculate column and row number
    col = int(event.x//col_width)
    row = int(event.y//row_height)

    # Check if the selected tile is a path
    if grid[row][col]==1:
        count=count+1
        # the first selected point is the starting point
        if count==1:
            start_x = row
            start_y = col
        # the second selected point is the ending point
        else:
            end_x = row
            end_y = col
        
        # mark the starting and ending point
        tiles[row][col] = c.create_rectangle(col*col_width, row*row_height, (col+1)*col_width, (row+1)*row_height, fill="green4")
        tiles[row][col] = c.create_oval(col*col_width, row*row_height, (col+1)*col_width, (row+1)*row_height, fill="green4")
        root.update_idletasks()               
        root.update()

    # if count == 2:
    # solve the maze -> finds the shortes path
    if count == 2:
        time.sleep(0.4)
        solveMaze(rows, cols, grid, root, c, tiles, row_height, col_width, start_x, start_y, end_x, end_y)
        c.unbind("<Button-1>")

c.bind("<Button-1>", callback)
    
root.mainloop()