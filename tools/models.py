from django.db import models


class Tool(models.Model):
    label = models.CharField(max_length=80)
    description = models.TextField()
    image_url = models.ImageField(upload_to='tools', blank=True, null=True)
    available_count = models.IntegerField()

    def __str__(self) -> str:
        return self.label
