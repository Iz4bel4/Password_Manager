from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    web = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

    if len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message="Please don't leave any fields empty!")
    else:
        is_okay = messagebox.askokcancel(title=website_entry.get(),
                                         message=f'These are the details entered: \nEmail: {email} \nPassword:{password}\nIs it okay to save?')
        if is_okay:
            with open('data.txt', 'a') as datafile:
                datafile.write(f' {web} / {email} / {password} \n')
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
generate_pass_button = Button(text='Generate Password', width=14)
generate_pass_button.grid(row=3, column=2)
add_button = Button(text='Add', width=43, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
