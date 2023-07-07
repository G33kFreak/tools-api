from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from bookings.models import Booking
from bookings.api.serializers import BookingSerializer

class BookingListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BookingSerializer
    http_method_names = ['get']
    
    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)