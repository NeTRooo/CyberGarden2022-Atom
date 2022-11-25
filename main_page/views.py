from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import logout
import json
import requests
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import threading

def main_page(request):
    return render(request, 'main_page/main_page.html')

def forms_page(request):
    return render(request, 'main_page/forms.html')

def quiz_page(request):
    return render(request, 'main_page/quiz.html')

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)