from . import views
from django.urls import path


app_name = 'accounts'

urlpatterns = [
    path('signup/', views.account_signup, name="signup"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('profile/', views.profile_view, name="profile"),
    path('profile/delete-account', views.delete_profile, name="deleteprofile"),
]
