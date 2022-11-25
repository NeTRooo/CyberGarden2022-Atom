from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import logout
import json
import requests
import cv2

def main_home(request):
    return render(request, 'main_page/main_page.html')

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
