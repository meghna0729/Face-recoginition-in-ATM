import pickle
import time
import tkinter
from collections import Counter
from tkinter import messagebox

import cv2
import imutils
import numpy as np
from imutils.video import FPS
from imutils.video import VideoStream

import front
import password

countter = 2


def video_check():
    global countter
    global real_user

    window = tkinter.Tk ()
    window.withdraw ()

    detector = cv2.dnn.readNetFromCaffe ('face_detection_model/deploy.prototxt',
                                         'face_detection_model/res10_300x300_ssd_iter_140000.caffemodel')

    # load our serialized face embedding model from disk
    print ("[INFO] loading face recognizer...")
    embedder = cv2.dnn.readNetFromTorch ('nn4.small2.v1.t7')

    # load the actual face recognition model along with the label encoder
    recognizer = pickle.loads (open ('output/recognizer.pickle', "rb").read ())
    le = pickle.loads (open ('output/le.pickle', "rb").read ())

    # initialize the video stream, then allow the camera sensor to warm up
    print ("[INFO] starting video stream...")
    vs = VideoStream (src=0).start ()
    time.sleep (2.0)

    # run check for only 15seconds and then stop
    timeout = time.time () + 5

    # start the FPS throughput estimator
    fps = FPS ().start ()

    # loop over frames from the video file stream
    real_user_list = []
    while True:

        # run check for only 15seconds and then stop
        if time.time () > timeout:
            cv2.destroyWindow ("Frame")
            break

        # grab the frame from the threaded video stream
        frame = vs.read ()

        # resize the frame to have a width of 600 pixels (while
        # maintaining the aspect ratio), and then grab the image
        # dimensions
        frame = imutils.resize (frame, width=800, height=200)
        (h, w) = frame.shape[:2]

        # construct a blob from the image
        imageBlob = cv2.dnn.blobFromImage (
            cv2.resize (frame, (300, 300)), 1.0, (300, 300),
            (104.0, 177.0, 123.0), swapRB=False, crop=False)

        # apply OpenCV's deep learning-based face detector to localize
        # faces in the input image
        detector.setInput (imageBlob)
        detections = detector.forward ()

        # loop over the detections
        for i in range (0, detections.shape[2]):
            # extract the confidence (i.e., probability) associated with
            # the prediction
            confidence = detections[0, 0, i, 2]

            # filter out weak detections
            if confidence > 0.5:
                # compute the (x, y)-coordinates of the bounding box for
                # the face
                box = detections[0, 0, i, 3:7] * np.array ([w, h, w, h])
                (startX, startY, endX, endY) = box.astype ("int")

                # extract the face ROI
                face = frame[startY:endY, startX:endX]
                (fH, fW) = face.shape[:2]

                # ensure the face width and height are sufficiently large
                if fW < 20 or fH < 20:
                    continue

                # construct a blob for the face ROI, then pass the blob
                # through our face embedding model to obtain the 128-d
                # quantification of the face
                faceBlob = cv2.dnn.blobFromImage (face, 1.0 / 255,
                                                  (96, 96), (0, 0, 0), swapRB=True, crop=False)
                embedder.setInput (faceBlob)
                vec = embedder.forward ()

                # perform classification to recognize the face
                preds = recognizer.predict_proba (vec)[0]
                j = np.argmax (preds)
                proba = preds[j]
                name = le.classes_[j]

                # # draw the bounding box of the face along with the
                # # associated probability

                # Decision boundary
                if (name == 'unknown') or (proba * 100) < 50:
                    print ("Fraud detected")
                    real_user_list.append (name)
                else:
                    # cv2.destroyWindow("Frame")
                    real_user_list.append (name)
                    break

        # update the FPS counter
        fps.update ()

        # show the output frame
        cv2.imshow ("Frame", frame)
        key = cv2.waitKey (1) & 0xFF

        # if the `q` key was pressed, break from the loop
        if key == ord ("q"):
            break

    # stop the timer and display FPS information
    fps.stop ()
    print ("[INFO] elasped time: {:.2f}".format (fps.elapsed ()))
    print ("[INFO] approx. FPS: {:.2f}".format (fps.fps ()))

    # do a bit of cleanup
    cv2.destroyAllWindows ()
    vs.stop ()
    print (real_user_list)

    try:
        Counter (real_user_list).most_common (1)[0][0] == 'unknown'
    except IndexError:
        if countter != 0:
            messagebox._show ("Verification Info!",
                              "Face Id match failed! You have {} trials left".format (countter))
            countter = countter - 1
            vs.stream.release ()
            video_check ()
        else:
            messagebox._show ("Verification Info!",
                              "Face Id match failed! You cannot withdraw at this time, try again later")
            vs.stream.release ()
            front.front ()
            countter = 2


    else:
        if Counter (real_user_list).most_common (1)[0][0] == 'unknown':
            if countter != 0:
                messagebox._show ("Verification Info!",
                                  "Face Id match failed! You have {} trials left".format (countter))
                countter = countter - 1
                vs.stream.release ()
                video_check ()
            else:
                messagebox._show ("Verification Info!",
                                  "Face Id match failed! You cannot withdraw at this time, try again later")
                vs.stream.release ()
                front.front ()
                countter = 2

        else:
            real_user = int (Counter (real_user_list).most_common (1)[0][0])
            print (real_user)
            messagebox._show ("Verification Info!", "Face Id match!")
            vs.stream.release ()
            cv2.destroyAllWindows ()
            password.password ()
