from django.db import models

# Create your models here.

class Task(models.Model):
    task_name = models.CharField(max_length=200)
    task_desc = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now=True)  # auto_now to get the current time
    completed = models.BooleanField(default=False)
    image = models.ImageField(upload_to= 'Images/', default='Images/None/No0img.jpg')

# We need a serializer to take the model and convert it into a json file. Every REST API needs a serializer
# So that json can be presented to a user to request from API

