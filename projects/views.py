from django.http  import HttpResponse
from django.shortcuts import render
import datetime as dt

# Create your views here.
def projects_today(request):
    date = dt.date.today()

    return render(request, 'today-projects.html', {"date":date,})    

def search_results(request):

    if 'topics' in request.GET and request.GET["topics"]:
        search_term = request.GET.get("topics")
        searched_articles = Topics.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"topics": searched_topics})

    else:
        message = "You haven't searched for any topic"
        return render(request, 'search.html',{"message":message})   