import os
from tkinter import messagebox

import cv2
import pandas as pd

import embedding
import front
import traning


def capture_user():
    data = pd.read_csv ('bank_details.csv')
    name = data.loc[:, 'unique_id'].values[-1]
    cam = cv2.VideoCapture (0)

    cv2.namedWindow ("capture")

    img_counter = 0

    dirname = f'dataset/{name}'
    os.mkdir (dirname)

    while True:
        ret, frame = cam.read ()
        cv2.imshow ("capture", frame)

        if img_counter == 5:
            cv2.destroyWindow ("capture")
            break
        if not ret:
            break
        k = cv2.waitKey (1)

        if k % 256 == 27:
            # ESC pressed
            messagebox._show ('Error!', "Escape hit, closing...")
            break
        elif k % 256 == 32:
            # SPACE pressed
            path = f'dataset/{name}'
            img_name = "{}.jpg".format (img_counter)
            cv2.imwrite (os.path.join (path, img_name), frame)
            cv2.imwrite (img_name, frame)
            print ("{} written!".format (img_name))
            img_counter += 1

    cam.release ()

    cv2.destroyAllWindows ()

    embedding.get_embeddings ()
    # self.get_embeddings()
    traning.train_model ()
    messagebox._show ('Registration Info!', 'Face Id Successfully Registered!')
    front.front ()
