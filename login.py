import tkinter
from tkinter import messagebox

import SwiftBankAuth
import write_csv

entry_1 = ''
entry_2 = ''
entry_3 = ''


def get_email():
    return entry_1.get ()


def get_pass():
    return entry_2.get ()


def get_mob():
    return entry_3.get ()


def login():
    global entry_2
    global entry_1
    global entry_3

    from pathlib import Path
    import dashboard
    from tkinter import Canvas, Entry, Button, PhotoImage

    OUTPUT_PATH = Path (__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path ("./login")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path (path)

    def get_v():
        email = entry_1.get ()
        password = entry_2.get ()
        mobile_number = entry_3.get ()
        print (email)
        print (password)
        print (mobile_number)

        if not email and not password:
            window.destroy ()
            messagebox._show ("Error", "You need a email to enroll an account and you need to input a password!")
            login ()
        elif not password:
            window.destroy ()
            messagebox._show ("Error", "You need to input a password!")
            login ()
        elif not email:
            window.destroy ()
            messagebox._show ("Error", "You need a email to enroll an account!")
            login ()
        elif len (password) < 8:
            window.destroy ()
            messagebox._show ("Password Error", "Your password needs to be at least 8 digits!")
            login ()
        elif '@' not in email or '.com' not in email:
            window.destroy ()
            messagebox._show ("Email Error", "please! enter correct email id")
            login ()
        elif len (mobile_number) != 10:
            window.destroy ()
            messagebox._show ("Mobile no error", "mobile no must be 10 digit")
        else:
            write_csv.write_csv ()
            window.destroy ()
            SwiftBankAuth.create_acc (email, password)

    window = tkinter.Toplevel ()

    window.geometry ("1050x800")
    window.configure (bg="#FFFFFF")

    canvas = Canvas (
        window,
        bg="#FFFFFF",
        height=800,
        width=1050,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place (x=0, y=0)
    canvas.create_rectangle (
        0.0,
        0.0,
        1050.0,
        800.0,
        fill="#162A94",
        outline="")

    canvas.create_rectangle (
        585.0,
        56.0,
        1119.0,
        930.0,
        fill="#29218F",
        outline="")

    entry_image_1 = PhotoImage (
        file=relative_to_assets ("entry_1.png"))
    entry_bg_1 = canvas.create_image (
        818.5,
        496.5,
        image=entry_image_1
    )
    entry_3 = Entry (window,
                     bd=0,
                     bg="#FFFFFF",
                     highlightthickness=0
                     )
    entry_3.place (
        x=672.5,
        y=473.0,
        width=292.0,
        height=45.0
    )

    canvas.create_text (
        698.0,
        426.0,
        anchor="nw",
        text="Mobile Number",
        fill="#FFB06D",
        font=("MontserratRoman Bold", 22 * -1)
    )

    canvas.create_text (
        699.0,
        280.0,
        anchor="nw",
        text="Password",
        fill="#FFB06D",
        font=("MontserratRoman Bold", 22 * -1)
    )

    button_image_1 = PhotoImage (
        file=relative_to_assets ("button_1.png"))
    button_1 = Button (window,
                       image=button_image_1,
                       borderwidth=0,
                       highlightthickness=0,
                       command=lambda: get_v (),
                       relief="flat"
                       )
    button_1.place (
        x=698.0,
        y=568.0,
        width=265.0,
        height=76.0
    )

    button_image_2 = PhotoImage (
        file=relative_to_assets ("button_2.png"))
    button_2 = Button (window,
                       image=button_image_2,
                       borderwidth=0,
                       highlightthickness=0,
                       command=lambda: (window.destroy (), dashboard.dashboard ()),
                       relief="flat"
                       )
    button_2.place (
        x=699.0,
        y=652.0,
        width=264.0,
        height=76.0
    )

    entry_image_2 = PhotoImage (
        file=relative_to_assets ("entry_2.png"))
    entry_bg_2 = canvas.create_image (
        818.5,
        210.5,
        image=entry_image_2
    )
    entry_1 = Entry (window,
                     bd=0,
                     bg="#FFFFFF",
                     highlightthickness=0
                     )
    entry_1.place (
        x=673.5,
        y=186.0,
        width=290.0,
        height=47.0
    )

    entry_image_3 = PhotoImage (
        file=relative_to_assets ("entry_3.png"))
    entry_bg_3 = canvas.create_image (
        818.5,
        350.5,
        image=entry_image_3
    )
    entry_2 = Entry (window,
                     bd=0,
                     bg="#FFFFFF",
                     highlightthickness=0,
                     show="*"
                     )
    entry_2.place (
        x=672.5,
        y=327.0,
        width=292.0,
        height=45.0
    )

    canvas.create_text (
        698.0,
        139.0,
        anchor="nw",
        text="Email",
        fill="#FFB06D",
        font=("MontserratRoman Bold", 22 * -1)
    )

    image_image_1 = PhotoImage (
        file=relative_to_assets ("image_1.png"))
    image_1 = canvas.create_image (
        307.0,
        409.0,
        image=image_image_1
    )
    window.resizable (False, False)
    window.mainloop ()
