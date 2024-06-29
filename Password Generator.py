import string
#1import art
from Color_Console import ctext
from tkinter import filedialog
import random
from tkinter import filedialog
import time

l1 = list(string.ascii_lowercase)
l2 = list(string.ascii_uppercase)
l3 = list(string.digits)
l4 = list(string.punctuation)

random.shuffle(l1)
random.shuffle(l2)
random.shuffle(l3)
random.shuffle(l4)

ctext("=" * 90, "yellow", "black")
ctext("This script app was made by developer Abdallah Medhat.\nSoftware Engineer", "cyan", "black")
ctext("=" * 90, "yellow", "black")

while True:
    try:
        user = int(input("How many characters for the Password?...Note: It must be 8 characters or more\nPlease type here: "))
        if user < 8:
            ctext("\nInvalid Input", "red", "black")
            ctext("Your input are lower than 8.\n", "red", "white")
        else:
            break
    except ValueError:
        ctext("\nInvalid Input", "red", "black")
        ctext("It must be an integer characters\n", "red", "white")

while True:
    web = input("Type the Website you want to create a password for:\n")
    try:
        web = int(web)
        ctext("\nInvalid Input", "red", "black")
    except ValueError:
        break

while True:
    user_name = input("Type your user name:\n")
    try:
        user_name = int(user_name)
        ctext("\nInvalid Input", "red", "black")
    except ValueError:
        break

part1 = round(user*(30/100))
part2 = round(user*(20/100))

password = []

for x in range(part1):
    password.append(l1[x])
    password.append(l2[x])

for x in range(part2):
    password.append(l3[x])
    password.append(l4[x])

random.shuffle(password)
st = "".join(password)
ctext("Here is your password:", "cyan", "black")
ctext(f"{st}", "green", "black")
print()

ctext("Note: Save your file in this format:", "cyan", "black")
ctext("EX: File Name.txt", "green", "black")


list_lines = [f"Website Names: {web}\n", f"User Name: {user_name}\n", f"Password: {st}\n"]
folder = filedialog.asksaveasfilename()

file = open(folder,"a+")
file.writelines(list_lines)
file.write("==================================================\n")
file.close()

ctext("=" * 90, "yellow", "black")
ctext("This script app was made by developer Abdallah Medhat.\nSoftware Engineer", "cyan", "black")
ctext("Follow me on Facebook: https://bit.ly/3S6z8yt", "cyan", "black")
ctext("mail me on: abdallahmedhat333@gmail.com", "cyan", "black")
ctext("© Copyright 2024 Abdallah Medhat. All rights reserved", "green", "black")
ctext("=" * 90, "yellow", "black")
time.sleep(7)