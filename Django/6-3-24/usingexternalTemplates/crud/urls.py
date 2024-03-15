# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('register/', registration_view, name='register'),
    path('show_data/', show_data, name='show_data'),
    path('delete_data/<int:id>/', deleteView, name='delete_data'),
    path('update_data/<int:id>/', updateView, name='update_data'),

    # Add other URLs as needed
]
