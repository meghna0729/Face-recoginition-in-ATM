import tkinter.messagebox

import login
import capture


def create_acc(email, passw):
    import pyrebase

    firebaseConfig = {
        'apiKey': "AIzaSyAPDBEezt1P1hx3lCq_Jdb1ijr0_qlPEbU",
        'authDomain': "swiftbankauth.firebaseapp.com",
        'projectId': "swiftbankauth",
        'storageBucket': "swiftbankauth.appspot.com",
        'messagingSenderId': "319488657428",
        'appId': "1:319488657428:web:29765311f4ffed314f3f01",
        'measurementId': "G-K5E4W95YY0",
        'databaseURL': "https://console.firebase.google.com/u/8/project/swiftbankauth/database/swiftbankauth-default-rtdb"
                       "/data/~2F "
    }

    firebase = pyrebase.initialize_app (firebaseConfig)
    auth = firebase.auth ()
    try:
        user = auth.create_user_with_email_and_password (email, passw)
        print ("Successfully created Account ")
        tkinter.messagebox._show ("verification", "Account created successfully....")
        capture.capture()
    except:
        print ("Failed to Create Account ")
        tkinter.messagebox._show ("error", "User already exists....")
        login.login ()
