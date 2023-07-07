import uuid

from django.db import models

from users.models import User
from tools.models import Tool

class Booking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='orders',
        null=True,
    )
    tools = models.ManyToManyField(Tool)
    is_verified = models.BooleanField(default=False)

    @property
    def sum_price(self):
        sum_price = 0
        for tool in self.tools.all():
            sum_price += tool.price
        return sum_price

    def __str__(self) -> str:
        return f"{self.id} - {self.user.first_name} {self.user.last_name} - {self.created_at.strftime('%d.%m.%Y, %H:%M:%S')}"
    
