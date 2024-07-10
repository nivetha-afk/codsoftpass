import tkinter as tk
import random
import string

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    status_label.config(text="Password copied to clipboard!")

def generate_and_display_password():
    length = int(length_entry.get())
    password = generate_password(length)
    password_entry.delete(0, tk.END)
    password_entry.insert(tk.END, password)
    status_label.config(text="Password generated!")

root = tk.Tk()
root.title("Password Generator")

# Length label and entry
length_label = tk.Label(root, text="Length:")
length_label.grid(row=0, column=0)
length_entry = tk.Entry(root, width=5)
length_entry.grid(row=0, column=1)

# Generate button
generate_button = tk.Button(root, text="Generate", command=generate_and_display_password)
generate_button.grid(row=0, column=2)

# Password entry
password_entry = tk.Entry(root, width=90)
password_entry.grid(row=1, column=0, columnspan=3)

# Copy button
copy_button = tk.Button(root, text="Copy", command=copy_password)
copy_button.grid(row=2, column=0)

# Status label
status_label = tk.Label(root, text="")
status_label.grid(row=2, column=1, columnspan=2)

root.mainloop()

