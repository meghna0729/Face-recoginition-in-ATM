import tkinter
from tkinter import messagebox

import pandas as pd

import transaction
import video_check


def deposit():
    from pathlib import Path

    from tkinter import Canvas, Entry, Button, PhotoImage

    OUTPUT_PATH = Path (__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path ("./Deposit")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path (path)

    def user_deposit_trans():
        data = pd.read_csv ('bank_details.csv')
        update_data = data.set_index ('unique_id')
        update_data.loc[video_check.real_user, 'account_balance'] += int (entry_1.get ())
        update_data.reset_index (inplace=True)
        update_data.columns = ['unique_id', 'account_number', 'email', 'bank', 'password', 'acc_balance', 'mobile_no']
        update_data.to_csv ('bank_details.csv', index=None)
        messagebox._show ("Deposit Info!", "Successfully Deposited!")
        window.destroy ()
        transaction.transaction ()

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

    entry_image_1 = PhotoImage (
        file=relative_to_assets ("entry_1.png"))
    entry_bg_1 = canvas.create_image (
        240.5,
        344.0,
        image=entry_image_1
    )
    entry_1 = Entry (window,
                     bd=0,
                     bg="#F1B191",
                     highlightthickness=0
                     )
    entry_1.place (
        x=125.0,
        y=322.0,
        width=231.0,
        height=42.0
    )

    canvas.create_text (
        54.0,
        243.0,
        anchor="nw",
        text="Enter Amount To Deposit",
        fill="#000000",
        font=("Imprima Regular", 35 * -1)
    )

    button_image_2 = PhotoImage (
        file=relative_to_assets ("button_2.png"))
    button_2 = Button (window,
                       image=button_image_2,
                       borderwidth=0,
                       highlightthickness=0,
                       command=lambda: (window.destroy (), transaction.transaction ()),
                       relief="flat"
                       )
    button_2.place (
        x=79.0,
        y=563.0,
        width=322.0,
        height=177.0
    )

    button_image_3 = PhotoImage (
        file=relative_to_assets ("button_3.png"))
    button_3 = Button (window,
                       image=button_image_3,
                       borderwidth=0,
                       highlightthickness=0,
                       command=lambda: user_deposit_trans (),
                       relief="flat"
                       )
    button_3.place (
        x=79.0,
        y=437.0,
        width=336.0,
        height=142.0
    )
    window.resizable (False, False)
    window.mainloop ()
