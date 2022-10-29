from django.urls import path
from . import views
app_name = 'LES1'
urlpatterns = [
    path('Register/',views.register_users, name='register-form'),
    path('Login/', views.login_users, name = 'login'),
    path('Introduction/',views.introduction_users,name = 'introduction'),
    path('Logout/',views.logout_users, name ='logout'),
]
    