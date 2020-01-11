from django.shortcuts import render, redirect 
from newsapi import NewsApiClient 
from django.template import loader
from django.http import HttpResponse
from newsapp.models import techCrunchHeadline
#def home(request):
#   return HttpResponse("Hello, world. You're at the polls index.")



# importing api 

  
# Create your views here.  
def techCrunch(request):
    techCrunchHeadline.objects.all().delete() 
    newsapi = NewsApiClient(api_key ='7890f99f817b40a0a587325193ca0933') 
    top = newsapi.get_top_headlines(sources ='techcrunch') 
  
    l = top['articles'] 
    desc =[] 
    news =[] 
    img =[] 
  
    for i in range(len(l)): 
        f = l[i] 
        #news.append(f['title']) 
        #desc.append(f['description']) 
        #img.append(f['urlToImage']) 
        new_headline = techCrunchHeadline()
        new_headline.title = f['title']
        new_headline.url = f['url']
        new_headline.save()
    #TClist = zip(news, desc, img) 
    
    return redirect("../")

def news_list(request):
    headlines = techCrunchHeadline.objects.all()[::-1]
    context = {
        'object_list': headlines,
    }
    return render(request, "newsapp/home.html", context)


