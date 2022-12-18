from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from LES1.forms import RegisterForm, UserForm,EventForm
from .models import UserData,Event
from .utils import Calendar
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from django.views import generic
from datetime import date, datetime,timedelta
import calendar
from .models import * 
from LES1.forms import * 


# Create your views here.
def create_events(request):
    print("HI I entered here")
    if request.method == 'POST':
        form1 = EventForm(request.POST)
        if form1.is_valid():
            user1 = request.session["name"]
            user = UserData.objects.get(first_name=user1)
            day = request.POST['Day']
            start = request.POST['start_time'] 
            end = request.POST['end_time']
            Tittle = request.POST['Tittle']
            Description = request.POST["Description"]
            event1 = Event(Day=day,start_time=start,end_time=end,Tittle =Tittle,Description = Description,User1=user)
            event1.save()
            return HttpResponseRedirect(reverse('LES1:login'))
        else:
            return HttpResponseRedirect(reverse('LES1:login'))
def event_details(request,event_id):
    e = Event.objects.get(pk=event_id)
    return render(request,'event.html',{"event":e})



def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month
def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

# @Helper Method to  login_users
def calendar1(request,name):
      d = get_date(request.GET.get('month', None))
      prevmonth = prev_month(d)
      nextmonth = next_month(d)
      c = Calendar(d.year, d.month)
      html_cal = c.formatmonth(withyear=True,user=name)
      return [html_cal, prevmonth, nextmonth]


def login_users(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        form1 = EventForm()
        if form.is_valid():
            try:
                value = UserData.objects.get(email_id = request.POST['email_id'],password = request.POST['password'])
                user1 = value.first_name
                context = {
                    "user1":user1,
                    "form":form1,
                }
            except UserData.DoesNotExist:
                return render(request, 'LES1/login.html',{'form' : form, 'message':'Invalid Credentials'})
            request.session["name"] = user1
            value = calendar1(request,user1)
            html_cal = mark_safe(value[0])
            return render(request,'base1.html',{"user1":user1,"form":form1,'calendar':html_cal,'prev_month':value[1],'next_month':value[2]})
        else:
            return render(request,'LES1/login.html',{'form':form})
    else:
        form1 = UserForm()
        form2 = EventForm()
        if "name" in request.session:
            user1 =  request.session["name"]
            value = calendar1(request,user1)
            html_cal = mark_safe(value[0])
            return render(request,'base1.html',{"user1":user1,"form":form2,'calendar':html_cal,'prev_month':value[1],'next_month':value[2]})
        return render(request,'LES1/login.html',{'form':form1})

def register_users(request):
    form2 = EventForm()
    form1 = RegisterForm()
    if request.method == 'POST':
        user_details  = RegisterForm(request.POST)
        if user_details.is_valid():
            user_details.save()
            return  render(request,'LES1/login.html',{'form':form1})
        else:
             return render(request,'LES1/Registration.html',{'form':user_details})
    else:
        if "name" in request.session:
            user1 =  request.session["name"]
            value = calendar1(request,user1)
            html_cal = mark_safe(value[0])
            return render(request,'base1.html',{"user1":user1,"form":form2,'calendar':html_cal,'prev_month':value[1],'next_month':value[2]})
        return render(request,'LES1/Registration.html',{'form':form1})

def logout_users(request):
    print("Hi Iam Logout")
    if "name" in request.session:
        del request.session["name"]
    return render(request,'LES1/introduction.html')



def introduction_users(request):
    form2 = EventForm()
    if "name" in request.session:
        user1 =  request.session["name"]
        value = calendar1(request,user1)
        html_cal = mark_safe(value[0])
        return render(request,'base1.html',{"user1":user1,"form":form2,'calendar':html_cal,'prev_month':value[1],'next_month':value[2]})  
    return render(request,'LES1/introduction.html')

class EventEdit(generic.UpdateView):
    model = Event
    fields = ["Day", "start_time", "end_time","Tittle","Description"]
    template_name = "event1.html"


# discussions

def home(request):
    forums=forum.objects.all().order_by('-date_created')[:5]
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())
    # discussions.reverse()
    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request,'home.html',context)

def addInForum(request):
    form = CreateInForum()
    if request.method == 'POST':
        form = CreateInForum(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/LES1/home')
    context ={'form':form}
    return render(request,'addInForum.html',context)

def addInDiscussion(request):
    form = CreateInDiscussion()
    if request.method == 'POST':
        form = CreateInDiscussion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/LES1/home')
    context ={'form':form}
    return render(request,'addInDiscussion.html',context)
