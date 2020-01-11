
from django.urls import path
from newsapp.views import techCrunch, news_list
urlpatterns = [
  path('techCrunch/', techCrunch, name="techCrunch"),
  path('', news_list, name="home"),
]