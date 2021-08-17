from . import views
from django.urls import path

app_name = 'main'

urlpatterns = [
    path('home/', views.home, name='home')
]
