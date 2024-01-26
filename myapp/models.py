from django.db import models

# Create your models here.
class Todoitem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)