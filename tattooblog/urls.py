from django.urls import path
from . import views


app_name = 'tattooposts'

urlpatterns = [
    path('', views.tattoo_gallery, name="gallery"),
    path('create/', views.tattoo_create, name="create"),
    path('<slug>', views.tattoo_gallery_detail, name="post_detail"),
]
