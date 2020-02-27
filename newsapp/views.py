from django.shortcuts import render, redirect 
from newsapi import NewsApiClient 
from django.template import loader
from django.http import HttpResponse
from newsapp.models import techCrunchHeadline
from newsapp.models import wallStreetJournalHeadline
from newsapp.models import theVergeHeadline
from newsapp.models import wiredHeadline
from newsapp.models import seekingAlphaHeadline
from newsapp.models import businessInsiderHeadline
from newsapp.models import lastUpdated


from datetime import timedelta
import time, os
#def home(request):
#   return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.  

def about(request):
    return render(request, "newsapp/about.html")

def baseScrape(request):
    techCrunchHeadline.objects.all().delete() 
    wallStreetJournalHeadline.objects.all().delete() 
    theVergeHeadline.objects.all().delete() 
    
    lastUpdated.objects.all().delete()
    KEY = os.getenv('NEWS_API_KEY')
    newsapi = NewsApiClient(api_key = KEY) 
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
        new_headline.desc = f['description']
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
        new_headline.desc = f['description']
        new_headline.url = f['url']
        new_headline.save()

    TVtop = newsapi.get_top_headlines(sources ='hacker-news')

    tvjl = TVtop['articles'] 
    desc =[] 
    news =[] 
    img =[] 
  
    for i in range(len(l)): 
        f = tvjl[i] 
        new_headline = theVergeHeadline()
        new_headline.title = f['title']
        new_headline.desc = f['description']
        new_headline.url = f['url']
        new_headline.save()

    #Business Insider scraper
    BItop = newsapi.get_top_headlines(sources ='business-insider')

    tvjl = TVtop['articles'] 
    desc =[] 
    news =[] 
    img =[] 
  
    for i in range(len(l)): 
        f = tvjl[i] 
        new_headline = businessInsiderHeadline()
        new_headline.title = f['title']
        new_headline.desc = f['description']
        new_headline.url = f['url']
        new_headline.save()

    #Wired Scraper
    Wtop = newsapi.get_top_headlines(sources ='wired')

    tvjl = TVtop['articles'] 
    desc =[] 
    news =[] 
    img =[] 
  
    for i in range(len(l)): 
        f = tvjl[i] 
        new_headline = wiredHeadline()
        new_headline.title = f['title']
        new_headline.desc = f['description']
        new_headline.url = f['url']
        new_headline.save()

    #Seeking Alpha
    TVtop = newsapi.get_top_headlines(sources ='the-verge')

    tvjl = TVtop['articles'] 
    desc =[] 
    news =[] 
    img =[] 
  
    for i in range(len(l)): 
        f = tvjl[i] 
        new_headline = seekingAlphaHeadline()
        new_headline.title = f['title']
        new_headline.desc = f['description']
        new_headline.url = f['url']
        new_headline.save()

    newTime = lastUpdated()
    os.environ['UTC'] = 'US/Eastern'
    time.tzset()
    t = time.localtime()
    newTime.hours = time.strftime("%I" , t)
    newTime.minutes = time.strftime("%M" , t)
    
    newTime.save()
    return redirect("../")


def news_list(request):
    #The first 5 headlines for each news site
    TCheadlinesShort = techCrunchHeadline.objects.all()[:5]
    WSJHeadLinesShort = wallStreetJournalHeadline.objects.all()[:5]
    TVHeadlLinesShort = theVergeHeadline.objects.all()[:5] 
    WiredheadlinesShort = wiredHeadline.objects.all()[:5]
    SkAlphaHeadLinesShort = seekingAlphaHeadline.objects.all()[:5]
    BIHeadlLinesShort = businessInsiderHeadline.objects.all()[:5]    

    #The rest of the headlines for each news site
    TCheadlinesFull = techCrunchHeadline.objects.all()[5:]
    WSJHeadLinesFull = wallStreetJournalHeadline.objects.all()[5:]
    TVHeadlLinesFull = theVergeHeadline.objects.all()[5:]   
    WiredheadlinesFull = techCrunchHeadline.objects.all()[5:]
    SkAlphaHeadLinesFull = wallStreetJournalHeadline.objects.all()[5:]
    BIHeadlLinesFull = businessInsiderHeadline.objects.all()[5:]  
    
    #timeOfUpdate = 10
    context = {
        'TCobject_listHalf': TCheadlinesShort,
        'WSJobject_listHalf' : WSJHeadLinesShort,
        'TVobject_listHalf' : TVHeadlLinesShort,
        'Wiredobject_listHalf': WiredheadlinesShort,
        'SAobject_listHalf' : SkAlphaHeadLinesShort,
        'BIobject_listHalf' : BIHeadlLinesShort,
        'TCobject_listRest': TCheadlinesFull,
        'WSJobject_listRest' : WSJHeadLinesFull,
        'TVobject_listRest' : TVHeadlLinesFull,
        'Wiredobject_listRest': WiredheadlinesFull,
        'SAobject_listRest' : SkAlphaHeadLinesFull,
        'BIobject_listRest' : BIHeadlLinesFull,
        
    }
    return render(request, "newsapp/home.html", context)

def timeSince(request):
    minutes = 10

    os.environ['UTC'] = 'US/Eastern'
    time.tzset()
    t = time.localtime()
    currentMinutes = int(time.strftime("%M" , t))

    minutesSinceUpdate = 0
    if minutes > currentMinutes:
        minutesSinceUpdate = (60 - minutes) + currentMinutes
    else:
        minutesSinceUpdate = currentMinutes - minutes

    context = {
        'minutes_since_update' : minutesSinceUpdate 
    }
    return render(request, "newsapp/lastUpdated.html", context)