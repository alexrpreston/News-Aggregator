from django.urls import path

from . import views

urlpatterns = [
    path('', views.techCrunch, name='techCrunch'),
    path('', views.wallStreetJournal, name='wallStreetJournal'),
]