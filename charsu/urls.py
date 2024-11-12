"""
Definition of urls for charsu.
"""


from django.contrib import admin
from django.contrib.auth.views import LogoutView
from app import views
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('user_service.urls')),
    path('api/', include('product_service.urls')),
    path('api/', include('order_service.urls')),
    path('api/', include('payment_service.urls')),
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('api/token/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
        ]+urlpatterns
