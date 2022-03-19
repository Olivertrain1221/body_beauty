from django.shortcuts import redirect, render
from.models import TattooPost
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from django.views.generic import UpdateView

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
    tattoopost = TattooPost.objects.get(slug=slug)
    return render(request, 'tattooblog/tattoopost_detail.html', {'post': tattoopost})


@login_required(login_url="/accounts/login/")
def tattoo_create(request):
    """
    Allows the user to go to create a post
    and saves to database once user has been confirmed
    """
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            case = form.save(commit=False)
            case.author = request.user
            case.save()
            return redirect('tattooposts:gallery')
    else:
        form = forms.CreatePost()
    return render(request, 'tattooblog/tattoo_post_create.html', {'form': form })
