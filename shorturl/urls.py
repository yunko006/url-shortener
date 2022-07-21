from django.urls import path

from . import views

app_name = "shorturl"
urlpatterns = [
    # Home 
    path('',views.home, name='home'),
    # choisir un nom
    path('choose/', views.choose_url, name='choose_url'),
    # hash l'url
    path('generate/', views.generate_url, name='generate_url'),
    # si url deja dans la base de donnée 
    path('retrieve/', views.retrieve_url, name='retrieve'),
    # redirect vers le "vrai" lien
    path('<str:short>/', views.redirect_url, name='redirect_url'),
]
