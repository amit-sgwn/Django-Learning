from django.db import models

# Create your models here.

class Rooms(models.Model):
    code = models.CharField(max_length=8, default="", unique=True)
    