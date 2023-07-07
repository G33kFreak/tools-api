from rest_framework import serializers

from bookings.models import Booking
from tools.api.serializers import ToolSerializer

class BookingSerializer(serializers.ModelSerializer):
    tools = ToolSerializer(many=True)
    class Meta:
        model = Booking
        fields = [
            'id',
            'created_at',
            'is_verified',
            'tools',
            'sum_price',
        ]