from user.models import User
from dishes.models import Dish

# Django imports
from django.db import models
from django.utils import timezone


class Order(models.Model):
    comment = models.TextField(
        null=True,
    )
    
    created_at = models.DateTimeField(
    default=timezone.now,
    null=False,
    )
    dish = models.ForeignKey(
    Dish,
    on_delete=models.CASCADE
    )
    
    class Meta:
        get_latest_by = 'created_at'
        ordering = ['-created_at']

    def __str__(self):
        return self.name
