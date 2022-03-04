from django.conf.urls import url
from . import views
from django.urls import path, include

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.account_signup, name="signup"),
    path('login/', views.login_view, name="login"),
]
