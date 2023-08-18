from tkinter import *
import math
import re

root = Tk()
root.title("Simple Calculator")
root.geometry("570x600+100+200")
root.resizable(False, False)
root.configure(bg="#17161b")
equation = ""


def show(value):
    global equation
    equation += value
    label_result.config(text=equation)


def clear():
    global equation
    equation = ""
    label_result.config(text=equation)


def calculate_sqrt(number):
    return math.sqrt(number)


def get_square_root_value(root_digit):
    match = re.search(r'√(\d+(\.\d+)?)', root_digit)
    if match:
        return match.group(1)
    return ""


def rplace(val1, val2):
    # Find the part under the square root using regular expression
    match = re.search(r'√\w+', val1)

    if match:
        # Extract the matched part (e.g., "√anynumber")
        matched_part = match.group()

        # Replace the matched part with a new value
        new_value = val2  # Replace this with the value you want
        new_equation = equation.replace(matched_part, new_value)

        return new_equation
    else:
        print("No match found in the equation.")


def Calculate():
    global equation
    result = ""
    try:
        match = get_square_root_value(equation)
        match = int(match)
        print(match)
        equation = rplace(equation, f" + calculate_sqrt({match})")
        if equation != "":
            # try:
            result = eval(equation)
            # except Exception as e:
            # result = "error"
            # print(f"An error occurred: {e}")
            equation = str(result)
    except:

        if equation != "":
            # try:
            result = eval(equation)
            # except Exception as e:
            #result = "error"
            # print(f"An error occurred: {e}")
            equation = str(result)
    label_result.config(text=result)


label_result = Label(root, width=25, height=2, text="", font=("arial", 30))
label_result.pack()

Button(root, text="C", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5",command=lambda: clear()).place(x=10, y=100)
Button(root, text="√", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2b36",command=lambda: show("√")).place(x=150, y=100)
Button(root, text="/", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2b36",command=lambda: show("/")).place(x=290, y=100)
Button(root, text="<", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2b36",command=lambda: show("<")).place(x=430, y=100)

Button(root, text="7", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2b36",command=lambda: show("7")).place(x=10, y=200)
Button(root, text="8", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2b36",command=lambda: show("8")).place(x=150, y=200)
Button(root, text="9", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2b36",command=lambda: show("9")).place(x=290, y=200)
Button(root, text="*", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2b36",command=lambda: show("*")).place(x=430, y=200)

Button(root, text="4", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2b36",command=lambda: show("4")).place(x=10, y=300)
Button(root, text="5", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2b36",command=lambda: show("5")).place(x=150, y=300)
Button(root, text="6", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2b36",command=lambda: show("6")).place(x=290, y=300)
Button(root, text="-", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2b36",command=lambda: show("-")).place(x=430, y=300)

Button(root, text="1", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2b36",command=lambda: show("1")).place(x=10, y=400)
Button(root, text="2", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2b36",command=lambda: show("2")).place(x=150, y=400)
Button(root, text="3", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2b36",command=lambda: show("3")).place(x=290, y=400)
Button(root, text="+", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2b36",command=lambda: show("+")).place(x=430, y=400)

Button(root, text="!", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2b36",command=lambda: show("!")).place(x=10, y=500)
Button(root, text="0", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2b36",command=lambda: show("0")).place(x=150, y=500)
Button(root, text=".", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2b36",command=lambda: show(".")).place(x=290, y=500)
Button(root, text="=", width=6, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#fe9037",command=lambda: Calculate()).place(x=430, y=500)

root.mainloop()