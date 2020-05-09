from django.db import models
from datetime import datetime

# Create your models here.

class TurtleBrand(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=20)
    seed_word = models.CharField(max_length=50)

class turtle_calls(models.Model):
    request_id = models.IntegerField(unique=True, primary_key=True)
    request_url = models.CharField(max_length=200)
    request_date = models.DateField(auto_now=True)
    
class TurtleBrandSignup(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    source = models.CharField(max_length=10)
    signup_date = models.DateField(default=datetime.now)
