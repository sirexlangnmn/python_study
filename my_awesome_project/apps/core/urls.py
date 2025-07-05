from django.urls import path
from .views import HomeView, time_view

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('time/', time_view, name='time'),
]
