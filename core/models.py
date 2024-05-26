from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_seller = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

class Property(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    place = models.CharField(max_length=255)
    area = models.FloatField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties')
    hospitals_nearby = models.CharField(max_length=255, blank=True, null=True)
    colleges_nearby = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
