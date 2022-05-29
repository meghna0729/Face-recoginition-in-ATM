import tkinter
from pathlib import Path
from tkinter import Button, PhotoImage

import Balance
import Deposit
import front
import transfer
import withdraw


def transaction():
    OUTPUT_PATH = Path (__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path ("./transaction")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path (path)

    window = tkinter.Toplevel ()

    window.geometry ("1100x800")
    window.configure (bg="#FFFFFF")

    canvas = tkinter.Canvas (
        window,
        bg="#FFFFFF",
        height=800,
        width=1100,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place (x=0, y=0)
    image_image_1 = PhotoImage (
        file=relative_to_assets ("image_1.png"))
    image_1 = canvas.create_image (
        692.0,
        400.0,
        image=image_image_1
    )

    canvas.create_rectangle (
        0.0,
        0.0,
        494.0,
        800.0,
        fill="#FFFFFF",
        outline="")

    button_image_1 = PhotoImage (
        file=relative_to_assets ("button_1.png"))
    button_1 = Button (window,
                       image=button_image_1,
                       borderwidth=0,
                       highlightthickness=0,
                       command=lambda: (window.destroy (), front.front ()),
                       relief="flat"
                       )
    button_1.place (
        x=53.0,
        y=654.0,
        width=322.0,
        height=98.0
    )

    button_image_2 = PhotoImage (
        file=relative_to_assets ("button_2.png"))
    button_2 = Button (window,
                       image=button_image_2,
                       borderwidth=0,
                       highlightthickness=0,
                       command=lambda: (window.destroy (), Deposit.deposit ()),
                       relief="flat"
                       )
    button_2.place (
        x=51.0,
        y=509.0,
        width=322.0,
        height=98.0
    )

    button_image_3 = PhotoImage (
        file=relative_to_assets ("button_3.png"))
    button_3 = Button (window,
                       image=button_image_3,
                       borderwidth=0,
                       highlightthickness=0,
                       command=lambda: (window.destroy (), Balance.balance ()),
                       relief="flat"
                       )
    button_3.place (
        x=53.0,
        y=364.0,
        width=322.0,
        height=98.0
    )

    button_image_4 = PhotoImage (
        file=relative_to_assets ("button_4.png"))
    button_4 = Button (window,
                       image=button_image_4,
                       borderwidth=0,
                       highlightthickness=0,
                       command=lambda: (window.destroy (), withdraw.with_draw ()),
                       relief="flat"
                       )
    button_4.place (
        x=39.0,
        y=219.0,
        width=336.0,
        height=98.0
    )

    button_image_5 = PhotoImage (
        file=relative_to_assets ("button_5.png"))
    button_5 = Button (window,
                       image=button_image_5,
                       borderwidth=0,
                       highlightthickness=0,
                       command=lambda: (window.destroy (), transfer.transfer ()),
                       relief="flat"
                       )
    button_5.place (
        x=53.0,
        y=74.0,
        width=322.0,
        height=98.0
    )

    canvas.create_rectangle (
        970.0,
        55.0,
        1057.0,
        97.0,
        fill="#FFFFFF",
        outline="")
    window.resizable (False, False)
    window.mainloop ()
