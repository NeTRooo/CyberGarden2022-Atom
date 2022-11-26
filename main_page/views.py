from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import logout
import json
import requests
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import threading
import camera

def main_page(request):
    return render(request, 'main_page/main_page.html')

def forms_page(request):
    return render(request, 'main_page/forms.html')

def quiz_page(request):
    return render(request, 'main_page/quiz.html')

import cv2
import math
import sys
import numpy as np
import time
import os
import random
from django.views.decorators import gzip
from django.http import StreamingHttpResponse

import threading



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
    font = cv2.FONT_HERSHEY_COMPLEX
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    rand_lvl = [random.randrange(70, 100) for i in range(0, 50)]
    frame_cntr = 0
    while True:

        ret, frame = video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        i = 0
        for (x, y, z, h) in faces:
            frame_cntr += 1

            cv2.rectangle(frame, (x, y), (x + z, y + h), (255, 0, 0), 2)
            if frame_cntr < 100:
                cv2.putText(frame, f'Вы junior-разработчик на:{random.randrange(0, 100)}%', (x - 6, y), font, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
            else:
                i += 1
                cv2.putText(frame, f'Вы junior-разработчик на:{rand_lvl[i]}%', (x - 6, y), font, 0.7, (255, 255, 255), 2, cv2.LINE_AA)


        x, imag = cv2.imencode('.jpg', frame)

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + imag.tobytes() + b'\r\n\r\n')
@gzip.gzip_page
def livefe(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad! replace it with proper handling
        pass
#a