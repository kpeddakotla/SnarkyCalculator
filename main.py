import random
import time
import tkinter as tk
import webbrowser


def open_link(event):
    # Open the URL in the default web browser
    webbrowser.open("https://admissions.pitt.edu/")


def calculate():
    # Get the user's input
    equation = input_field.get()

    # Check if the user wants to quit
    if equation == 'q':
        root.destroy()

    # Reset the labels
    result_label['text'] = ""
    comment_label['text'] = ""

    # Try to evaluate the equation
    try:
        result = eval(equation)
        result_label['text'] = f"The result is {result}."
    except SyntaxError:
        result_label['text'] = "Invalid syntax. Please try again."
        comment_label['text'] = "Maybe you should try reading a math book or two."
    except NameError:
        if equation == 'Kavin':
            comment_label['text'] = "\nThis: https://admissions.pitt.edu/"
            comment_label['text'] += "\nAnd the new instagram post."
            comment_label['text'] += "\nEnough said."
        else:
            result_label['text'] = "Unknown variable. Please check your spelling and try again."
            comment_label['text'] = "I hope you didn't misspell your variable on purpose."
    except ZeroDivisionError:
        result_label['text'] = "You can't divide by zero. Please try again."
        comment_label['text'] = "I'm pretty sure you learned this in elementary school."
    except:
        result_label['text'] = "Sorry, something went wrong. Please try again."
        comment_label['text'] = "I'm not sure what you did, but it was definitely wrong."

    # Choose a comment based on the result
    if result == 917:
        comment_label['text'] = "You get the feeling this might be someone's favorite number..."
        comment_label['text'] += "\n"
        comment_label['text'] += "\n(P.S. You should wish Baasil a Happy Birthday)"
    elif result == 9:
        comment_label['text'] = "NOBODY SHOW AARON"
        comment_label['text'] += "\nI REPEAT..."
        comment_label['text'] += "\nNOBODY"
        comment_label['text'] += "\nSHOW"
        comment_label['text'] += "\nAARON!!!!"
    elif result == 36:
        comment_label['text'] = "I wonder how Aaron's car is doing."
    elif result == 8008:
        comment_label['text'] = "heehee"
    elif result == 20:
        random_number = random.randint(1, 20)
        comment_label['text'] = f"You rolled a {random_number}!"
        if random_number == 1:
            comment_label['text'] += "\nOooh. Well. I think you died. "
            time.sleep(5)
            root.destroy()
        elif random_number == 20:
            comment_label['text'] += "\nNice! I guess you just win!"
        elif random_number < 10:
            comment_label['text'] += "\nYour shot bounces off the dragon, doing nothing!"
        elif random_number >= 10:
            comment_label['text'] += "\nYou do... some damage."
    elif result < 0:
        comment_label['text'] = "Let's try to be more positive, okay?"
    elif result == 0:
        comment_label['text'] = "Well, at least you didn't mess up."
    else:
        comment_label['text'] += "\nLooks like you know your stuff!"
        comment_label['text'] += "\nKeep up the good work!"


# Create the window
root = tk.Tk()
root.title("Calculator")
root.geometry("1000x720")

# Create the input field
input_field = tk.Entry(root, font=("Arial", 24), width=50)
input_field.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

# Create the calculate button
calculate_button = tk.Button(root, text="Calculate", font=("Arial", 24), command=calculate)
calculate_button.grid(row=1, column=0, padx=20, pady=20)
calculate_button.grid(row=1, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")

# Create the result label
result_label = tk.Label(root, font=("Arial", 24), width=50)
result_label.grid(row=2, column=0, columnspan=2, padx=20, pady=60)
result_label.grid(row=2, column=0, columnspan=2, padx=20, pady=60, sticky="nsew")

# Create the comment label
comment_label = tk.Label(root, font=("Arial", 24), width=50)
comment_label.grid(row=3, column=0, columnspan=2, padx=20, pady=120)

# Start the window loop
root.mainloop()
