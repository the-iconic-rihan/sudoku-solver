from tkinter import *

root = Tk()
root.title("Image Viewer")
root.geometry("500x300")
# remove title bar
root.overrideredirect(True)


def move_app(e):
    # the "e.x_root == 500 and e.y_root == 300"
    root.geometry(f'+{e.x_root}+{e.y_root}')


def quitter(e):
    root.quit()


# fake title bar creation Using a frame and adding some bg color and border none
title_bar = Frame(root, bg="darkgreen", relief="raised", bd=0)

title_bar.pack(expand=1, fill=X)

# Bind the title bar
title_bar.bind("<B1-Motion>", move_app)
# Added the name of the app at title bar
title_label = Label(title_bar, text="Image Viewer", bg="darkgreen", fg='white')
title_label.pack(side=LEFT, pady=2)
# close button on titlle bar
close_label = Label(title_bar, text=" X ", bg="darkgreen", fg="white", relief="raised", bd=0)
close_label.pack(side=RIGHT, pady=4)
close_label.bind("<Button-1>", quitter)
my_button = Button(root, text="CLOSE!", font=("Helvetica,32"), command=root.quit)
my_button.pack(pady=100)

root.mainloop()
