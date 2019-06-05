from django.http  import HttpResponse
from django.shortcuts import render
import datetime as dt

# Create your views here.
def projects_today(request):
    date = dt.date.today()

    return render(request, 'today-projects.html', {"date":date,})    

   