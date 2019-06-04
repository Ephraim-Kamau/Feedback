from django.http  import HttpResponse
from django.shortcuts import render
import datetime as dt

# Create your views here.
def welcome(request):
    return render( request, 'welcome.html')

def projects_today(request):
    date = dt.date.today()

    return render(request, 'all-projects/today-projects.html', {"date":date,})    

   