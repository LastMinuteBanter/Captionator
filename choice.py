from tkinter import *
from Login import printName


root = Tk()

instructions = Label(root, text="What would you like to do today ?")
status_update =Button(root, text= "Status Update")
upload_picture = Button(root, text="Upload a picture")



status_update.grid(row=1, column=0)
upload_picture.grid(row=1, column=1)
instructions.grid(row=0)


root.mainloop()