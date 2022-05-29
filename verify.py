import tkinter
from pathlib import Path
from tkinter import Canvas, Button, PhotoImage

import pandas as pd

import dashboard
import video_check


def verify():
    OUTPUT_PATH = Path (__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path ("./verify")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path (path)

    window = tkinter.Toplevel ()
    window.geometry ("1100x700")
    window.configure (bg="#FFFFFF")

    canvas = Canvas (
        window,
        bg="#FFFFFF",
        height=700,
        width=1100,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place (x=0, y=0)
    image_image_1 = PhotoImage (
        file=relative_to_assets ("image_1.png"))
    image_1 = canvas.create_image (
        550.0,
        350.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage (
        file=relative_to_assets ("button_1.png"))
    button_1 = Button (window,
                       image=button_image_1,
                       borderwidth=0,
                       highlightthickness=0,
                       command=lambda: (window.destroy ()),
                       relief="flat"
                       )
    button_1.place (
        x=322.0,
        y=492.0,
        width=212.0,
        height=64.0
    )

    button_image_2 = PhotoImage (
        file=relative_to_assets ("button_2.png"))
    button_2 = Button (window,
                       image=button_image_2,
                       borderwidth=0,
                       highlightthickness=0,
                       command=lambda: (window.destroy (), video_check.video_check ()),
                       relief="flat"
                       )
    button_2.place (
        x=110.0,
        y=372.0,
        width=361.0,
        height=64.0
    )

    button_image_3 = PhotoImage (
        file=relative_to_assets ("button_3.png"))
    button_3 = Button (window,
                       image=button_image_3,
                       borderwidth=0,
                       highlightthickness=0,
                       command=lambda: (window.destroy (), dashboard.dashboard ()),
                       relief="flat"
                       )
    button_3.place (
        x=54.0,
        y=492.0,
        width=212.0,
        height=64.0
    )

    button_image_4 = PhotoImage (
        file=relative_to_assets ("button_4.png"))
    button_4 = Button (window,
                       image=button_image_4,
                       borderwidth=0,
                       highlightthickness=0,
                       command=lambda: print ("button_4 clicked"),
                       relief="flat"
                       )
    button_4.place (
        x=17.0,
        y=33.0,
        width=679.0,
        height=339.0
    )
    data = pd.read_csv ('bank_details.csv')
    window.resizable (False, False)
    window.mainloop ()
