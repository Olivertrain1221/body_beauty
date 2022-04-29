from django.shortcuts import get_object_or_404, redirect, render
from tattooblog.forms import CreatePost, EditPost
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import TattooPost
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView
    )
from accounts.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class TattooListView(ListView):
    """
    Class base view of Tattoo model all posts
    """
    model = TattooPost
    template_name = 'tattooblog/tattoo_gallery.html'
    context_object_name = 'tattooposts'
    ordering = ['-id']


class TattooDetailListView(DetailView):
    """
    Class base view of Tattoo model singular posts
    """
    model = TattooPost
    template_name = 'tattooblog/tattoopost_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            profile = get_object_or_404(Profile, user=self.request.user)
        except:
            profile = None
        if profile is not None:
            context['profile'] = profile
            return context
        else:
            return context
    context_object_name = 'post'


def postcreateview(request):
    """
    Creates the post
    """
    form = CreatePost()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = CreatePost(request.POST, request.FILES)
        if form.is_valid():
            try:
                profile = get_object_or_404(Profile, user=request.user)
                tattoo_form = form.save(commit=False)
                tattoo_form.author = profile
                tattoo_form.save()
                return redirect('tattooposts:tattoo_gallery')
            except:
                messages.warning(request, 'Please Use an Image')
                context = {
                    'form': form
                }
                return render(request,
                              'tattooblog/tattoo_post_create.html', context)
        else:
            context = {
                'form': form
            }
            messages.warning(request, 'Please fill out the form accordingly.')
            return render(request,
                          'tattooblog/tattoo_post_create.html', context)

    return render(request, 'tattooblog/tattoo_post_create.html', context)


@login_required
def update_post_view(request, slug):
    """
    update
    """
    post = get_object_or_404(TattooPost, slug=slug)
    post_form = EditPost(instance=post)
    if request.method == 'POST':
        post_form = EditPost(request.POST,
                             request.FILES,
                             instance=post)
        if post_form.is_valid():
            try:
                post_form.save()
                messages.info(request, 'Post Updated!')
                return redirect('tattooposts:tattoo_gallery')
            except:
                messages.warning(request, 'Please Use an Image')
                context = {
                    'form': post_form
                }
                return render(request,
                              'tattooblog/tattoopost_form.html', context)

    context = {
        'form': post_form
    }

    return render(request, 'tattooblog/tattoopost_form.html', context)


class DeleteAPostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Class base view of deleting an original post
    """
    model = TattooPost
    success_message = "Post Deleted"
    success_url = '/tattooblog/'

    def test_func(self):
        post = self.get_object()
        profile = get_object_or_404(Profile, user=self.request.user)
        if profile == post.author:
            return True
        return False
