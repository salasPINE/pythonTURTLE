import tkinter as tk

window = tk.Tk()
window.title("Hello World")
window.geometry("200x100")

hello = tk.Label(text="Hello world!")
hello.pack()
button = tk.Button(text="Click me!")
button.pack()

tk.mainloop()