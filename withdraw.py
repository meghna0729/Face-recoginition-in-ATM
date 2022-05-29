import tkinter
from tkinter import messagebox

import pandas as pd

import transaction
import video_check


def with_draw():
    from pathlib import Path

    from tkinter import Canvas, Entry, Button, PhotoImage

    OUTPUT_PATH = Path (__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path ("./withdraw")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path (path)

    window = tkinter.Toplevel ()

    window.geometry ("1100x800")
    window.configure (bg="#FFFFFF")

    def user_withdrawl_trans():
        data = pd.read_csv ('bank_details.csv')
        update_data = data.set_index ('unique_id')
        if int (entry_1.get ()) % 500 != 0:
            messagebox._show ("withdrawl info!", "please enter amount in multiple of 500")
        elif int (entry_1.get ()) <= update_data.loc[video_check.real_user, 'account_balance']:
            update_data.loc[video_check.real_user, 'account_balance'] -= int (entry_1.get ())
            update_data.reset_index (inplace=True)
            update_data.columns = ['unique_id', 'account_number', 'email', 'bank', 'password', 'acc_balance', 'mobile_no']
            update_data.to_csv ('bank_details.csv', index=None)
            messagebox._show ("Withdrwawal Info!", "Successfully Withdrwan, please take your cash")
            window.destroy ()
            transaction.transaction ()
        else:
            messagebox._show ("Withdrwal Info!", "Insufficient Funds")
            window.destroy ()
            transaction.transaction ()

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
        x=79.0,
        y=563.0,
        width=322.0,
        height=177.0
    )

    button_image_2 = PhotoImage (
        file=relative_to_assets ("button_2.png"))
    button_2 = Button (window,
                       image=button_image_2,
                       borderwidth=0,
                       highlightthickness=0,
                       command=lambda: user_withdrawl_trans (),
                       relief="flat"
                       )
    button_2.place (
        x=79.0,
        y=437.0,
        width=336.0,
        height=142.0
    )

    canvas.create_text (
        54.0,
        243.0,
        anchor="nw",
        text="Enter Amount To Withdraw",
        fill="#000000",
        font=("Imprima Regular", 35 * -1)
    )

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
    window.resizable (False, False)
    window.mainloop ()
