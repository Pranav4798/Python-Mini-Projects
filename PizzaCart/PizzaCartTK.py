import tkinter
import tkinter as tk
from tkinter import messagebox


items = ['Margherita', 'Supreme', '5 Cheese', 'Meat Monster', 'Garden']
costs = [14.25, 18.50, 18, 19, 17.50]
menu = dict(zip(items, costs))

cart = []
prices = []

def add_to_cart():
    selected = pizza_var.get()
    if selected:
        cart.append(selected)
        prices.append(menu[selected])
        update_cart()

def update_cart():
    cart_text.delete('1.0', tk.END)
    for item, price in zip(cart, prices):
        cart_text.insert(tk.END, f'{item} - ${price:.2f}\n')
    total = sum(prices)
    tax = total * 0.10
    final = total + tax
    total_label.config(text=f'Total: ${total:.2f}\nTax (10%): ${tax:.2f}\nGrand Total: ${final:.2f}')

def checkout():
    if not cart:
        messagebox.showwarning('Cart Empty', 'Add at least one item to checkout')
        return
    msg = "\n".join(f'{item} - ${price:.2f}' for item, price in zip(cart, prices))
    total = sum(prices)
    tax = total * 0.10
    final = total + tax
    msg += f"\n\nTotal: ${total:.2f}\nTax (10%): ${tax:.2f}\nGrand Total: ${final:.2f}"
    messagebox.showinfo("Your Receipt", msg)

root = tk.Tk()
root.title("Pizza Cart Ordering App - Order Now")
root.geometry('400x500')

tk.Label(root, text='Welcome to the Pizza Cart!', font = ('Helvetica', 16)).pack(pady=10)

pizza_var = tk.StringVar()
pizza_var.set(items[0])
tk.Label(root, text = 'Choose your pizza: ').pack()
tk.OptionMenu(root, pizza_var, *items).pack()

tk.Button(root, text = 'Add to Cart', command=add_to_cart).pack(pady=5)

tk.Label(root, text='Your Cart: ').pack()
cart_text = tk.Text(root, height= 10, width=40)
cart_text.pack()

total_label = tk.Label(root, text = "Total: $0.00\nTax: $0.00\nGrand Total: $0.00", font=("Helvetica", 12))
total_label.pack(pady=10)

tk.Button(root, text="Checkout", command=checkout, bg='green', fg='white').pack(pady=5)

root.mainloop()