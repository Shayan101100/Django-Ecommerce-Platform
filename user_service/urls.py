
from django.urls import path
from .views import UserProfile, UserRegister, UserLogin



urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('signup/', UserRegister.as_view(), name='user-registre'),
    path('profile/', UserProfile.as_view(), name='user-profile'),
    
    ]
