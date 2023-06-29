from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.liste, name='url_liste'),
    path('', views.nouveau, name='url_nouveau'),
    path('', views.redirection, name='url_redirection'),
]
