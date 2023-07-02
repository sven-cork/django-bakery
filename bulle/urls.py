from . import views
from django.urls import path

urlpatterns = [
    path("", views.RecipieList.as_view(), name="home"),
    path('<slug:slug>/', views.RecipieDetail.as_view(), name='recipies_content')
]