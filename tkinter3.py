import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    current = entry.get()
    
    if text == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create an Entry widget
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="ridge")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Create and place buttons
for i, button in enumerate(buttons):
    b = tk.Button(root, text=button, width=5, height=2, font=('Arial', 18))
    row = (i // 4) + 1
    col = i % 4
    b.grid(row=row, column=col, padx=5, pady=5)
    b.bind("<Button-1>", click)

# Start the Tkinter event loop
root.mainloop()

