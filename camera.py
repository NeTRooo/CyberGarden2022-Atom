import cv2
import math
import sys
import numpy as np
import time
import os
import random
import time



class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        global video
        video = cv2.VideoCapture(0)

        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')

    def __del__(self):
        video.release()

    def get_frame(self):
        success, image = video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()


def gen(camera):
    CONFIDENCE = 0.5
    SCORE_THRESHOLD = 0.5
    IOU_THRESHOLD = 0.5

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


    font = cv2.FONT_HERSHEY_COMPLEX
    percent_choise = 0
    a = [random.randrange(70, 100) for i in range(0, 20)]
    while True:

        ret, frame = video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 100)
        rand_perc = str(random.randrange(1, 100))
        i = 0
        for (x, y, z, h) in faces:
            percent_choise+=1
            cv2.rectangle(frame, (x, y), (x + z, y + h), (255, 0, 0), 2)

            if percent_choise < 100:
                cv2.putText(frame, (f"junior-разработчик:{rand_perc}%"), (x, y), font, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
            else:
                i += 1
                cv2.putText(frame, (f"junior-разработчик:{a[i]}%"),(x-6,y-6), font, 0.7,(255,255,255),2,cv2.LINE_AA)

        x, imag = cv2.imencode('.jpg', frame)

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + imag.tobytes() + b'\r\n\r\n')
