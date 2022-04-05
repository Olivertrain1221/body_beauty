from django.urls import path
from .views import TattooDetailListView, TattooListView, CreatePostView
from . import views


app_name = 'tattooposts'

urlpatterns = [
    path('', TattooListView.as_view(), name="gallery"),
    path('create/', CreatePostView.as_view(), name="create"),
    path('<slug>', TattooDetailListView.as_view(), name="post_detail"),
]


