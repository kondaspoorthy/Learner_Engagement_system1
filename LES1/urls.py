from django.urls import path
from . import views
# from LES1.views import *
app_name = 'LES1'
urlpatterns = [
    path('Register/',views.register_users, name='detail'),
    path('Login/', views.login_users, name = 'login'),
    path('Logout/',views.logout_users, name ='logout'),
    path('Introduction/',views.introduction_users,name='Introduction'),
    path('Eventcreation/',views.create_events,name="events"),
    path("event/details/<int:event_id>", views.event_details, name="event-detail"),
    path('home/',views.home,name='home'),
    path('addInForum/',views.addInForum,name='addInForum'),
    path('addInDiscussion/',views.addInDiscussion,name='addInDiscussion'),

]
