from django.shortcuts import render, redirect 
from newsapi import NewsApiClient 
from django.template import loader
from django.http import HttpResponse
from newsapp.models import techCrunchHeadline
from newsapp.models import wallStreetJournalHeadline
from newsapp.models import theVergeHeadline
from newsapp.models import lastUpdated
from datetime import timedelta
import time, os
#def home(request):
#   return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.  
def baseScrape(request):
    techCrunchHeadline.objects.all().delete() 
    wallStreetJournalHeadline.objects.all().delete() 
    theVergeHeadline.objects.all().delete() 
    
    lastUpdated.objects.all().delete() 
    newsapi = NewsApiClient(api_key ='7890f99f817b40a0a587325193ca0933') 
    top = newsapi.get_top_headlines(sources ='techcrunch') 
  
    l = top['articles'] 
    desc =[] 
    news =[] 
    img =[] 
  
    for i in range(len(l)): 
        f = l[i] 
        new_headline = techCrunchHeadline()
        new_headline.title = f['title']
        new_headline.url = f['url']
        new_headline.save()
    
    WSJtop = newsapi.get_top_headlines(sources ='the-wall-street-journal') 
  
    wsjl = WSJtop['articles'] 
    desc =[] 
    news =[] 
    img =[] 
  
    for i in range(len(l)): 
        f = wsjl[i] 
        new_headline = wallStreetJournalHeadline()
        new_headline.title = f['title']
        new_headline.url = f['url']
        new_headline.save()

    TVtop = newsapi.get_top_headlines(sources ='the-verge')

    tvjl = TVtop['articles'] 
    desc =[] 
    news =[] 
    img =[] 
  
    for i in range(len(l)): 
        f = tvjl[i] 
        new_headline = theVergeHeadline()
        new_headline.title = f['title']
        new_headline.url = f['url']
        new_headline.save()

    newTime = lastUpdated()
    os.environ['TZ'] = 'US/Eastern'
    time.tzset()
    t = time.localtime()
    newTime.time = time.strftime("%I:%M %p %Z" , t)
    
    newTime.save()
    return redirect("../")


def news_list(request):
    TCheadlines = techCrunchHeadline.objects.all()[::-1]
    WSJHeadLines = wallStreetJournalHeadline.objects.all()[::-1]
    TVHeadlLines = theVergeHeadline.objects.all()[::-1]
    timeOfUpdate = lastUpdated.objects.all()[0]
    context = {
        'TCobject_list': TCheadlines,
        'WSJobject_list' : WSJHeadLines,
        'TVobject_list' : TVHeadlLines,
        'update_Time' : timeOfUpdate,
    }
    return render(request, "newsapp/home.html", context)

def updater(request):
    starttime=time.time()
    while True:
        techCrunch(request)
        time.sleep(60.0 - ((time.time() - starttime) % 60.0))