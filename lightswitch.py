import random
import tkinter as tk
window = tk.Tk()

button = tk.Button(text='...', bg="white", fg="black")
button.pack(pady = 20, padx = 20)

# schijf hier tussen je code
Color = ['Red','Green','Blue','Yellow','Orange','Pink','Purple','Magenta','Turquoise']
window['bg'] = 'black'

def clickButton(event):
    button.config(text=' light on')
    print ("light is on")
    window['bg'] = random.choice(Color)
button.bind("<Button-1>", clickButton)

def clickButton1(event):
    button.config(text=' light off')
    print ("light is off")
    window['bg'] = random.choice(Color)
button.bind("<Button-3>", clickButton1)

# schijf hier tussen je code

window.mainloop()