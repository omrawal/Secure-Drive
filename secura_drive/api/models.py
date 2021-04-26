from django.db import models
import uuid
from main.models import Profile
from django.conf import settings


# Create your models here.
class File(models.Model):
    fid = models.CharField(
        primary_key=True, max_length=200, default=uuid.uuid4)
    file_data = models.TextField()
    file_name = models.CharField(max_length=200)
    file_size = models.IntegerField()
    file_content_type = models.CharField(max_length=100)
    owner_id = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "File"
        verbose_name_plural = "Files"

    def __str__(self):
        return self.file_name
