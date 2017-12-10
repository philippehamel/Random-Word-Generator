import tkinter as tk
from functions import random_word


def word():
    label.configure(text=random_word())


window = tk.Tk()
window.title("Générateur de mots")
window.configure(bd=10)

label = tk.Label(window, text="", width=30)
label.grid()
label.configure(font=('Courrier', 40))

button = tk.Button(window, text="Changer", command=word)
button.grid(row=1)

quit = tk.Button(window, text='Quitter', command=window.quit)
quit.grid(row=2)

window.mainloop()
