from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def Home(request):
    return HttpResponse("Welcome to imobilis")


def about(request):
    return HttpResponse("about emobilis")


def courses(request):
    return HttpResponse("we offer variety of courses")


def contacts(request):
    return HttpResponse("you can reach us in the following number ......")


def directions(request):
    return HttpResponse("we are located in westlands.")
