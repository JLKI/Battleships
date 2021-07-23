import tkinter as tk


# renaming the process header name
app = tk.Tk(className=' Battleships')

# classifying the elements
leftFrame = tk.Frame(app)
rightFrame = tk.Frame(app)
bottomLabel = tk.Label(app, text="Welcome to the game, Click something")

# defining the game area
leftFrame.grid(row=0, column=0, padx=(10, 20), pady=10, ipady=0)
rightFrame.grid(row=0, column=1, padx=(20, 10), pady=10, ipady=0)
bottomLabel.grid(row=1, column=0, columnspan=2, padx=0, pady=(0, 10), ipadx=0)


# printing the location of pressed button
def click(row, col, table):
    bottomLabel.configure(text="You clicked row %s column %s on the %s table" % (row + 1, col + 1, table))


# spawning of the buttons
for x in range(10):
    for y in range(10):
        lbuttons = tk.Button(leftFrame, text="%s" % 'x', command=lambda row=x, col=y, table="Left": click(row, col, table))
        rbuttons = tk.Button(rightFrame, text="%s" % 'x', command=lambda row=x, col=y, table="Right": click(row, col, table))
        # Button(frame, text="x")
        lbuttons.grid(column=x, row=y, ipadx=10, ipady=10)
        rbuttons.grid(column=x, row=y, ipadx=10, ipady=10)


app.mainloop()
