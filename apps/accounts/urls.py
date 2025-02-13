from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'accounts'

urlpatterns = [
    path('retrieve-token', TokenObtainPairView.as_view(), name='retrieve_token'),
    path('refresh-token', TokenRefreshView.as_view(), name='token_refresh'),
]