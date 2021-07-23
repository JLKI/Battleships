import tkinter as tk

# renaming the process header name
app = tk.Tk(className=' Battleshipsv2')

# classifying the elements
leftFrame = tk.Frame(app)
rightFrame = tk.Frame(app)
bottomLabel = tk.Label(app, text="Welcome to the game, Click something")

# defining the game area
leftFrame.grid(row=0, column=0, padx=(10, 20), pady=10, ipady=0)
rightFrame.grid(row=0, column=1, padx=(20, 10), pady=10, ipady=0)
bottomLabel.grid(row=1, column=0, columnspan=2, padx=0, pady=(0, 10), ipadx=0)

mapgridsize = 10  # changeing the map grid size will break the game

# opponent ship location
eship = {"ship1": [[1], [1]],
         "ship2": [[2, 2], [2, 3]],
         "ship3": [[6, 7, 8], [3, 3, 3]],
         "ship4": [[4, 4, 4, 4], [6, 7, 8, 9]],
         "ship5": [[6, 7, 8, 9, 10], [9, 9, 9, 9, 9]]}


# Logic check
def click(row, col, table):
    rowb = row + 1
    colb = col + 1
    xukai = False
    for i in range(5):  # check through the ships
        if xukai:
            break
        else:
            for k in range(5):   # check through the ships
                valentino = str(row) + str(col)
                valentino = int(valentino)
                try:
                    if rowb == eship.get("ship%s" % (i + 1))[0][k] and colb == eship.get("ship%s" % (i + 1))[1][k]:  # check cell hit to each ship's value
                        
                        # if successfully hit a ship, turn cell light green
                        if table == "Right":
                            rbname = (rbutton_identities[int(valentino)])
                            rbname.configure(text="O", relief=tk.SUNKEN, background="lightgreen")
                        else:
                            lbname = (lbutton_identities[int(valentino)])
                            lbname.configure(text="O", relief=tk.SUNKEN, background="lightgreen")
                        print("You've hit a ship at ", eship.get("ship%s" % (i + 1))[0][k], eship.get("ship%s" % (i + 1))[1][k])
                        
                        xlocation = eship.get("ship%s" % (i + 1))[0][k]
                        ylocation = eship.get("ship%s" % (i + 1))[1][k]
                        bottomLabel.configure(text="You've hit a ship at %s %s" % (xlocation, ylocation))
                        xukai = True
                        break
                        
                except IndexError:
                    bottomLabel.configure(text="You clicked row %s column %s on the %s table" % (rowb, colb, table))
            else:
                bottomLabel.configure(text="You clicked row %s column %s on the %s table" % (rowb, colb, table))
                if table == "Right":
                    rbname = (rbutton_identities[int(valentino)])
                    rbname.configure(text="O", relief=tk.SUNKEN, background="red")
                else:
                    lbname = (lbutton_identities[int(valentino)])
                    lbname.configure(text="O", relief=tk.SUNKEN, background="red")


# spawning of the buttons
lbutton_identities = []
rbutton_identities = []
for x in range(mapgridsize):
    for y in range(mapgridsize):
        lbuttons = tk.Button(leftFrame, text="%s" % 'X', command=lambda row=x, col=y, table="Left": click(row, col, table))
        lbuttons.pack
        lbutton_identities.append(lbuttons)
        rbuttons = tk.Button(rightFrame, text="%s" % 'X', command=lambda row=x, col=y, table="Right": click(row, col, table))
        rbuttons.pack
        rbutton_identities.append(rbuttons)
        lbuttons.grid(column=x, row=y, ipadx=10, ipady=5)
        rbuttons.grid(column=x, row=y, ipadx=10, ipady=5)


app.mainloop()
