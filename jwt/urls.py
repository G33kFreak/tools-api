from django.urls import path
from jwt.api.views import ObtainTokensAPIView, RefreshTokensAPIView


urlpatterns = [
    path('', ObtainTokensAPIView.as_view()),
    path('refresh/', RefreshTokensAPIView.as_view()),
]