# for writing data in the excel sheet(bank_details.csv)

import csv
from random import randint

import login


def write_csv():
    n = 10
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    account_number = randint (range_start, range_end)
    n = 5
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    unique_id = randint (range_start, range_end)
    bank = "Swift Bank"
    acc_balance = 10000
    email = login.get_email ()
    mobile_no = login.get_mob ()
    otp = 0
    password = login.get_pass ()
    with open (r'bank_details.csv', 'a', newline='\n') as f:
        writer = csv.writer (f)
        writer.writerow ([unique_id, account_number, email, bank, password, acc_balance, mobile_no])
