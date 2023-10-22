from urllib import response
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    """Return HOME"""
    return render(request, "recipes/home.html", context={'nome':'Paulo'})


def contato(request):
    """Return Contato"""
    return HttpResponse("Contato!")


def sobre(request):
    """Return Sobre"""
    return render(request, "recipes/home.html")
