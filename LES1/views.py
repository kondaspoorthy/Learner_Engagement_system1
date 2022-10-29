from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
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
                user1 = value.first_name
                context = {
                    "user1":user1
                }
            except UserData.DoesNotExist:
                return render(request, 'LES1/login.html',{'form' : form, 'message':'Invalid Credentials'})
            request.session["name"] = user1
            return render(request,'base1.html',context)
        else:
            return render(request,'LES1/login.html',{'form':form})
    else:
        form1 = UserForm()
        if "name" in request.session:
            return render(request,'base1.html')
        return render(request,'LES1/login.html',{'form':form1})

def register_users(request):
    form1 = UserForm()
    context = {
                'form':form1,
        }
    if request.method == 'POST':
        user_details  = RegisterForm(request.POST)
        if user_details.is_valid():
            user_details.save()
            return  render(request,'LES1/login.html',{'form':form1})
        else:
             return render(request,'LES1/Registration.html',{'form':user_details})
    else:
        if "name" in request.session:
            return render(request,'base1.html')
        form1 = RegisterForm()
        context = {
                'form':form1,
        }
        return render(request,'LES1/Registration.html',context)

def logout_users(request):
    print("Hi Iam Logout")
    if "name" in request.session:
        del request.session["name"]
    return render(request,'LES1/introduction.html')



def introduction_users(request):
    if "name" in request.session:
            return render(request,'base1.html')  
    return render(request,'LES1/introduction.html')


