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

def baseScrape():

    techCrunchHeadline.objects.all().delete()
    wallStreetJournalHeadline.objects.all().delete()
    theVergeHeadline.objects.all().delete()
    seekingAlphaHeadline.objects.all().delete()
    businessInsiderHeadline.objects.all().delete()
    wiredHeadline.objects.all().delete()


    KEY = os.getenv('NEWS_API_KEY')
    newsapi = NewsApiClient(api_key = KEY) 
    top = newsapi.get_top_headlines(sources ='techcrunch')

    tcl = top['articles']
    desc =[]
    news =[]
    img =[]

    for i in range(len(tcl)):
        f = tcl[i]
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

    for i in range(len(wsjl)):
        f = wsjl[i]
        new_headline = wallStreetJournalHeadline()
        new_headline.title = f['title']
        new_headline.desc = f['description']
        new_headline.url = f['url']
        new_headline.save()

    TVtop = newsapi.get_top_headlines(sources ='hacker-news')

    hnl = TVtop['articles']
    desc =[]
    news =[]
    img =[]

    for i in range(len(hnl)):
        f = hnl[i]
        new_headline = theVergeHeadline()
        new_headline.title = f['title']
        new_headline.desc = f['description']
        new_headline.url = f['url']
        new_headline.save()

    #Business Insider scraper
    BItop = newsapi.get_top_headlines(sources ='business-insider')

    BIl = BItop['articles']
    desc =[]
    news =[]
    img =[]

    for i in range(len(BIl)):
        f = BIl[i]
        new_headline = businessInsiderHeadline()
        new_headline.title = f['title']
        new_headline.desc = f['description']
        new_headline.url = f['url']
        new_headline.save()

    #Wired Scraper
    Wtop = newsapi.get_top_headlines(sources ='wired')

    wl = Wtop['articles']
    desc =[]
    news =[]
    img =[]

    for i in range(len(wl)):
        f = wl[i]
        new_headline = wiredHeadline()
        new_headline.title = f['title']
        new_headline.desc = f['description']
        new_headline.url = f['url']
        new_headline.save()

    #CNBC Articles
    CNBCtop = newsapi.get_top_headlines(sources ='cnbc')

    cnbcl = CNBCtop['articles']
    desc =[]
    news =[]
    img =[]

    for i in range(len(cnbcl)):
        f = cnbcl[i]
        new_headline = seekingAlphaHeadline()
        new_headline.title = f['title']
        new_headline.desc = f['description']
        new_headline.url = f['url']
        new_headline.save()






    #newTime = lastUpdated()
    os.environ['UTC'] = 'US/Eastern'
    time.tzset()
    t = time.localtime()
    #newTime.minutes = int(time.strftime("%M" , t))

    timeFile = open("/home/alexrpreston/alexrpreston.pythonanywhere.com/timeHolder.txt","w+")
    timeFile.write(time.strftime("%M" , t))
    print("Minutes of Last update to write to Txt File: ",time.strftime("%M" , t))
    timeFile.close()


    timeFile = open("/home/alexrpreston/alexrpreston.pythonanywhere.com/timeHolder.txt","r")
    oldTime = timeFile.read()
    print("Minutes of Last update from Txt File: ",oldTime)
    timeFile.close()

    #print(int(time.strftime("%M" , t)))
    #newTime.save()

    #timeOfUpdate = lastUpdated.objects.all()[0]
    #print(timeOfUpdate)
    #return redirect("../")


def news_list(request):
    lastUpdated.objects.all().delete()
    newTime = lastUpdated()
    os.environ['UTC'] = 'US/Eastern'
    time.tzset()
    t = time.localtime()

    timeFile = open("/home/alexrpreston/alexrpreston.pythonanywhere.com/timeHolder.txt","r")
    oldTime = timeFile.read()
    timedifference = int(time.strftime("%M" , t)) - int(oldTime)
    if timedifference < 0:
        timedifference = 60 - abs(int(time.strftime("%M" , t)) - int(oldTime))
    timeFile.close()

    newTime = lastUpdated()
    newTime.minutes = timedifference
    newTime.save()

    timeOfUpdate = lastUpdated.objects.all()[0]
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
    WiredheadlinesFull = wiredHeadline.objects.all()[5:]
    SkAlphaHeadLinesFull = seekingAlphaHeadline.objects.all()[5:]
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
        'time_updated' : timeOfUpdate,

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