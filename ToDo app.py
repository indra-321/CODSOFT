import tkinter as tk
import json
from tkinter import messagebox
from PIL import Image, ImageTk



def save_todo_list():
    with open("todo_list.json", "w") as f:
        json.dump(todo_listbox.get(0, tk.END), f)

def add_todo():
    todo = todo_entry.get()
    if todo:
        todo_listbox.insert(tk.END, todo)
        todo_entry.delete(0, tk.END)
        save_todo_list()
    else:
        tk.messagebox.showwarning("Warning", "Please enter a task.")

def edit_todo():
    selected_index = todo_listbox.curselection()
    if selected_index:
        selected_task = todo_listbox.get(selected_index)
        edit_window = tk.Toplevel(root)
        edit_window.title("Edit Task")
        edit_entry = tk.Entry(edit_window, width=40)
        edit_entry.insert(tk.END, selected_task)
        edit_entry.pack(padx=10, pady=10)

        def save_edited_task():
            new_task = edit_entry.get()
            todo_listbox.delete(selected_index)
            todo_listbox.insert(selected_index, new_task)
            save_todo_list()
            edit_window.destroy()

        save_button = tk.Button(edit_window, text="Save", command=save_edited_task)
        save_button.pack(padx=10, pady=10)

def delete_todo(event=None):  # Make the event parameter optional
    selected_index = todo_listbox.curselection()
    if selected_index:
        todo_listbox.delete(selected_index)
        save_todo_list()

# Load data from JSON file if it exists
try:
    with open("todo_list.json", "r") as f:
        file_contents = f.read()
        todo_data = json.loads(file_contents) if file_contents else []
except FileNotFoundError:
    todo_data = []

# Create the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("800x400")  # Set your desired window size here

favicon_path = "todo.ico"  # Replace with the path to your favicon image
root.iconbitmap(favicon_path)
# Add vertical space using an empty label


# Load the header image
header_image = Image.open("todo.png")
header_image = header_image.resize((80, 80))  # Resize the image if needed
header_image = ImageTk.PhotoImage(header_image)
# Create widgets
header_label = tk.Label(root, text="To-Do List (Indra)",image=header_image, font=("Arial", 24, "bold"),bg="sky blue", width=370, compound=tk.LEFT, height=80)
todo_entry = tk.Entry(root, width=60)
todo_button = tk.Button(root, text="Add", command=add_todo, bg='blue', width=13, fg='white', font=("Arial",10,"bold"))
edit_button = tk.Button(root, text="Edit", command=edit_todo, bg='green', width=13, fg='white', font=("Arial",10,"bold"))
delete_button = tk.Button(root, text="Delete", command=delete_todo, bg='red', width=13, fg='white', font=("Arial",10,"bold"))
todo_listbox = tk.Listbox(root, width=70)

# Populate the listbox with the loaded data
for item in todo_data:
    todo_listbox.insert(tk.END, item)

# Grid layout
header_label.grid(row=0, column=1)

todo_entry.grid(row=1, column=1, padx=10, pady=20, columnspan=4)
todo_button.grid(row=1, column=5, padx=10, pady=10)
edit_button.grid(row=1, column=6, padx=10, pady=10)
delete_button.grid(row=1, column=7, padx=10, pady=10)
todo_listbox.grid(row=5, column=0, padx=10, pady=10, columnspan=6)


# Bind Enter and Delete keys to corresponding functions
root.bind("<Return>", lambda event: add_todo())
root.bind("<Delete>", delete_todo)

root.mainloop()
