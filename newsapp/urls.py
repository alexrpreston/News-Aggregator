
from django.urls import path
from newsapp.views import baseScrape, news_list, timeSince, about

urlpatterns = [
  path('about/', about, name="about"),
  path('', news_list, name="home"),
]
