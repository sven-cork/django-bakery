from . import views
from django.urls import path

urlpatterns = [
    path("", views.RecipieList.as_view(), name="home"),
]