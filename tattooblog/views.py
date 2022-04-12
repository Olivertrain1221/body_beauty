from.models import TattooPost
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
## <app>/<model>_<viewtype>.html

class TattooDetailListView(DetailView):
    model = TattooPost
    template_name = 'tattooblog/tattoopost_detail.html'
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = TattooPost
    template_name = 'tattooblog/tattoo_post_create.html'  
    fields = ['title', 'body', 'image']
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = TattooPost
    fields = ['title', 'body', 'image']
    template_name = 'tattooblog/tattoopost_form.html'  
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class DeleteAPostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = TattooPost
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


