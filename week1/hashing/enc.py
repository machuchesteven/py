import tkinter as tk

from tkinter import ttk

class MainApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self, height=500, width=500)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Startpage, Page1, Page2):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')
        self.show_frame(Startpage)
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class Startpage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Start page", )
        label.grid(row=1, column=1, padx=10, pady=10)
        button1 = ttk.Button(self, text="Page1", command=lambda : controller.show_frame(Page1))
        button1.grid(row=1, column=1, padx=10, pady=10)
        button2 = ttk.Button(self, text="Page2", command=lambda : controller.show_frame(Page2))
        button2.grid(row=2, column=1, padx=10, pady=10)


class Page1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page 1")
        label.grid(row=0, column=4, padx=10, pady=10)
        button1 = ttk.Button(self, text="Start page", command=lambda: controller.show_frame(Startpage))
        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="Page2", command=lambda: controller.show_frame(Page2))
        button2.grid(row=2, column=1, padx=10, pady=10)

class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page 2")
        label.grid(row=0, column=4, padx=10, pady=10)
        button1 = ttk.Button(self, text="Start page", command=lambda: controller.show_frame(Startpage))
        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="Page1", command=lambda: controller.show_frame(Page1))
        button2.grid(row=2, column=1, padx=10, pady=10)

app = MainApp()

app.mainloop()