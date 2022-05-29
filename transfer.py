import tkinter

import pandas as pd

import video_check


def transfer():
    from pathlib import Path
    import transaction

    from tkinter import Canvas, Entry, Button, PhotoImage, messagebox

    OUTPUT_PATH = Path (__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path ("./transfer")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path (path)

    def user_transc():

        data = pd.read_csv ('bank_details.csv')
        if int (entry_2.get ()) not in data['account_number'].values:
            messagebox._show ("Transfer Info!", "Invalid account number")
            window.destroy ()
            transaction.transaction ()
        elif int (entry_2.get ()) == video_check.real_user:
            messagebox._show ("Transfer Info!", "Sorry, you cannot make a transfer to yourself")
            window.destroy ()
            transaction.transaction ()
        elif int (entry_1.get ()) >= \
                data[data.loc[:, 'unique_id'] == video_check.real_user].loc[:, 'account_balance'].values[0]:
            messagebox._show ("Transfer Info!", "Insufficient Funds")
            window.destroy ()
            transaction.transaction ()
        else:
            data = pd.read_csv ('bank_details.csv')
            update_data = data.set_index ('account_number')
            update_data.loc[int (entry_2.get ()), 'account_balance'] += int (entry_1.get ())
            update_data.loc[data[data.loc[:, 'unique_id'] == video_check.real_user].loc[:, 'account_number'].values[
                                0], 'account_balance'] -= int (entry_1.get ())
            update_data['account_number'] = update_data.index
            update_data.reset_index (drop=True, inplace=True)
            update_data = update_data.reindex (
                labels=['unique_id', 'account_number', 'email', 'bank', 'password', 'acc_balance', 'mobile_no'], axis=1)
            update_data.to_csv ('bank_details.csv', index=None)
            messagebox._show ("Transfer Info!", "Successfully Transferred")
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
        260.0,
        344.0,
        image=entry_image_1
    )
    entry_1 = Entry (window,
                     bd=0,
                     bg="#F1B191",
                     highlightthickness=0
                     )
    entry_1.place (
        x=140.0,
        y=322.0,
        width=231.0,
        height=42.0
    )

    entry_image_2 = PhotoImage (
        file=relative_to_assets ("entry_2.png"))
    entry_bg_2 = canvas.create_image (
        256.5,
        189.0,
        image=entry_image_2
    )
    entry_2 = Entry (window,
                     bd=0,
                     bg="#F1B191",
                     highlightthickness=0
                     )
    entry_2.place (
        x=140.0,
        y=167.0,
        width=220.0,
        height=42.0
    )

    canvas.create_text (
        50.0,
        267.0,
        anchor="nw",
        text="Enter Amount To Transfer",
        fill="#000000",
        font=("Imprima Regular", 35 * -1)
    )

    canvas.create_text (
        0.0,
        97.0,
        anchor="nw",
        text="Enter reciepient’s account number",
        fill="#000000",
        font=("Imprima Regular", 35 * -1)
    )

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
                       command=lambda: (user_transc ()),
                       relief="flat"
                       )
    button_2.place (
        x=79.0,
        y=437.0,
        width=336.0,
        height=142.0
    )
    window.resizable (False, False)
    window.mainloop ()
