from django.db import models
from .file_crypto import generateKey
from django.contrib.auth.models import User
import uuid

class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    picture = models.ImageField(upload_to='./uploads/')
    cryptoKey = models.CharField(default=generateKey, max_length=200)
    
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return self.user.username
