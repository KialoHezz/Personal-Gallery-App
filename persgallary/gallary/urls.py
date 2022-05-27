from django.urls import path

from gallary.views import home_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home_view ,name='home-view'),
]