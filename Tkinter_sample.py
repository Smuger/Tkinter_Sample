from tkinter import *

class SharedPower(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        # title of the pages
        self.title("Shared Power")

        # store pages
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        # list of pages
        for F in (StartPage, ConnectPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)


    # this function stacks pages and displays the current one
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        Label(self, text="StartPage").pack()
        Button(self, text="Go to ConnectPage", command=lambda: controller.show_frame(ConnectPage)).pack()


class ConnectPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        Label(self, text="ConnectPage").pack()
        Button(self, text="Go to StartPage", command=lambda: controller.show_frame(StartPage)).pack()

if __name__ == "__main__":
    app = SharedPower()
    app.mainloop()


