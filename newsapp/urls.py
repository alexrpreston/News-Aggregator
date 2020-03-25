
from django.urls import path
from newsapp.views import baseScrape, news_list, about

urlpatterns = [
  path('about/', about, name="about"),
  path('', news_list, name="home"),
]
