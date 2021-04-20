from django.db import models
import uuid
# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=200)
    uid = models.CharField(
        primary_key=True, max_length=200, default=uuid.uuid4)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.name



