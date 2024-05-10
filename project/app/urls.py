from django.urls import path
from .views import*

urlpatterns = [
    path('', home, name='home'),
    path('insert/', insert, name='insert'),
    path('display/', display, name='display'),
    path('edit/', edit, name='edit'),
    path('display/', display, name='display'),
]
