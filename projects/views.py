from django.http  import HttpResponse
from django.shortcuts import render,redirect
import datetime as dt
from .forms import NewProfileForm,NewTopicsForm,NewCommentsForm
from .models import Topics,Comments,Profile
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/accounts/login/')
def projects_today(request):
    topics = Topics.objects.all()

    return render(request, 'today-projects.html', {"topics":topics})  

def profile(request):

    return render(request, 'profile.html')

def always_topic(request):
    topics = Topics.objects.all()
    comments = Comments.objects.all()

    return render(request, 'always.html',{"topics":topics, "comments":comments}) 

@login_required(login_url='/accounts/login/')
def comment(request):
    current_user=request.user

    if request.method=='POST':
        form=NewCommentsForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)      
            post.profile = current_user
            post.save()
        return redirect("always_topic")
    else:
        form = NewCommentsForm() 
    return render(request,'comments.html',{"form":form}) 

    
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


def new_topic(request):
    current_user=request.user

    if request.method=='POST':
        form=NewTopicsForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)      
            post.profile = current_user
            post.save()
        return redirect("projectsToday")
    else:
        form = NewTopicsForm() 
    return render(request,'new-topic.html',{"form":form})  

def search_results(request):

    if 'topics' in request.GET and request.GET["topics"]:
        search_term = request.GET.get("topics")
        searched_topics = Topics.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"topics": searched_topics})

    else:
        message = "You haven't searched for any topic"
        return render(request, 'search.html',{"message":message})   