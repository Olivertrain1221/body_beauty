from django.contrib import admin
from django.urls import path, include
from . import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name="homepage"),
    path('about/', views.about_page, name="about"),
    path('tattooblog/', include("tattooblog.urls")),
    path('accounts/', include("accounts.urls")),
]
