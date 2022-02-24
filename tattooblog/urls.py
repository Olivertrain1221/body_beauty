from django.urls import path
from . import views


urlpatterns = [
    path('', views.tattoo_gallery),
]
