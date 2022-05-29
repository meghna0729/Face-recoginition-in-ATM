import tkinter
from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage

import dashboard


def front():
    OUTPUT_PATH = Path (__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path ("./front")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path (path)

    root = Tk ()
    root.withdraw ()
    window = tkinter.Toplevel ()
    window.title ("demo")

    window.geometry ("1101x800")
    window.configure (bg="#FFFFFF")

    canvas = Canvas (
        window,
        bg="#FFFFFF",
        height=800,
        width=1101,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place (x=0, y=0)
    image_image_1 = PhotoImage (
        file=relative_to_assets ("image_1.png"))
    image_1 = canvas.create_image (
        295.0,
        400.0,
        image=image_image_1
    )

    canvas.create_rectangle (
        591.0,
        0.0,
        1101.0,
        800.0,
        fill="#E29FB7",
        outline="")

    button_image_1 = PhotoImage (
        file=relative_to_assets ("button_1.png"))

    button_1 = Button (window,
                       image=button_image_1,
                       borderwidth=0,
                       highlightthickness=0,
                       command=lambda: (window.destroy (), dashboard.dashboard ()),
                       relief="flat"
                       )

    button_1.place (
        x=664.0,
        y=274.0,
        width=379.0,
        height=89.0
    )

    button_image_2 = PhotoImage (
        file=relative_to_assets ("button_2.png"), master=window)
    button_2 = Button (window,
                       image=button_image_2,
                       borderwidth=0,
                       highlightthickness=0,
                       command=lambda: (window.destroy (), root.destroy ()),
                       relief="flat"
                       )

    button_2.place (
        x=663.0,
        y=416.0,
        width=380.0,
        height=94.0
    )

    canvas.create_text (
        641.0,
        49.0,
        anchor="nw",
        text="SWIFT BANK",
        fill="#000000",
        font=("JacquesFrancoisShadow", 48 * -1)
    )

    canvas.create_rectangle (
        641.0,
        114.0,
        1073.0,
        117.0,
        fill="#000000",
        outline="")

    window.resizable (False, False)
    window.mainloop ()
