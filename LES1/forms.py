from socket import fromshare
from django.contrib.admin.widgets import AdminDateWidget
from datetime import date
from django.forms import ModelForm
from django import forms
import datetime
from django.db.models import Q
from .models import UserData,Event
from django.forms import ModelForm, TextInput, EmailInput,DateInput
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db.models import Q
from .models import *

def passwords_match(x,y):
    return x == y
class UserForm(forms.Form):
    email_id = forms.EmailField( widget = forms.EmailInput(attrs= {'class':'form-control'}))
    password = forms.CharField(max_length=12, widget = forms.PasswordInput(attrs ={'class' : 'form-control'}))
class EventForm(ModelForm):
    class Meta: 
        model = Event
        fields = ["Day","start_time","end_time","Tittle","Description"]
        widgets = {
            "Day":DateInput(attrs={
                'class': "form-control"
            }),
            'start_time': forms.TimeInput(attrs=
            {'type': 'time',
            'class': "form-control"}),
            
            'end_time': forms.TimeInput(attrs=
            {'type': 'time',
            'class': "form-control"}),
            
            'Tittle': TextInput(attrs={
               
                'class': "form-control",
                
            }),
             'Description': TextInput(attrs={   
                'class': "form-control",       
            }),
        }
class RegisterForm(ModelForm):
    class Meta:
        model = UserData
        fields = '__all__'
        error_messages = {
            'first_name': {
                'required': _("Please enter first name")
            },
            'last_name': {
                'required': _("Please enter last name")
            },
             'email_id': {
                'required': _("Please enter email")
            },
             'password': {
                'required': _("Please enter password")
            },
             'date_of_birth': {
                'required': _("Please enter D.O.B")
            },
             're_password': {
                'required': _("Please enter Again")
            },
        }
        widgets = {
            'first_name': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'First_Name'
                }),
            'last_name': TextInput(attrs={
                
                'class': "form-control",
                'placeholder': 'Last_Name'
                }),
                'date_of_birth': DateInput(attrs={
               
                'class': "form-control",
                'placeholder': 'yyyy-mm-d'
            }),
            'password': forms.PasswordInput(attrs={
                'class': "form-control",
                'placeholder': 'password'
            }),
            'email_id': EmailInput(attrs={
                
                'class': "form-control",
                'placeholder': 'Email'
            }),
            're_password': forms.PasswordInput(attrs={
                
                'class': "form-control",
                'placeholder': 'Enter Again'
                }),
        }
    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data['date_of_birth']
        if datetime.datetime.now().year - date_of_birth.year > 20:
            raise forms.ValidationError("Too old to Register")
        return date_of_birth
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password")
        password2 = cleaned_data.get("re_password")
        if not passwords_match(password1,password2):
            raise forms.ValidationError("Password's dont match")
        firstname = cleaned_data.get("first_name")
        lastname = cleaned_data.get("last_name")
        dateofbirth= cleaned_data.get("email_id")
        email = cleaned_data.get("date_of_birth") 
        if UserData.objects.filter(Q(first_name=firstname)|Q(last_name=lastname)|Q(email_id=email)|Q(password=password1)):
            raise forms.ValidationError("User Already Registered") 
        return cleaned_data
    
# forms for discussion page


class CreateInForum(ModelForm):
    class Meta:
        model= forum
        fields = "__all__"


class CreateInDiscussion(ModelForm):
    class Meta:
        model= Discussion
        fields = "__all__"
        
       
       
         



   

    