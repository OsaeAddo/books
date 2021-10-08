from django.urls import path

from .views import HomePageView


urlpatters = [
    path('', HomePageView.as_view(), name='home')
]