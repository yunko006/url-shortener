from django.urls import path

from . import views

app_name = "shorturl"
urlpatterns = [
    # Home 
    path('',views.home, name='home'),
    # choisir un nom
    path('test/', views.choose_url, name='choose_url'),
]
