from django.urls import path
from . import views
app_name = 'LES1'
urlpatterns = [
    path('Register/',views.register_users, name='detail'),
    path('Login/', views.login_users, name = 'login'),
    path('Logout/',views.logout_users, name ='logout'),
]