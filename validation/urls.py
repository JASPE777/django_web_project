from django.urls import path
from .views import V_register, close_acount, login

urlpatterns = [
    
    path('', V_register.as_view(), name='validation'),

    path('close_acount', close_acount, name='close_acount'),

    path('login', login, name='login'),
    
]