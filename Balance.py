# for showing balance of the user
import tkinter

import pandas as pd

import transaction
import video_check


def balance():
    from pathlib import Path

    from tkinter import Canvas, Button, PhotoImage

    OUTPUT_PATH = Path (__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path ("./Balance")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path (path)

    window = tkinter.Toplevel ()

    window.geometry ("1100x800")
    window.configure (bg="#FFFFFF")

    canvas = Canvas (
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
        970.0,
        55.0,
        1057.0,
        97.0,
        fill="#FFFFFF",
        outline="")

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
                       command=lambda: (window.destroy (), transaction.transaction ()),
                       relief="flat"
                       )
    button_1.place (
        x=86.0,
        y=400.0,
        width=322.0,
        height=177.0
    )
    data = pd.read_csv ('bank_details.csv')
    text = data[data.loc[:, 'unique_id'] == video_check.real_user].loc[:, 'account_balance'].values[0]

    canvas.create_text (
        63.0,
        283.0,
        anchor="nw",
        text="Current Amount Balance: Rs" + str (text),
        fill="#000000",
        font=("Imprima Regular", 35 * -1)
    )
    window.resizable (False, False)
    window.mainloop ()
