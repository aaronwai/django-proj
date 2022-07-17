from django.shortcuts import render
from django.http import HttpResponse

# create a function for for the index link to urls API route


def index(request):
    return render(request, "pages/index.html")


def about(request):
    return render(request, "pages/about.html")
