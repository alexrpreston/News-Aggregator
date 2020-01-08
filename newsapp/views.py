from django.shortcuts import render 
from newsapi import NewsApiClient 
from django.template import loader
from django.http import HttpResponse

#def home(request):
#   return HttpResponse("Hello, world. You're at the polls index.")



# importing api 

  
# Create your views here.  
def home(request): 
    newsapi = NewsApiClient(api_key ='7890f99f817b40a0a587325193ca0933') 
    top = newsapi.get_top_headlines(sources ='business-insider') 
  
    l = top['articles'] 
    desc =[] 
    news =[] 
    img =[] 
  
    for i in range(len(l)): 
        f = l[i] 
        news.append(f['title']) 
        desc.append(f['description']) 
        img.append(f['urlToImage']) 
    mylist = zip(news, desc, img) 
    
    #return HttpResponse(template.render(context, request))
    #return HttpResponse(template.render(context ={"mylist":mylist}, request))
    return render(request, 'home.html', context ={"mylist":mylist}) 