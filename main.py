import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(8, 10)]
    password_symbols = [random.choice(symbols) for _ in range(2, 4)]
    password_numbers = [random.choice(numbers) for _ in range(2, 4)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    website = website_entry.get()
    user = user_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "user": user,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Make sure you haven't left any fields empty.")
    else:
        with open("data.json", "a") as data_file:
            json.dump(new_data, data_file, indent=4)
        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=20, padx=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=0, columnspan=3)

website_label = Label(text="WEBSITE: ")
website_label.grid(row=1, column=0)
website_entry = Entry(width=20)
website_entry.grid(row=1, column=1)
website_entry.focus()

user_label = Label(text="EMAIL/USERNAME:")
user_label.grid(row=2, column=0)
user_entry = Entry(width=40)
user_entry.grid(row=2, column=1, columnspan=2)
user_entry.insert(0, "briantapia1155@gmail.com")

password_label = Label(text="PASSWORD:")
password_label.grid(row=3, column=0)
password_entry = Entry(width=20)
password_entry.grid(row=3, column=1)

generate_button = Button(text="GENERATE PASSWORD", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="ADD", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
