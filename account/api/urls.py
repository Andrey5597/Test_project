from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views import registration_view, date_of_user_registration_view
app_name = 'account'

urlpatterns = [
    path('register', registration_view, name='register'),
    path('login', jwt_views.TokenObtainPairView.as_view(), name='login'),
    path('token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('date_joined', date_of_user_registration_view, name='date_joined')
]
