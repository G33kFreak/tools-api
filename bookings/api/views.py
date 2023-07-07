from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotAuthenticated

from bookings.models import Booking
from tools.models import Tool
from bookings.api.serializers import BookingSerializer, BookingCreateSerializer
from bookings.exceptions import NoAvailableTools

class BookingListAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'post']
    
    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BookingCreateSerializer
        else:
            return BookingSerializer
        
    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            request.data['user'] = request.user.pk
            selected_tools = Tool.objects.filter(pk__in=request.data['tools'])
            for tool in selected_tools:
                if tool.available <= 0:
                    raise NoAvailableTools(detail=f'No available tools left for ID: {tool.id}')
            return super().create(request, *args, **kwargs)
        else:
            raise NotAuthenticated()