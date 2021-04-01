from menu.models import Menu

# Django imports
from django.db import models
from django.utils import timezone


class Dish(models.Model):
    name = models.TextField(
        null=False,
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        null=False,
    )
    menu = models.ForeignKey(
    Menu,
    on_delete=models.CASCADE
    )
    
    class Meta:
        """Meta option."""
        get_latest_by = 'created_at'
        ordering = ['-created_at']

    def __str__(self):
        return self.name
