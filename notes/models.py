from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Note(models.Model):
    NOTE_TYPES = [
        ('text', 'Text'),
        ('audio', 'Audio'),
        ('video', 'Video'),
    ]
    
    title = models.CharField(max_length=255)
    content_type = models.CharField(max_length=10, choices=NOTE_TYPES)
    content = models.FileField(upload_to='notes/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    shared_with = models.ManyToManyField(User, related_name='shared_notes')

    def __str__(self):
        return self.title