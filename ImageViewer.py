import os
from tkinter import *
from tkinter import filedialog as fd, filedialog

from PIL import ImageTk, Image


#  Build A Image Viewer Now
def move_app(e):
    # the "e.x_root == 500 and e.y_root == 300"
    root.geometry(f'+{e.x_root}+{e.y_root}')


# the function for X On title bar.
def quitter():
    root.quit()


class image_viewer:

    def __init__(self, master):
        self.canvas = None
        self.wt = None
        self.pilImage = None
        self.status = None
        self.savefile = None
        self.master = master
        self.c_size = (700, 500)
        self.setup_gui(self.c_size)
        self.img = None

    def setup_gui(self, s):
        Label(self.master, text='Image Viewer', pady=5, bg='white', font=('Arial', 30)).pack()
        self.canvas = Canvas(self.master, height=s[1], width=s[0], bg='Black', bd=10, relief='ridge')
        self.canvas.pack()
        txt = ''' 
                                                By Rihan Bagwan 
                                '''
        self.wt = self.canvas.create_text(s[0] / 2 - 270, s[1] / 2, text=txt, font=('', 30), fill='white')
        f = Frame(self.master, bg='white', padx=10, pady=10)
        Button(f, text='Open Image', bd=2, fg='white', bg='black', font=('', 15), command=self.make_image).pack(
            side=LEFT)
        #
        Button(f, text='Exit Image', bd=2, fg='white', bg='green', font=('', 15), command=root.quit).pack(
            side=LEFT)
        f.pack()

    def make_image(self):
        File = fd.askopenfilename(initialdir=os.getcwd(), title="Select Image file",
                                  filetypes=(("JPG FILE", "*.jpg"), ("PNG FILE", "*.png"),
                                             ("ALL FILE", "*.*")))
        self.pilImage = Image.open(File)
        re = self.pilImage.resize((700, 500), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(re)
        self.canvas.delete(ALL)
        self.canvas.create_image(self.c_size[0] / 2 + 10, self.c_size[1] / 2 + 10, anchor=CENTER, image=self.img)
        self.status['text'] = 'Current Image:' + File


root = Tk()
# removing in-built title bar
root.overrideredirect(True)
# adding customize title bar
# customize title bar creation Using a frame and adding some bg color and border none
title_bar = Frame(root, bg="darkgreen", relief="raised", bd=0, padx=5, pady=5)
title_bar.pack(side=TOP, expand=1, fill=X)
# Bind the title bar
title_bar.bind("<B1-Motion>", move_app)
# Added the name of the app at title bar
title_label = Label(title_bar, text="  Image Viewer  ", bg="darkgreen", fg='black', font=('Arial', 10))
title_label.pack(side=LEFT, pady=2)

# close button on titlle bar
close_label = Label(title_bar, text=" X ", bg="darkgreen", fg="white", relief="raised", bd=1)
close_label.pack(side=RIGHT, pady=4)
close_label.bind("<Button-1>", quitter)
root.configure(bg='white')
root.title('Image Viewer')
image_viewer(root)
root.resizable(True, True)
root.mainloop()
