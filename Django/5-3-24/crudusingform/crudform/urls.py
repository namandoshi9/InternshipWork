from django.urls import path
from .views import *

urlpatterns = [
    path('', addemployeeView,name='addemp'),
    path('updateemp/<int:id>/', updateemployeeView,name='updateemp'),
    path('deleteemp/<int:id>/', deleteemployeeView,name='deleteemp'),
]