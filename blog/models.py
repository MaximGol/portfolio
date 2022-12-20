from django.db import models
from django.db import models

class Blog_Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=250)
    date = models.DateField()

# Create your models here.
