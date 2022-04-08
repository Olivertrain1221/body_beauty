from django.urls import path
from .views import PostCreateView, TattooDetailListView, TattooListView, UpdatePostView


app_name = 'tattooposts'

urlpatterns = [
    path('', TattooListView.as_view(), name="tattoo_gallery"),
    path('post/create/',PostCreateView.as_view(), name="tattoo_post_create"),
    path('<slug>', TattooDetailListView.as_view(), name="post_detail"),
    path('<slug>/update/', UpdatePostView.as_view(), name="post_update"),
]
