from django.db import models
from django.db import models

class Blog_Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2500)
    date = models.DateField()

# Create your models here.
    def __str__(self):
            return self.title