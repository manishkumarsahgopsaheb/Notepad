from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

window = Tk()
window.geometry('752x600')
window.title("*Untitled-Notepad")
window.config(bg="white")


# window.iconbitmap()

def newfunc():
    pass


def newfile():
    global file
    window.title("untitled - Notepad")
    file = None
    text_Widget.delete(1.0, END)


def newwindow():
    pass

def openfile():
    global file
    file = askopenfilename(defaultextension=".txt", filetype=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        window.title(os.path.basename(file) + " - Notepad")
        text_Widget.delete(1.0, END)
        f = open(file, "r")
        text_Widget.insert(1.0, f.read())
        f.close()


def savefile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                 filetype=[("All Files", "*.*"), ("Text Documents", "*.txt")])

        if file == "":
            file = None
        else:
            # save as a new file
            f = open(file, "w")
            f.write(text_Widget.get(1.0, END))
            f.close()

            window.title(os.path.basename(file) + " - Notepad")
            print("file save")
    else:
        # save the file
        f = open(file, "w")
        f.write(text_Widget.get(1.0, END))
        f.close()


def saveasfile():
    global file
    file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                             filetype=[("All Files", "*.*"), ("Text Documents", "*.txt")])

    if file == "":
        file = None
    else:
        # save as a new file
        f = open(file, "w")
        f.write(text_Widget.get(1.0, END))
        f.close()

        window.title(os.path.basename(file) + " - Notepad")
        print("file save")


def undo():
    pass


def cut():
    text_Widget.event_generate("<<Cut>>")


def copy():
    text_Widget.event_generate("<<Copy>>")


def paste():
    text_Widget.event_generate("<<Paste>>")


def delete():
    pass


def about():
    showinfo("Notepad", "Notepad by Manish Kumar Sah")


#############################################
# creating main menu

main_menu = Menu(window)

m1 = Menu(main_menu, tearoff=0)
m1.add_command(label="New", command=newfile)
m1.add_command(label="New Window", command=newwindow)
m1.add_command(label="Open", command=openfile)
m1.add_command(label="Save", command=savefile)
m1.add_command(label="Save As...", command=saveasfile)
m1.add_separator()
m1.add_command(label="Page Setup...", command=newfunc)
m1.add_command(label="Print...", command=newfunc)
m1.add_separator()
m1.add_command(label="Exit", command=quit)
window.config(menu=main_menu)
main_menu.add_cascade(label="File", menu=m1)

m2 = Menu(main_menu, tearoff=0)
m2.add_command(label="Undo", command=undo)
m2.add_separator()
m2.add_command(label="Cut", command=cut)
m2.add_command(label="Copy", command=copy)
m2.add_command(label="Paste", command=paste)
m2.add_command(label="Delete", command=delete)
m2.add_separator()
m2.add_command(label="Search with Bing...", command=newfunc)
m2.add_command(label="Find...", command=newfunc)
m2.add_command(label="Find Next", command=newfunc)
m2.add_command(label="Find Previous", command=newfunc)
m2.add_command(label="Replace", command=newfunc)
m2.add_command(label="Go To...", command=newfunc)
m2.add_separator()
m2.add_command(label="Select All", command=newfunc)
m2.add_command(label="Time/Date", command=newfunc)
window.config(menu=main_menu)
main_menu.add_cascade(label="Edit", menu=m2)

m3 = Menu(main_menu, tearoff=0)
m3.add_command(label="Word Wrap", command=newfunc)
m3.add_command(label="Font...", command=newfunc)
window.config(menu=main_menu)
main_menu.add_cascade(label="Format", menu=m3)

m4 = Menu(main_menu, tearoff=0)
m4.add_command(label="Zoom", command=newfunc)
m4.add_command(label="Status Bar", command=newfunc)
window.config(menu=main_menu)
main_menu.add_cascade(label="View", menu=m4)

m5 = Menu(main_menu, tearoff=0)
m5.add_command(label="View Help", command=newfunc)
m5.add_command(label="Send Feedback", command=newfunc)
m5.add_separator()
m5.add_command(label="About Notepad", command=about)
window.config(menu=main_menu)
main_menu.add_cascade(label="Help", menu=m5)

# end of main menu
######################################


# creating a text widget

text_Widget = Text(window, bd=0, font="Lucida 12 normal")
text_Widget.pack(fill=BOTH, expand=True)

file = None;

# adding scroll view in text area

scroll = Scrollbar(text_Widget)
scroll.pack(side=RIGHT, fill=Y)
scroll.config(command=text_Widget.yview)
text_Widget.config(yscrollcommand=scroll.set)

window.mainloop()
