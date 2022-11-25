import cv2
import math
import sys
import numpy as np
import time
import os
import random



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

    per_r = '10' + '%'
    font = cv2.FONT_HERSHEY_COMPLEX
    percent_choise = 0
    while True:

        ret, frame = video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)


        for (x, y, z, h) in faces:
            percent_choise+=1
            cv2.rectangle(frame, (x, y), (x + z, y + h), (255, 0, 0), 2)
            if percent_choise < 50:
                continue
            cv2.putText(frame, (f"Сходство с junior-разработчиком:{per_r}"),(10,500), font, 1.5,(255,255,255),2,cv2.LINE_AA)

        x, imag = cv2.imencode('.jpg', frame)

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + imag.tobytes() + b'\r\n\r\n')
