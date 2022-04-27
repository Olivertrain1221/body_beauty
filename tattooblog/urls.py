from django.urls import path
from .views import (PostCreateView,
                    TattooDetailListView,
                    TattooListView,
                    UpdatePostView,
                    DeleteAPostView
                    )


app_name = 'tattooposts'

urlpatterns = [
    path('', TattooListView.as_view(), name="tattoo_gallery"),
    path('post/create/', PostCreateView.as_view(), name="tattoo_post_create"),
    path('<slug>', TattooDetailListView.as_view(), name="tattoopost_detail"),
    path('<slug>/update/', UpdatePostView.as_view(), name="post_update"),
    path('<slug>/delete/', DeleteAPostView.as_view(),
         name="tattoopost_confirm_delete"),
]
