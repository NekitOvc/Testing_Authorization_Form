from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, askokcancel

import logging

logging.basicConfig(level=logging.INFO, filename='py_log.log', filemode='w', format='%(asctime)s %(levelname)s %(message)s')

app = Tk(logging.info(f"Application is running"))
app.title("Authorization")
app.geometry("300x250")
app.resizable(False, False)


def click_button_enter():
    login = input_text_login.get()
    logging.info(f"The user has specified a username '{login}'")
    showinfo(title="Notification", message="Authorization was successful")
    logging.info("The user entered the data")
    app.destroy()

def close_app():
    confirmation_window = askokcancel(title="Warning", message="Get out?")
    if confirmation_window:
        logging.info("The user closed the application")
        app.destroy()

text_login = ttk.Label(text="Login")
text_login.pack(anchor=N, padx=20, pady=10)
input_text_login = ttk.Entry()
input_text_login.pack(anchor=N, padx=20)

text_password = ttk.Label(text="Password")
text_password.pack(anchor=N, padx=20, pady=10)
input_text_password = ttk.Entry()
input_text_password.pack(anchor=N, padx=20)

button_enter = ttk.Button(text="Enter", command=click_button_enter)
button_enter.pack(expand=True, anchor=S, pady=30)

app.protocol("WM_DELETE_WINDOW", close_app)
app.mainloop()