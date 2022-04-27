from django.shortcuts import get_object_or_404
from .models import TattooPost
from accounts.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView
    )

# Create your views here.


class TattooListView(ListView):
    model = TattooPost
    template_name = 'tattooblog/tattoo_gallery.html'  
    context_object_name = 'tattooposts'
    ordering = ['-date']
    paginate = []


class TattooDetailListView(DetailView):
    model = TattooPost
    template_name = 'tattooblog/tattoopost_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if Profile.objects.filter(user = self.request.user).exists():
            profile = get_object_or_404(Profile, user=self.request.user)
            context['profile'] = profile
            return context
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = TattooPost
    template_name = 'tattooblog/tattoo_post_create.html'  
    fields = ['title', 'body', 'image']
    success_url = '/tattooblog/'

    def form_valid(self, form):
        profile = get_object_or_404(Profile, user=self.request.user)
        form.instance.author = profile
        return super().form_valid(form)


class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
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
    model = TattooPost
    success_url = '/tattooblog/'

    def test_func(self):
        post = self.get_object()
        profile = get_object_or_404(Profile, user=self.request.user)
        if profile == post.author:
            return True
        return False
