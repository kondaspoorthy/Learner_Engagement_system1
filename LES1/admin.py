from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserData)
admin.site.register(Event)
admin.site.register(forum)
admin.site.register(Discussion)