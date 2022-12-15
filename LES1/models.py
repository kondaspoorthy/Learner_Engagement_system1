from django.db import models
from datetime import date, time, datetime
from django.urls import reverse
from django.core.exceptions import ValidationError

# Create your models here.
class UserData(models.Model):
    first_name = models.CharField(max_length = 12)
    last_name = models.CharField(max_length= 12)
    date_of_birth = models.DateField()
    email_id = models.EmailField()
    password = models.CharField(max_length=12)
    re_password = models.CharField(max_length = 12)

    def __str__(self):
        return f'{self.first_name}, { self.email_id}, {self.password}'
class Event(models.Model):
    Day = models.DateField(default=date.today())
    start_time = models.TimeField()
    end_time = models.TimeField()
    Tittle = models.CharField(max_length=30)
    Description = models.TextField(max_length=150)
    User1 = models.ForeignKey(UserData,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.Tittle}'
    @property
    def get_html_url(self):
        url = reverse('LES1:event-detail', args=(self.id,))
        return f'<a href="{url}"> {self.Tittle} </a>'
    def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
        overlap = False
        if new_start == fixed_end or new_end == fixed_start:    #edge case
            overlap = False
        elif (new_start >= fixed_start and new_start <= fixed_end) or (new_end >= fixed_start and new_end <= fixed_end): #innner limits
            overlap = True
        elif new_start <= fixed_start and new_end >= fixed_end: #outter limits
            overlap = True
        return overlap
    def previous_events(self,Day1,time1):
        if Day1 < date.today():
            return True
        # elif time1 < datetime.now().time():
        #     return True
    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError('Ending times must after starting times')
        events = Event.objects.filter(Day=self.Day)
        if events.exists():
            for event in events:
                if self.check_overlap(event.start_time, event.end_time, self.start_time, self.end_time):
                    raise ValidationError(
                        'There is an overlap with another event')
        if  self.previous_events(self.Day,self.start_time):
            raise ValidationError("You can't add events for previous days")
