from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='games_home')
]