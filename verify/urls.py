from django.urls import path, include
from .views import my_view

urlpatterns = [
    path('list/', my_view, name='list'),
]