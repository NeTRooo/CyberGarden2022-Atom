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
<<<<<<< HEAD

def forms_page(request):
    return render(request, 'main_page/forms.html')

def quiz_page(request):
    return render(request, 'main_page/quiz.html')
=======
>>>>>>> 22b4b0c41a80199f62f2754ee0bc0821bf107e05
