from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Course(models.Model):
    name = models.CharField(default="", max_length=100)
    description = models.CharField(default="", max_length=300)
    fees = models.IntegerField(default=0)
    teacher = models.CharField(default="", max_length=100)
    timings = models.CharField(default="", max_length=20)
    
    def __str__(self):
        return self.name

class Founder(models.Model):
    name = models.CharField(max_length=100)
    rank = models.CharField(max_length=100, default="")
    specialties = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f'{self.user} - {self.rating}'