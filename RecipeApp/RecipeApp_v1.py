import pandas as pd
import numpy as np
import tkinter as tk


#Title = input('Enter the name of the Recipe: ')
#Ingredients =  input('Enter the list of ingredients: ')
#Steps = input('Enter the steps: ')

#print("That's a great recipe!")

#print(f'Saved Recipe {Title}!')

def rec():
    Rn = Rname.get()
    Ig = Ingredients.get()
    St = Steps.get()

    recps.config(text = f"Title: {Rn}\nIngedients: {Ig}\nSteps: {St}")

root = tk.Tk()
root.title('My Recipe App')
root.geometry('400x500')

tk.Label(root, text='Enter name of the recipe', font = ('Helvetica', 16)).pack(pady=10)
Rname = tk.Entry(root)
Rname.pack()

tk.Label(root, text='Enter Ingredients of the recipe', font = ('Helvetica', 16)).pack(pady=10)
Ingredients = tk.Entry(root)
Ingredients.pack()

tk.Label(root, text='Enter Steps of the recipe', font = ('Helvetica', 16)).pack(pady=10)
Steps = tk.Entry(root)
Steps.pack()

tk.Button(root, text = 'Save', command = rec).pack()

recps = tk.Label(root, text="")
recps.pack()

root.mainloop()