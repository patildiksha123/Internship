from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return  render (request , "index.html")

def signup(request):
    return  render (request , "signup.html")
    

def sign_In(request):
    return  render (request , "sign_In.html")

def sub(request):
    return  render (request , "sub.html")

