from django.urls import path

from gallary.views import (home_view,about_view,index_view,categories_view,view_image,add_details)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home_view ,name='home_view'),
    path('add/',add_details, name='add_details'),
    path('category/', categories_view, name='categories_view'),
    path('view_image/<int:pk>/',view_image, name='view_image'),
    path('index/' ,index_view ,name='index_view'),
    path('about/', about_view , name='about_view'),
]