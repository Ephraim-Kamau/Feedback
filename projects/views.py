from django.http  import HttpResponse
from django.shortcuts import render
import datetime as dt
from .forms import NewProfileForm

# Create your views here.
def projects_today(request):
    date = dt.date.today()

    return render(request, 'today-projects.html', {"date":date,})  

def profile(request):

    return render(request, 'profile.html',)


def new_profile(request):
    current_user=request.user

    if request.method=='POST':
        form=NewProfileForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)      
            post.profile = current_user
            post.save()
        return redirect("profile")
    else:
        form = NewProfileForm() 
    return render(request,'edit-profile.html',{"form":form}) 

def search_results(request):

    if 'topics' in request.GET and request.GET["topics"]:
        search_term = request.GET.get("topics")
        searched_articles = Topics.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"topics": searched_topics})

    else:
        message = "You haven't searched for any topic"
        return render(request, 'search.html',{"message":message})   