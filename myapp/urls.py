from django.urls import path
from . import views
from .views import RegisterView, VerifyEmail
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    # path('', views.home, name='home'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/<str:uidb64>/<str:token>/', VerifyEmail.as_view(), name='verify_email'),
]
