
from django.urls import path
from newsapp.views import baseScrape, news_list

urlpatterns = [
  path('baseScrape/', baseScrape, name="baseScrape"),
  path('', news_list, name="home"),
]
