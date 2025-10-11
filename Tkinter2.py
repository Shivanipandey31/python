import tkinter as tk

def show_selection():
    print("Selected" if var.get() else "Not Selected")

# Create the main window
root = tk.Tk()
root.title("Checkbutton Example")

# Create a variable to hold the state of the checkbutton
var = tk.IntVar()

# Create the checkbutton
checkbutton = tk.Checkbutton(root, text="Check me", variable=var, command=show_selection)
checkbutton.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()