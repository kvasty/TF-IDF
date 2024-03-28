from django.urls import path
from . import views

urlpatterns = [
    path('clear', views.clear, name='clear'),
    path('results', views.results, name='results'),
    path('', views.index, name='index'),
]
