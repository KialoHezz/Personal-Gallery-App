from django.urls import path

from gallary.views import (home_view,about_view,index_view,travel_view,food_view,add_travel,category,view_image)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home_view ,name='home-view'),
    path('view_image/<int:pk>/',view_image, name='view_image'),
    path('category/',category, name='category'),
    path('add-travel/',add_travel,name='add_travel'),
    path('foods/',food_view,name='food_view'),
    path('travelled-places/',travel_view,name='travel_view'),
    path('index/' ,index_view ,name='index_view'),
    path('about/', about_view , name='about_view'),
]