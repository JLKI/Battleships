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

# ship location test
pship = {"ship1": [[1], [1]],
         "ship2": [[2, 2], [2, 3]],
         "ship3": [[6, 7, 8], [3, 3, 3]],
         "ship4": [[5, 5, 5, 5], [6, 7, 8, 9]],
         "ship5": [[6, 7, 8, 9, 10], [8, 8, 8, 8, 8]]}


# Logic check
def click(row, col, table):
    row = row + 1
    col = col + 1
    xukai = False
    for i in range(5):
        if xukai:
            break
        else:
            for k in range(5):
                try:
                    if row == pship.get("ship%s" % (i + 1))[0][k] and col == pship.get("ship%s" % (i + 1))[1][k]:
                        print("Hit ship%s at " % (i + 1), pship.get("ship%s" % (i + 1))[0][k], pship.get("ship%s" % (i + 1))[1][k])
                        xlocation = pship.get("ship%s" % (i + 1))[0][k]
                        ylocation = pship.get("ship%s" % (i + 1))[1][k]
                        bottomLabel.configure(text="Hit ship%s at %s %s" % (i + 1, xlocation, ylocation))
                        xukai = True
                        break
                except IndexError:
                    bottomLabel.configure(text="You clicked row %s column %s on the %s table" % (row, col, table))
            else:
                print('boo')
                bottomLabel.configure(text="You clicked row %s column %s on the %s table" % (row, col, table))


# spawning of the buttons
for x in range(10):
    for y in range(10):
        lbuttons = tk.Button(leftFrame, text="%s" % 'x', command=lambda row=x, col=y, table="Left": click(row, col, table))
        rbuttons = tk.Button(rightFrame, text="%s" % 'x', command=lambda row=x, col=y, table="Right": click(row, col, table))
        # Button(frame, text="x")
        lbuttons.grid(column=x, row=y, ipadx=10, ipady=10)
        rbuttons.grid(column=x, row=y, ipadx=10, ipady=10)

app.mainloop()
