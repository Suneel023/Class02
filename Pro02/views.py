from django.http import HttpResponse
from django.shortcuts import render

def main(request):
    return HttpResponse("Main Django")

def index(request):
    return HttpResponse("Hello World Django")

def home(request):
    return HttpResponse("<h1>Welcome to Django Home Page</h1>")

def html_demo(request):
    return render(request,"sample.html")

def html_demo2(request):
    return render(request,"sample2.html")
