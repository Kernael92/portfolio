from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt 


# Create your views here.
def index(request):
    return render(request,'index.html')

def self(request):
    return render(request,'self.html')

def project(request):
    return render(request,'project.html')

