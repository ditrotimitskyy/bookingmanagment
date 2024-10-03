from django.urls import path
from .views import index, cabin_list, visitors_list, new_cabin

urlpatterns = [
    path("", index, name="index"),
    path("cabin/", cabin_list, name="cabin"),
    path("visitor/", visitors_list, name="visitor"),
    path("new_cabin/", new_cabin, name="new_cabin"),
]
