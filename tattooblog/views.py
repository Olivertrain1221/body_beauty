from django.shortcuts import render
from.models import TattooPost
from django.http import HttpResponse

# Create your views here.


def tattoo_gallery(request):
    """
    Runs the url.py tattoo_gallery
    """
    tattooposts = TattooPost.objects.all().order_by('date')
    return render(request, 'tattooblog/tattoo_gallery.html', {'tattooposts': tattooposts})


def tattoo_gallery_detail(request, slug):
    """
    Enables the view of each post
    """
    return HttpResponse(slug)
