
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
from unittest import result
from logic import *
from succes import *


# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1280x720")
window.configure(bg = "#B9EBF6")

global keterangan
keterangan = ""
def cek () :
    print (username.get())
    print (password.get())
    result = login(username.get(), password.get())
    if result == 1 :
        print ("login berhasil")
        window_succes(window)
    else :
        keterangan = result
        print(keterangan)
        canvas.itemconfig(flag_error, text=keterangan)
        
        # massag_flag(keterangan)



canvas = Canvas(
    window,
    bg = "#B9EBF6",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    566.0,
    125.0,
    anchor="nw",
    text="Sign in ",
    fill="#000000",
    font=("Poppins Bold", 50 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    652.5,
    296.0,
    image=entry_image_1
)
username = Entry(
    bd=0,
    bg="#F9F9F9",
    highlightthickness=0
)
username.place(
    x=491.0,
    y=265.5,
    width=323.0,
    height=59.0
)

canvas.create_text(
    490.0,
    234.0,
    anchor="nw",
    text="Username :",
    fill="#000000",
    font=("Poppins Regular", 20 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    652.5,
    422.0,
    image=entry_image_2
)
password = Entry(
    bd=0,
    bg="#F9F9F9",
    highlightthickness=0
)
password.place(
    x=491.0,
    y=391.5,
    width=323.0,
    height=59.0
)

canvas.create_text(
    490.0,
    360.0,
    anchor="nw",
    text="Pasword",
    fill="#000000",
    font=("Poppins Regular", 20 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: cek(),
    relief="flat"
)
button.place(
    x=539.0,
    y=498.0,
    width=228.0,
    height=82.0
)

flag_error = canvas.create_text(
    1280/2,
    632.0,
    anchor="center",
    text= keterangan,
    fill="#e35b2d",
    font=("Poppins Regular", 20 * -1)
)
window.resizable(False, False)
window.mainloop()
