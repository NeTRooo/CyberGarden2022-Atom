from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import logout
import json
import requests
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import threading

def main_home(request):
    return render(request, 'main_page/main_page.html')
