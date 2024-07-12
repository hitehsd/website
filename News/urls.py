from re import search
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home" , views.index, name="index"),
    path("search/", views.search, name="search"),
    path("categories/<str:name>/", views.category, name="categories"),
]
