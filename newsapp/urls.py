
from django.urls import path
from newsapp.views import baseScrape, news_list, timeSince

urlpatterns = [
  path('baseScrape/', baseScrape, name="baseScrape"),
  path('timeSince/', timeSince, name="timeSince"),
  path('', news_list, name="home"),
]
