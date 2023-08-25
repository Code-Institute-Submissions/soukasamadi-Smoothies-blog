from django.db import models
from cloudinary.models import CloudinaryField
from django.urls import reverse


class Challenge(models.Model):
    """
    Model for Challenge
    """
    name = models.CharField(max_length=20)
    picture = CloudinaryField('image')
    goal = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)
    link = models.URLField(blank=True)
    review = models.TextField(max_length=200)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Sets absolute URL"""
        return reverse('challenge')
