from django.contrib import admin
from .models import UserData, Event

# Register your models here.
admin.site.register(UserData)
admin.site.register(Event)
