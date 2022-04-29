from django.urls import path
from . import views
from .views import (TattooDetailListView,
                    TattooListView,
                    DeleteAPostView
                    )


app_name = 'tattooposts'

urlpatterns = [
    path('', TattooListView.as_view(), name="tattoo_gallery"),
    path('post/create/', views.postcreateview, name="tattoo_post_create"),
    path('<slug>', TattooDetailListView.as_view(), name="tattoopost_detail"),
    path('<slug>/update/', views.update_post_view, name="post_update"),
    path('<slug>/delete/', DeleteAPostView.as_view(),
         name="tattoopost_confirm_delete"),
]
