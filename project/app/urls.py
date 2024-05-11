from django.urls import path
from .views import*

urlpatterns = [
    path('', home, name='home'),
    path('insert/', insert, name='insert'),
    path('display/', display, name='display'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('update/<int:pk>/', update, name='update'),
    path('delet/<int:pk>/', delet, name='delet'),
]
