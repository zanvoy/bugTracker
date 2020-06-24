from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class SomeUser(AbstractUser):
   placeholder = models.CharField(max_length=42)

class Ticket(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    author = models.ForeignKey(SomeUser, on_delete=models.CASCADE, related_name='author')
    assigned = models.ForeignKey(SomeUser, on_delete=models.CASCADE, related_name='assigned',blank=True, null=True, default=None)
    compleated = models.ForeignKey(SomeUser, on_delete=models.CASCADE, related_name='compleated',blank=True, null=True,default=None)
    status_choices = [
        ('New','New'),
        ('In Progress','In Progress'),
        ('Done','Done'),
        ('Invalid','Invalid')
    ] 
    status = models.CharField(
        max_length=12,
        choices=status_choices,
        default='New'
    )

    def __str__(self):
        return self.title

