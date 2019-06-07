from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("Felicidades! Completaron la practica no. 1")
