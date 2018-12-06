from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt 


# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to the Kernel Portfolio')
def projects_today(request):
    date = dt.date.today()
    return render(request,'all-projects/today-projects.html', {"date": date,})

def past_days_projects(request,past_date):
    try:
        # Converts data from the string url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False
    if date == dt.date.today():
        return redirect(projects_today)
    return render(request, 'all-projects/past-projects.html', {"date":date})




