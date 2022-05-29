import tkinter
from tkinter import Canvas, Entry, Button, PhotoImage
from tkinter import messagebox

import pandas as pd

import otp
import video_check

otp_no = 0


def password():
    from pathlib import Path
    import front

    OUTPUT_PATH = Path (__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path ("./password")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path (path)

    data = pd.read_csv ('bank_details.csv')

    def send_otp():
        # sending otp on the registered mobile no
        import random
        import requests
        import json

        global otp_no

        url = "https://www.fast2sms.com/dev/bulkV2"
        phone_no = data[data.loc[:, 'unique_id'] == video_check.real_user].loc[:, 'mobile_no'].values[0]
        print (phone_no)

        otp_no = random.randint (1000, 9999)

        my_data = {

            'sender_id': 'FSTSMS',
            'message': ('YOUR OTP FOR LOGIN IS ' + str (otp_no)),
            'language': 'english',
            'route': 'p',
            'numbers': phone_no
        }

        headers = {
            'authorization': 'mETJL973ifpZ4X58M0rUONYuHaWehPSBwQv2yRxKnlqobIkACzxILfSWGoqm98ZACXineY5R1PBaHshc',
            'Content-Type': "application/x-www-form-urlencoded",
            'Cache-Control': "no-cache"
        }
        # make a post request
        response = requests.request ("POST", url, data=my_data, headers=headers)
        returned_msg = json.loads (response.text)

        print (returned_msg['message'])
        otp.otp ()

    def verify_user():
        gottenPassword = data[data.loc[:, 'unique_id'] == video_check.real_user].loc[:, 'password'].values[0]
        print (str (gottenPassword))
        gottenEmail = data[data.loc[:, 'unique_id'] == video_check.real_user].loc[:, 'name'].values[0]
        print (str (gottenEmail))
        if str (entry_1.get ()) == str (gottenPassword):
            window.destroy ()
            messagebox._show ("Verification Info!", "Verification Successful!")
            send_otp ()
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
    gottenEmail = data[data.loc[:, 'unique_id'] == video_check.real_user].loc[:, 'name'].values[0]

    canvas.create_text (
        35.0,
        180.0,
        anchor="nw",
        text="Welcome " + gottenEmail,
        fill="#E5F80F",
        font=("Inter Bold", 28 * -1)
    )
    canvas.create_text (
        35.0,
        223.0,
        anchor="nw",
        text="Please Enter Your Password",
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
