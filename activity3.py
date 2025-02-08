from tkinter import*

root = Tk()
root.geometry("400x400")
root.title("main")

def topwin():
    top= Toplevel()
    top.geometry("180x100")
    top.title("toplevel")

    label2 = Label(top, text = "This is toplevel window")
    label2.pack()

    top.mainloop()

label = Label(root, text = "This is root window")
button = Button(root, text = "Click here to open another window" , command = topwin)

label.pack()
button.pack()
root.mainloop()