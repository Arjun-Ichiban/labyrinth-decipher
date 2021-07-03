import tkinter as tk

root = tk.Tk()


root.geometry("400x400")
  
# declaring string variable
# for storing name and password
ROWS=tk.IntVar()
COLS=tk.IntVar()
 
  
# defining a function that will
# get the name and password and
# print them on the screen
def submit():
 
    name=ROWS.get()
    password=COLS.get()
     
    print("The rows is : " + str(name))
    print("The columns is : " + str(password))

    root.destroy()

     
     
# creating a label for
# name using widget Label
rows_label = tk.Label(root, text = 'Rows', font=('calibre',10, 'bold'))
  
# creating a entry for input
# name using widget Entry
rows_entry = tk.Entry(root,textvariable = ROWS, font=('calibre',10,'normal'))
  
# creating a label for password
cols_label = tk.Label(root, text = 'Columns', font = ('calibre',10,'bold'), anchor='w')
  
# creating a entry for password
cols_entry=tk.Entry(root, textvariable = COLS, font = ('calibre',10,'normal'))
  
# creating a button using the widget
# Button that will call the submit function
sub_btn=tk.Button(root,text = 'Submit', command = submit)
  
# placing the label and entry in
# the required position using grid
# method
rows_label.grid(row=0,column=0)
rows_entry.grid(row=0,column=1)
cols_label.grid(row=1,column=0)
cols_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)

#c = tk.Canvas(root, width=330, height=330, borderwidth=0, background='black')

# performing an infinite loop
# for the window to display
root.mainloop()

ROWS = ROWS.get()
COLS = COLS.get()
root = tk.Tk()
c = tk.Canvas(root, width=ROWS*20, height=COLS*20, borderwidth=0, background='black')
c.pack()

col_width = 30
row_height = 30

root.mainloop()