import tkinter as tk
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))
def button_operator(op):
    global operator
    global first_number
    operator = op
    first_number = float(entry.get())
    entry.delete(0, tk.END)
def button_clear():
    entry.delete(0, tk.END)

# Function to calculate result
def button_equal():
    second_number = float(entry.get())
    entry.delete(0, tk.END)
    if operator == '+':
        result = int(first_number + second_number)
    elif operator == '-':
        result = int(first_number - second_number)
    elif operator == '*':
        result = int(first_number * second_number)
    elif operator == '/':
        if second_number == 0:
            result = "Error: Division by zero"
        else:
            result = first_number / second_number
    entry.insert(0, result)
root = tk.Tk()
root.title("Simple Calculator")
entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]
for button_text, row, column in buttons:
    if button_text == '=':
        button = tk.Button(root, text=button_text, padx=40, pady=20, command=button_equal)
    elif button_text == 'C':
        button = tk.Button(root, text=button_text, padx=40, pady=20, command=button_clear)
    elif button_text in '+-*/':
        button = tk.Button(root, text=button_text, padx=40, pady=20, command=lambda x=button_text: button_operator(x))
    else:
        button = tk.Button(root, text=button_text, padx=40, pady=20, command=lambda x=button_text: button_click(x))
    button.grid(row=row, column=column)
root.mainloop()
