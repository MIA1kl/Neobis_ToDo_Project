from django.db import models
from django.utils import timezone


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50, default="", blank=True)
    description = models.CharField(max_length=200,  default="", blank=True)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
    date = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
    is_done = models.BooleanField(default=False)
    
    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title