import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import messagebox

#Title = input('Enter the name of the Recipe: ')
#Ingredients =  input('Enter the list of ingredients: ')
#Steps = input('Enter the steps: ')

#print("That's a great recipe!")

#print(f'Saved Recipe {Title}!')

def rec():
    Rn = Rname.get()
    Ig = Ingredients.get("1.0", "end-1c")
    St = Steps.get("1.0", "end-1c")

    recps.config(text = f"Title: {Rn}\nIngedients:\n {Ig}\nSteps :\n {St}")

def save_recipe():
    Rn = Rname.get()
    Ig = Ingredients.get("1.0", "end-1c")
    St = Steps.get("1.0", "end-1c")

    if Rn.strip() == "":
        messagebox.showwarning('Warning', 'Recipe Title cannot be empty!')
        return
    
    with open(f"{Rn}.txt", "w") as file:
        file.write(f"Title : {Rn}\n")
        file.write(f"Ingredients :\n {Ig}\n")
        file.write(f"Steps :\n {St}\n")

root = tk.Tk()
root.title('My Recipe App')
root.geometry('400x500')

tk.Label(root, text='Enter name of the recipe', font = ('Helvetica', 16)).pack(pady=10)
Rname = tk.Entry(root)
Rname.pack()

tk.Label(root, text='Enter Ingredients of the recipe', font = ('Helvetica', 16)).pack(pady=10)
Ingredients = tk.Text(root, width = 40, height = 5)
Ingredients.pack()

tk.Label(root, text='Enter Steps of the recipe', font = ('Helvetica', 16)).pack(pady=10)
Steps = tk.Text(root, width = 40, height = 5)
Steps.pack()

tk.Button(root, text = 'Show Recipe', command = rec).pack()
tk.Button(root, text='Save Recipe', command = save_recipe).pack(pady=5)

recps = tk.Label(root, text="")
recps.pack(pady=10)

root.mainloop()