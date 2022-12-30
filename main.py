import pygame
import random
import time
import tkinter as tk
from tkinter import font
import sympy

pygame.init()
pygame.mixer.music.load("XXXTENTACION - Moonlight (Super Slow 0,75x).mp3")
pygame.mixer.music.set_volume(0.15)


def calculate():
    # Get the user's input
    equation = input_field.get()

    # Check if the user wants to quit
    if equation == 'q':
        root.destroy()

    if 'E' in equation:
        user_input = ''.join(c for c in equation if c.isdigit() or c == '.')
        user_input = float(equation)
    equation = equation.replace('^', '**')
    equation = equation.replace('pi', str(sympy.pi))

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
    if result == 420:
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.stop()

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
    elif result == 528:
        comment_label['text'] = "Oh my god you got a secret number!"
        comment_label['text'] += "\n"
        comment_label['text'] += "\nI wonder why this number has significance though..."
    elif result == 36:
        comment_label['text'] = "I wonder how Aaron's car is doing."
    elif result == 420:
        comment_label['text'] = "ahhhhhh shiitttttttt"
    elif result == 8008 or result == 80085:
        comment_label['text'] = "heehee"
    elif result == 20:
        random_number = random.randint(1, 20)
        comment_label['text'] = f"You rolled a {random_number}!"
        if random_number == 1:
            time.sleep(1)
            comment_label['text'] += "\nOoh. Well. I think you died. "
            time.sleep(5)
            root.destroy()
        elif random_number == 20:
            comment_label['text'] += "\nNice! I guess you just win!"
        elif random_number < 10:
            comment_label['text'] += "\nYour shot bounces off the dragon, doing nothing!"
        elif random_number >= 10:
            comment_label['text'] += "\nYou do... some damage."
    elif result < 0:
        comment_label['text'] = "Let's TRY to be more positive, okay?"
    elif result == 0:
        comment_label['text'] = "Look! Its the amount of friends you have!"
    else:
        comments = ["You must be using a calculator or something...",
                    "You're a wizard Harry. \nA math wizard!",
                    "I'm proud of you, homes.",
                    "Nice work, ese.",
                    "Good stuff cuzzo.",
                    "You couldn't live with your own failure, \nand where did that bring you? \n\nBack to me.",
                    "Stream Back from You by Humdub on Spotify. \nNow.",
                    "I would be jealous of your math skills. \nIf I wasn't a calculator.",
                    "A system of cells. \nWithin cells interlinked. \nWithin one stem. \nAnd dreadfully distinct. \nAgainst the dark. \nA tall white fountain played.",
                    "I would be jealous of your math skills. \nIf I wasn't a calculator.",
                    "Just keep calculating. \nJust keep calculating. "]

        comment = random.choice(comments)
        comment_label['text'] = comment


# Create the window
root = tk.Tk()
root['bg'] = "#222"
root.title("Calculator")
root.geometry("450x700")
root.wm_title("The Snarky Calculator by Kushal P.")
root.wm_iconbitmap("simple-calculator.ico")

# Set the rows and columns to scale with the window size
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Create a frame to hold the widgets
frame = tk.Frame(root, bg='#222')
frame.grid(row=0, column=0)

# Create the label with the main text and add it to the frame
label = tk.Label(frame, text="The Snarky Calculator", font=("Helvetica", 30, "bold"), fg="#fff",bg='#222')
label.pack()

# Create a Text widget with the smaller text and add it to the frame
text = tk.Text(frame, font=("Helvetica", 16, "normal"), height=1, width=20, state=tk.NORMAL, bd=0)
text.insert(tk.END, "By Kushal P.")
text.configure(fg="#fff", bg="#222")
text.pack()

# Create the input field with a dark foreground color
input_field = tk.Entry(root, font=("Helvetica", 20), width=20, justify="center")
input_field.grid(row=2, column=0, columnspan=2, padx=20, pady=40, sticky="nsew")

# Create the calculate button with a smaller width
calculate_button = tk.Button(root, text="Calculate", font=("Helvetica", 24), width=20, command=calculate, fg="#fff",
                             bg='#222')
calculate_button.grid(row=3, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")

# Create the result label with a dark foreground color
result_label = tk.Label(root, font=("Helvetica", 16), width=50, fg="#fff", bg='#222', wraplength=350)
result_label.grid(row=4, column=0, columnspan=2, padx=20, pady=10, sticky="n")

# Create the comment label with a dark foreground color
comment_label = tk.Label(root, font=("Helvetica", 14), width=50, fg="#fff", bg='#222', wraplength=350)
comment_label.grid(row=5, column=0, columnspan=2, padx=20, pady=60, sticky="n")

# Start the window loop
root.mainloop()
