from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    letters_list = [random.choice(letters) for char in range(nr_letters)]

    symbols_list = [random.choice(symbols) for char in range(nr_symbols)]

    numb_list = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = letters_list + symbols_list + numb_list
    random.shuffle(password_list)

    password = ''.join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    web = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {
        web: {
        'email': email,
        'password': password
        }
    }

    if len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message="Please don't leave any fields empty!")
    else:
        try:
            with open('data.json', 'r') as datafile:
                data = json.load(datafile)
        except FileNotFoundError:
            with open('data.json', 'w') as datafile:
                # saving new data
                json.dump(new_data, datafile, indent=4)
        else:
            #updating new data
            data.update(new_data)
            with open('data.json', 'w') as datafile:
                # saving new data
                json.dump(new_data, datafile, indent=4)
        finally:
            website_entry.delete(0, END)
            pass_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    web = website_entry.get()
    try:
        with open('data.json', 'r') as datafile:
            data = json.load(datafile)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='No Data File Found')
    else:
        if web in data:
            messagebox.showinfo(title=f'{web}',
                                message=f'Email: {data[web]["email"]}\nPassword: {data[web]["password"]}')
        else:
            messagebox.showinfo(title='Error', message='No details for the website exists')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text='Website:')
website_label.grid(row=1, column=0)
email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)
pass_label = Label(text='Password:')
pass_label.grid(row=3, column=0)

# Entry
website_entry = Entry(width=32)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=50)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, 'email@email.com')
pass_entry = Entry(width=32)
pass_entry.grid(row=3, column=1)

# Button
search_button = Button(text='Search', width=14, command=find_password)
search_button.grid(row=1, column=2)
generate_pass_button = Button(text='Generate Password', width=14, command=generate_password)
generate_pass_button.grid(row=3, column=2)
add_button = Button(text='Add', width=43, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
