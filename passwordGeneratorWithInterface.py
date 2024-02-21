'''
    Password Generator using the TKinter library. 
    
    The program asks for password length and the amount of passwords the user desires. The said passwords
    are outputted to a textbox, as textboxes allow for copying. Inately, the program generates passwords with 
    digits, characters and signs.

'''

import random
import string
from tkinter import *
from tkinter import ttk
from tkinter import Text

GUI = Tk()
GUI.geometry("500x500") # Sets window size. #
GUI.title("Password Generator") # Sets window title. #

# Concatenates all letters, digits and punctuation characters of ASCII. # 
passwordAlphabet = string.ascii_letters + string.digits + string.punctuation

def generatePassword():
    # Creates the textbox for passwords. #
    passwordShow = Text(name = "isPassword", width = 60, height = 22)
    passwordShow.grid(row = 4, columnspan = 2)

    # Asks for password length and the number of passwords. #
    currentGeneratedPasswords = 0
    passwordLength = int(passwordLengthEntry.get())
    passwordNumber = int(passwordNumberEntry.get())

    # Deletes all previous passwords. #
    passwordShow.delete('1.0', END)

    while currentGeneratedPasswords < passwordNumber: # Will loop until all N number of passwords have been created. # 
        currentPasswordLength = 0
        password = ""
        while currentPasswordLength < passwordLength: # Will loop until the desired length of the password is reached. #
            password += random.choice(passwordAlphabet) 
            currentPasswordLength += 1

        # The Text widget gets the outputted passwords. #
        passwordShow.insert(END, password + "\n")
        currentGeneratedPasswords += 1

# Creates input points for the password length. #
passwordLengthLabel = ttk.Label(text = "Enter password length: ").grid(row = 0, column = 0, padx = 20)
passwordLengthEntry = ttk.Entry(GUI) # Entry widget allows for input. #
passwordLengthEntry.grid(row = 0, column = 1, padx =10)

# Creates input points for the number of passwords. #
passwordNumberLabel = ttk.Label(text = "Enter number of passwords: ").grid(row = 1, column = 0, padx = 20)
passwordNumberEntry = ttk.Entry(GUI)
passwordNumberEntry.grid(row = 1, column = 1, padx = 10)

# Creates the password generation button. #
generationButton = ttk.Button(GUI, text="Generate Password", command=generatePassword)
generationButton.grid(row = 3, columnspan = 1, pady = 5) 

# Event handler of the window. #
GUI.mainloop()