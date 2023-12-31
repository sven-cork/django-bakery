from . import views
from django.urls import path, include
from bulle.views import *

urlpatterns = [
    path("", views.recipie_list, name="home"),
    path('addrecipieform/', views.add_recipie, name='add_recipie'),
    path('deleterecipie/<recipie_id>/', delete_recipie, name='delete_recipie'),
    path('recipies/<slug:slug>/', views.recipie_detail, name='recipies_content'),
    path('like/<slug:slug>', views.recipie_like, name="recipie_like"),
    path('recipies/update/<slug:slug>/', views.update_recipie, name='update_recipie'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]
