
from django.urls import path
from newsapp.views import techCrunch, news_list, wallStreetJournal

urlpatterns = [
  path('techCrunch/', techCrunch, name="techCrunch"),
  path('wallStreetJournal/', wallStreetJournal, name="wallStreetJournal"),
  path('', news_list, name="home"),
]
