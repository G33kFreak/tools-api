from django.urls import path

from bookings.api.views import BookingListAPIView


urlpatterns = [
    path('list', BookingListAPIView.as_view())
]