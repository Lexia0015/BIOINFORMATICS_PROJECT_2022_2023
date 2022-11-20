import tkinter as tk

class MainApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        # the main container that holds all the frames
        container = tk.Frame(self)

        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0,weight = 1)


        self.frames = {}

        # adding frames to the dictionary
        for F in (Page1,Page2,Page3):

             frame = F(container,self)

             self.frames[F] = frame

             frame.grid(row = 0, column = 0, sticky = "w")

        self.show_frame(Page1)

    def show_frame(self,page_name):

        #SHOWS A FRAME WITH THE GIVEN NAME
        for frame in self.frames.values():
            frame.grid_remove()
        frame = self.frames[page_name]
        frame.grid()

    #STACKING THE FRAMES
    #frame = self.frames[cont]
    #frame.tkraise()

class Page1(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller

        lbl1 = tk.Label(self,text = "for page 2",font =("Helvetica",12,"bold"))
        lbl1.grid(row=1,sticky="W")

        lbl2 = tk.Label(self,text = "for page 3",font =("Helvetica",12,"bold"))
        lbl2.grid(row=1,column=1,sticky="W")

        btn1 = tk.Button(self, text="next page", font=('MS', 24, 'bold'))
        btn1.grid(row=3,column = 0,columnspan=1)
        #btn1['command'] = lambda: controller.show_frame(Page2)


        self.var1 = tk.BooleanVar()

        #rButton1 = tk.Button(self, text='Show Page 2', command=lambda: self.controller.show_frame(Page2))
        #rButton1.grid(row=2, sticky="W")
        #rButton2 = tk.Button(self, text='Show Page 3', command=lambda: self.controller.show_frame(Page3))
        #rButton2.grid(row=2, column=1, sticky="W")

        rButton1 = tk.Radiobutton(self,variable = self.var1,value=True,
            command=self.switch_pages)
        rButton1.grid(row=2,sticky = "W")

        rButton2 = tk.Radiobutton(self,variable = self.var1,value=False,
            command=self.switch_pages)
        rButton2.grid(row=2,column=1,sticky = "W")

    def switch_pages(self):

        if not self.var1.get():
            self.controller.show_frame(Page3)
        else:
            self.controller.show_frame(Page2)


class Page2(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        lbl = tk.Label(self,text="This is page 2",font=("Helvetica",12,"bold"))
        lbl.pack()


class Page3(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        lbl = tk.Label(self,text="This is page 3",font=("Helvetica",12,"bold"))
        lbl.pack()

app = MainApp()
app.mainloop()