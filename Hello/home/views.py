from django.shortcuts import render, HttpResponse
import socket


# Create your views here.
def index(request):
    context = {"variable": socket.gethostname()}
    return render(request, "index.html", context)
    # return HttpResponse("This is home page")


def about(request):
    context = {"variable": socket.gethostname()}
    return render(request, "about.html", context)
    #return HttpResponse("This is about page")


def services(request):
    context = {"variable": socket.gethostname()}
    return render(request, "services.html", context)
    #return HttpResponse("This is services page")


def contact(request):
    context = {"variable": socket.gethostname()}
    return render(request, "contact.html", context)
    #return HttpResponse("This is the contact page")
