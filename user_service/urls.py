from tokenize import Token
from django.urls import path, include
from .views import UserProfile, UserRegister, UserLogin
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('signup/', UserRegister.as_view(), name='user-registre'),
    path('profile/', UserProfile.as_view(), name='user-profile'),
    
    ]
