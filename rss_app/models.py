from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Link(models.Model):
    name = models.CharField(max_length=30)
    url = models.CharField(max_length=264)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name