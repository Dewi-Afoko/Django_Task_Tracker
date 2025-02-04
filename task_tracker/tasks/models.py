from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=30)
    description = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    date_due = models.DateField(null=True, blank=True)
    complete = models.BooleanField(default=False)
