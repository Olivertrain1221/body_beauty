from django.urls import path
from . import views
from.models import TattooPost


urlpatterns = [
    path('', views.tattoo_gallery),
]
