import tkinter as tk
from tkinter import messagebox
import numpy as np

def calculate_basis():
    try:
        # Read input values
        rows = int(row_entry.get())
        cols = int(col_entry.get())
        
        # Validate input dimensions
        if rows <= 0 or cols <= 0:
            raise ValueError("Rows and columns must be positive integers.")
        
        matrix = []
        for r in range(rows):
            row_values = entry_fields[r].get().split(',')
            if len(row_values) != cols:
                raise ValueError(f"Row {r+1} does not have {cols} columns.")
            matrix.append([float(x) for x in row_values])
        
        matrix = np.array(matrix)
        _, basis = np.linalg.qr(matrix.T)
        basis = basis.T

        result_text.set(f"Basis:\n{basis}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Basis Calculator")

# Create and place widgets
tk.Label(root, text="Number of rows:").pack()
row_entry = tk.Entry(root)
row_entry.pack()

tk.Label(root, text="Number of columns:").pack()
col_entry = tk.Entry(root)
col_entry.pack()

def create_entries():
    global entry_fields
    for widget in entry_frame.winfo_children():
        widget.destroy()
    
    try:
        rows = int(row_entry.get())
        cols = int(col_entry.get())
        if rows <= 0 or cols <= 0:
            raise ValueError("Rows and columns must be positive integers.")
        
        entry_fields = []
        for r in range(rows):
            tk.Label(entry_frame, text=f"Row {r+1}:").pack()
            entry = tk.Entry(entry_frame)
            entry.pack()
            entry_fields.append(entry)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers of rows and columns.")

tk.Button(root, text="Create Entries", command=create_entries).pack()
entry_frame = tk.Frame(root)
entry_frame.pack()

tk.Button(root, text="Calculate Basis", command=calculate_basis).pack()

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify=tk.LEFT)
result_label.pack()

# Start the Tkinter event loop
root.mainloop()