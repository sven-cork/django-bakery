from . import views
from django.urls import path, include
from bulle.views import *

urlpatterns = [
    path("", views.RecipieList.as_view(), name="home"),
    path('addrecipieform/', views.AddRecipie.as_view(), name='add_recipie'),
    path('deleterecipie/<recipie_id>/', delete_recipie, name='delete_recipie'),
    path('recipies/<slug:slug>/', views.RecipieDetail.as_view(), name='recipies_content'),
    path('like/<slug:slug>', views.recipie_like, name="recipie_like"),
    path('recipies/update/<slug:slug>/', views.UpdateRecipie.as_view(), name='update_recipie'),
    
]