from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tattooblog', include("tattooblog.urls")),
    path('about/', views.about_page),
    path('', views.homepage),
]
