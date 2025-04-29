import tkinter as tk
from tkinter import messagebox
import pandas as pd

def calculate_bmi():
    try:
        height = float(entry_height.get())
        weight = float(entry_weight.get())
        bmi = round(weight / (height ** 2), 2)

        if bmi < 18.5:
            status = 'Underweight'
        elif 18.5 <= bmi <= 24.9:
            status = 'Normal Weight'
        elif 25.0 <= bmi <= 29.9:
            status = 'Overweight'
        elif 30.0 <= bmi <= 34.9:
            status = 'Obesity Class I'
        elif 35.0 <= bmi <= 39.9:
            status = 'Obesity Class II'
        else:
            status = 'Obesity Class III'

        result_label.config(text=f"BMI: {bmi} - {status}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for height and weight.")

def show_bmi_chart():
    val = ['Below 18.5','18.5 to 24.9', '25.0 to 29.9', '30.0 to 34.9', '35.0 to 39.9', 'Above 40.0']
    stt = ['Underweight', 'Normal Weight', 'Overweight', 'Obesity Class I', 'Obesity Class II', 'Obesity Class III']
    Bdf = pd.DataFrame({'BMI Range': val, 'Weight Status': stt})

    # Create a new window for the chart
    chart_window = tk.Toplevel(root)
    chart_window.title("BMI Chart")
    chart_window.geometry("300x200")

    chart_text = tk.Text(chart_window, wrap=tk.WORD, width=40, height=10)
    chart_text.pack(pady=10)
    chart_text.insert(tk.END, Bdf.to_string(index=False))
    chart_text.config(state=tk.DISABLED)

# Main Window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x250")

tk.Label(root, text="Enter Height (m):").pack(pady=5)
entry_height = tk.Entry(root)
entry_height.pack()

tk.Label(root, text="Enter Weight (kg):").pack(pady=5)
entry_weight = tk.Entry(root)
entry_weight.pack()

tk.Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=10)
result_label = tk.Label(root, text="")
result_label.pack()

tk.Button(root, text="Show BMI Chart", command=show_bmi_chart).pack(pady=10)

root.mainloop()
