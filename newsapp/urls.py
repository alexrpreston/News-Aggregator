
from django.urls import path
from newsapp.views import baseScrape, news_list, timeSince, about

urlpatterns = [
  path('baseScrape/', baseScrape, name="baseScrape"),
  path('about/', about, name="about"),
  path('timeSince/', timeSince, name="timeSince"),
  path('', news_list, name="home"),
]
