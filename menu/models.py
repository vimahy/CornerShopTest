import uuid
#Django imports
from django.utils import timezone
from django.db import models



class Menu(models.Model):
    unique_id = models.UUIDField(
        default=uuid.uuid4, 
        editable=False, 
        unique=True
    )
    date = models.DateTimeField(
        default=timezone.now,
        null=False,
    )
    name = models.TextField(
        max_length=50,
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        null=False,
        help_text='Date time on which the object was created.'
    )
    
    class Meta:
        get_latest_by = 'created_at'
        ordering = ['-created_at']


    def __str__(self):
        return self.name

