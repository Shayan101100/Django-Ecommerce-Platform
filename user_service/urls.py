from tokenize import Token
from django.urls import path
from .views import UserProfile, UserRegister, UserLogin
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('signup/', UserRegister.as_view(), name='user-registre'),
    path('login/', UserLogin.as_view(), name='user-login'),
    path('profile/', UserProfile.as_view(), name='user-profile'),
    
    ]
