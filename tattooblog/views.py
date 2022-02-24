from django.shortcuts import render
from.models import TattooPost

# Create your views here.


def tattoo_gallery(request):
    """
    Runs the url.py tattoo_gallery
    """
    tattooposts = TattooPost.objects.all().order_by('date')
    return render(request, 'tattooblog/tattoo_gallery.html', {'tattooposts': tattooposts})
