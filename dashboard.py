import tkinter
from pathlib import Path
from tkinter import Canvas, Button, PhotoImage

import front
import login
import verify


def dashboard():
    OUTPUT_PATH = Path (__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path ("./dashboard")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path (path)

    window = tkinter.Toplevel ()

    window.geometry ("1100x800")
    window.configure (bg="#E29FB8")

    canvas = Canvas (
        window,
        bg="#E29FB8",
        height=800,
        width=1100,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place (x=0, y=0)
    canvas.create_rectangle (
        0.0,
        0.0,
        1100.0,
        800.0,
        fill="#C4C4C4",
        outline="")

    image_image_1 = PhotoImage (
        file=relative_to_assets ("image_1.png"))
    image_1 = canvas.create_image (
        550.0,
        400.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage (
        file=relative_to_assets ("button_1.png"))
    button_1 = Button (window,
                       image=button_image_1,
                       borderwidth=0,
                       highlightthickness=0,
                       command=lambda: (window.destroy (), login.login ()),
                       relief="flat"
                       )
    button_1.place (
        x=567.0,
        y=101.0,
        width=404.0,
        height=152.0
    )

    button_image_2 = PhotoImage (
        file=relative_to_assets ("button_2.png"))
    button_2 = Button (window,
                       image=button_image_2,
                       borderwidth=0,
                       highlightthickness=0,
                       command=lambda: (window.destroy (), verify.verify ()),
                       relief="flat"
                       )
    button_2.place (
        x=567.0,
        y=354.0,
        width=404.0,
        height=152.0
    )

    button_image_3 = PhotoImage (
        file=relative_to_assets ("button_3.png"))
    button_3 = Button (window,
                       image=button_image_3,
                       borderwidth=0,
                       highlightthickness=0,
                       command=lambda: (window.destroy (), front.front ()),
                       relief="flat"
                       )
    button_3.place (
        x=571.0,
        y=598.0,
        width=404.0,
        height=152.0
    )
    window.resizable (False, False)
    window.mainloop ()
