from django.urls import path
from . import views


urlpatterns = [
    path('', views.tattoo_gallery, name="gallery"),
    path('<slug:slug>/', views.tattoo_gallery_detail, name="post_detail"),
]
