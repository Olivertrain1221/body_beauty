from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    """
    Opens the homepage view
    """
    return render(request, "homepage.html")


def about_page(request):
    """
    Function for opening about page
    """
    return render(request, "about.html")
