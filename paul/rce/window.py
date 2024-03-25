import tkinter as tk

name_label = "Your name"

def print_name():
    print(name_label)

def window():
    window = tk.Tk()
    window.title = "Backdoor GUI"

    label1 = tk.Label(window, text="Enter your name below")
    label1.pack(padx=15, pady=10)

    label = tk.Label(window, textvariable=name_label)
    label.pack(padx=15, pady=10)

    text_input = tk.Entry(window, textvariable=name_label)
    text_input.pack(padx=15, pady=10)

    butt = tk.Button(text="Submit", command=print_name)
    butt.pack(padx=15, pady=10)
    return window
