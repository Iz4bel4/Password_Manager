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
        is_okay = messagebox.askokcancel(title=website_entry.get(),
                                         message=f'These are the details entered: \nEmail: {email} \nPassword:{password}\nIs it okay to save?')
        if is_okay:
            with open('data.json', 'r') as datafile:
                #reading old data
                data = json.load(datafile)
                #updating new data
                data.update(new_data)

            with open('data.json', 'w') as datafile:
                #saving new data
                json.dump(new_data, datafile, indent=4)

                website_entry.delete(0, END)
                pass_entry.delete(0, END)



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
website_entry = Entry(width=50)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=50)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, 'email@email.com')
pass_entry = Entry(width=32)
pass_entry.grid(row=3, column=1)

# Button
generate_pass_button = Button(text='Generate Password', width=14, command=generate_password)
generate_pass_button.grid(row=3, column=2)
add_button = Button(text='Add', width=43, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
