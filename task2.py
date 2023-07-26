from tkinter import *


def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(scvalue.get())

        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()
root.geometry("500x700")
root.title("Calculator")
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

f1 = Frame(root, bg="light blue")
b = Button(f1, text="9", padx=5, pady=4, font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=8, pady=8)
b = Button(f1, text="8", padx=5, pady=4, font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=8, pady=8)
b = Button(f1, text="7", padx=5, pady=4, font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=8, pady=8)
b = Button(f1, text="6", padx=5, pady=4, font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=8, pady=8)
f1.pack()


f1 = Frame(root, bg="light blue")
b = Button(f1, text="5", padx=5, pady=4, font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=8, pady=8)
b = Button(f1, text="4", padx=5, pady=4, font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=8, pady=8)
b = Button(f1, text="3", padx=5, pady=4, font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=8, pady=8)
b = Button(f1, text="2", padx=5, pady=4, font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=8, pady=8)
f1.pack()


f1 = Frame(root, bg="light blue")
b = Button(f1, text="1", padx=6.1, pady=4, font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=8, pady=8)
b = Button(f1, text="0", padx=6.1, pady=4, font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=8, pady=8)
b = Button(f1, text="+", padx=6.1, pady=4, font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=8, pady=8)
b = Button(f1, text="-", padx=6.3, pady=4, font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=8, pady=8)
f1.pack()


f1 = Frame(root, bg="light blue")
b = Button(f1, text="*", padx=7, pady=4, font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=8, pady=8)
b = Button(f1, text="=", padx=5, pady=4, font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=8, pady=8)
b = Button(f1, text="/", padx=5, pady=4, font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=8, pady=8)
b = Button(f1, text="%", padx=5, pady=4, font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=8, pady=8)
f1.pack()


f1 = Frame(root, bg="light blue")
b = Button(f1, text="C", padx=8, pady=4, font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=8, pady=8)
b = Button(f1, text=".", padx=8, pady=4, font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=8, pady=8)
b = Button(f1, text="(", padx=8, pady=4, font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=8, pady=8)
b = Button(f1, text=")", padx=8.3, pady=4, font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=8, pady=8)
f1.pack()


root.mainloop()
