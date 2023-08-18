import tkinter as tk
import random
import string
from tkinter import END


def new_rand(my_password=None):
    #Clear OUr Entry Box
    result_entry.delete(0,END)

    username = username_entry.get()
    length = int(length_entry.get())
    #generate_password(username, length)

    #createa variable to hold our password
    my_password = ''
    #Loop through password length
    for x in range(length):
        my_password += chr(random.randint(33, 126))

    #Output  password to the screen
    result_entry.insert(0, my_password)

def on_reset():
    username_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    result_entry.delete(0,tk.END)

def on_accept():
    generated_password = result_label.cget("text").replace("Generated Password: ", "")
    # Do something with the generated_password, e.g., store it securely or use it in your application.
    print("Accepted password:", generated_password)

# Create the main application window
app = tk.Tk()
app.geometry("680x400")
app.title("Password Generator")

tk.Label(app, text ='Password Generator',fg="blue", font = ('Helvetica 18 underline')).grid(row=1,column=1)


# Username entry
username_label = tk.Label(app, text="Username:",anchor="center",font=("Helvetica", 18), bd=12, bg="systembuttonface")
username_label.grid(row=5, column=0)
username_entry = tk.Entry(app, text='',font=("Helvetica", 24), bd=2, bg="systembuttonface")
username_entry.grid(row=5, column=1)

# Password length entry
length_label = tk.Label(app, text="Password Length:",anchor="center",font=("Helvetica", 18), bd=12, bg="systembuttonface")
length_label.grid(row=6,column=0)
length_entry = tk.Entry(app, text='',font=("Helvetica", 24), bd=2, bg="systembuttonface")
length_entry.grid(row=6,column=1)

# Display generated password
result_label = tk.Label(app, text="Generated Password: ",anchor="center",font=("Helvetica", 18), bd=17, bg="systembuttonface")
result_label.grid()
result_entry=tk.Entry(app, text='', font=("Helvetica", 24), bd=2, bg="systembuttonface")
result_entry.grid(row=7,column=1)

# Generate password button
generate_button = tk.Button(app, text="Generate Password",font=("Helvetica", 18), bd=4, bg="blue",fg="white", command=new_rand)
generate_button.grid(row=8 , column=1)

# Reset button
reset_button = tk.Button(app, text="Reset",font=("Helvetica", 18), bd=4, bg="systembuttonface",fg="blue", command=on_reset)
reset_button.grid(row=9 , column=1)

# Accept button
accept_button = tk.Button(app, text="Accept",font=("Helvetica", 18), bd=4, bg="systembuttonface",fg="blue", command=on_accept)
accept_button.grid(row=10 , column=1)


# Start the main event loop
app.mainloop()
