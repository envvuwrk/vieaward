from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def gallery(request):
    return render(request, "gallery.html")


def calender(request):
    return render(request, "calender.html")


def contact(request):
    return render(request, "contact.html")
