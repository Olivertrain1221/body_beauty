from django.shortcuts import redirect, render
from.models import TattooPost
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from . import forms
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView
    )

# Create your views here.


class TattooListView(ListView):
    model = TattooPost
    template_name = 'tattooblog/tattoo_gallery.html'  
    context_object_name = 'tattooposts'
    ordering = ['-date']
## <app>/<model>_<viewtype>.html

class TattooDetailListView(DetailView):
    model = TattooPost
    template_name = 'tattooblog/tattoopost_detail.html'
    context_object_name = 'post'



## <app>/<model>_<viewtype>.html


class PostCreateView(LoginRequiredMixin, CreateView):
    model = TattooPost
    fields = ['title', 'body', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# @login_required(login_url="/accounts/login/")
# def tattoo_create(request):
#     """
#     Allows the user to go to create a post
#     and saves to database once user has been confirmed
#     """
#     if request.method == 'POST':
#         form = forms.CreatePost(request.POST, request.FILES)
#         if form.is_valid():
#             case = form.save(commit=False)
#             case.author = request.user
#             case.save()
#             return redirect('tattooposts:gallery')
#     else:
#         form = forms.CreatePost()
#     return render(request, 'tattooblog/tattoo_post_create.html', {'form': form })


class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = TattooPost
    fields = ['title', 'body', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
