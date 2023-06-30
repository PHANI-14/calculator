import tkinter as tk

def button_click(num):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + num)

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

window = tk.Tk()
window.title("Calculator")

entry = tk.Entry(window, width=25, justify=tk.RIGHT)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("0", 4, 0),
]

for button_data in buttons:
    button_text, row, column = button_data
    button = tk.Button(window, text=button_text, width=5, command=lambda text=button_text: button_click(text))
    button.grid(row=row, column=column)

operators = [
    ("+", 1, 3),
    ("-", 2, 3),
    ("*", 3, 3),
    ("/", 4, 3),
    ("=", 4, 2),
    ("C", 4, 1),
]

for operator_data in operators:
    operator_text, row, column = operator_data
    operator = tk.Button(window, text=operator_text, width=5)
    if operator_text == "=":
        operator.config(command=button_equal)
    elif operator_text == "C":
        operator.config(command=button_clear)
    else:
        operator.config(command=lambda text=operator_text: button_click(text))
    operator.grid(row=row, column=column)

window.mainloop()
