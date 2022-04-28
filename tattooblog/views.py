from django.shortcuts import get_object_or_404
from .models import TattooPost
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
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
    ordering = ['-date']
    paginate = []


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


class PostCreateView(LoginRequiredMixin, CreateView):
    """
    Class base view of Tattoo model creating a post
    """
    model = TattooPost
    template_name = 'tattooblog/tattoo_post_create.html'
    fields = ['title', 'body', 'image']
    success_url = '/tattooblog/'

    def form_valid(self, form):
        profile = get_object_or_404(Profile, user=self.request.user)
        form.instance.author = profile
        return super().form_valid(form)


class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Class base view of updating an original post
    """
    model = TattooPost
    fields = ['title', 'body', 'image']
    template_name = 'tattooblog/tattoopost_form.html'
    success_url = '/tattooblog/'

    def form_valid(self, form):
        profile = get_object_or_404(Profile, user=self.request.user)
        form.instance.author = profile
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        profile = get_object_or_404(Profile, user=self.request.user)
        if profile == post.author:
            return True
        return False


class DeleteAPostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Class base view of deleting an original post
    """
    model = TattooPost
    success_message = "YOU DID IT OLLIE was updated successfully"
    success_url = '/tattooblog/'

    def test_func(self):
        post = self.get_object()
        profile = get_object_or_404(Profile, user=self.request.user)
        if profile == post.author:
            return True
        return False

        ######## FIGURE OUT THE MESDSAGES ON CLASS BASED VIEWS IMPOPRT THE MIXIN AT TOP ADN TO ABOVE FUNCTION