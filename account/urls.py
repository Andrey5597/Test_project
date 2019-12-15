from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views import RigistrationView, UserDateView
app_name = 'account'

urlpatterns = [
    path('register', RigistrationView.as_view(), name='register'),
    path('login', jwt_views.TokenObtainPairView.as_view(), name='login'),
    path('token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('date_joined', UserDateView.as_view(), name='date_joined')
]
