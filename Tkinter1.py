# import tkinter as tk
# root=tk.Tk() #main window
# name_label=tk.Label(root, text="Enter name")
# name_label.pack()
# text_box=tk.Entry(root)
# text_box.pack()

# email_label=tk.Label(root, text="Enter email")
# email_label.pack()
# email_text_box=tk.Entry(root)
# email_text_box.pack()
# root.mainloop()


# import tkinter as tk
# from tkinter import messagebox

# def login():
#     user_id = entry_user_id.get()
#     password = entry_password.get()
    # For demonstration purposes, we are just printing the values
    # In a real-world application, you would check these against a database or other authentication system
    # if user_id and password:
    #     messagebox.showinfo("Login", "Login successful!")
    # else:
    #     messagebox.showwarning("Login", "Please enter both User ID and Password.")

# Create the main window
# root = tk.Tk()
# root.title("Login Form")

# Create and place the labels and entry fields
label_user_id = tk.Label(root, text="User ID:")
label_user_id.pack(pady=(0, 0))

entry_user_id = tk.Entry(root)
entry_user_id.pack(pady=(0, 10))

label_password = tk.Label(root, text="Password:")
label_password.pack(pady=(10, 0))

entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=(0, 10))

# Create and place the login button
login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=(10, 10))

# Run the application
root.mainloop()
