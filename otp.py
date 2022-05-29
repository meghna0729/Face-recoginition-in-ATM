import tkinter
from tkinter import Canvas, Entry, Button, PhotoImage
from tkinter import messagebox

import password


def otp():
    from pathlib import Path
    import transaction
    import front
    global number

    OUTPUT_PATH = Path (__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path ("./password")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path (path)

    # checking otp sent on  the registered number matching with written otp or not
    def verify_user():

        gottenotp = password.otp_no

        if str (entry_1.get ()) == str (gottenotp):
            window.destroy ()
            messagebox._show ("Verification Info!", "Verification Successful!")
            transaction.transaction ()
        else:
            window.destroy ()
            messagebox._show ("Verification Info!", "Verification Failed")
            front.front ()

    window = tkinter.Toplevel ()

    window.geometry ("1000x700")
    window.configure (bg="#FFFFFF")

    canvas = Canvas (
        window,
        bg="#FFFFFF",
        height=700,
        width=1000,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place (x=0, y=0)
    image_image_1 = PhotoImage (
        file=relative_to_assets ("image_1.png"))
    image_1 = canvas.create_image (
        500.0,
        350.0,
        image=image_image_1
    )

    canvas.create_text (
        35.0,
        223.0,
        anchor="nw",
        text="Plzz.. Enter OTP sent on your registered mobile no",
        fill="#E5F80F",
        font=("Inter Bold", 28 * -1)
    )

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
        x=215.0,
        y=391.0,
        width=212.0,
        height=64.0
    )

    button_image_2 = PhotoImage (
        file=relative_to_assets ("button_2.png"))
    button_2 = Button (window,
                       image=button_image_2,
                       borderwidth=0,
                       highlightthickness=0,
                       command=lambda: verify_user (),
                       relief="flat"
                       )
    button_2.place (
        x=19.0,
        y=391.0,
        width=212.0,
        height=64.0
    )

    entry_image_1 = PhotoImage (
        file=relative_to_assets ("entry_1.png"))
    entry_bg_1 = canvas.create_image (
        212.5,
        306.5,
        image=entry_image_1
    )
    entry_1 = Entry (window,
                     bd=0,
                     bg="#FFFFFF",
                     highlightthickness=0,
                     show="*"
                     )
    entry_1.place (
        x=74.0,
        y=285.0,
        width=277.0,
        height=41.0
    )
    window.resizable (False, False)
    window.mainloop ()
