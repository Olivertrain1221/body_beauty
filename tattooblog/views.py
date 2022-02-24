from django.shortcuts import render

# Create your views here.
def tattoo_gallery(request):
    """
    Runs the url.py tattoo_gallery
    """
    tattooposts = TattooPost.objects.all()
    return render(request, 'tattooblog/tattoo_gallery.html')
