from django.urls import path
from .views import *


urlpatterns = [
    path('register/',RegisterApiView.as_view(),name='register'),
    path('login/',LoginApiView.as_view(),name='login'),
    path('logout/',LogoutAPIView.as_view(),name='logout'),
]

