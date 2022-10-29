from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from LES1.forms import RegisterForm, UserForm
from .models import UserData
from django.http import HttpResponse

# Create your views here.
def login_users(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                value = UserData.objects.get(email_id = request.POST['email_id'],password = request.POST['password'])
            except UserData.DoesNotExist:
                return render(request, 'LES1/login.html',{'form' : form, 'message':'Invalid Credentials'})
            return HttpResponse("You are sucessfully logged in")
        else:
            return render(request,'LES1/login.html',{'form':form})
    else:
        form1 = UserForm()
        return render(request,'LES1/login.html',{'form':form1})

def register_users(request):
    if request.method == 'POST':
        user_details  = RegisterForm(request.POST)
        if user_details.is_valid():
            user_details.save()
            return HttpResponse("Your Data is succesfully submitted")
        else:
             return render(request,'LES1/Registration.html',{'form':user_details})
    else:
        form1 = RegisterForm()
        context = {
                'form':form1,
        }
        return render(request,'LES1/Registration.html',context)
def sampleview(request):
    return HttpResponse('you are looking at me')
def introduction_users(request):
    return render(request,'LES1/introduction.html')

