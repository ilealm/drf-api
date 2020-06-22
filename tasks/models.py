from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Task(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now=True)
    event_date = models.DateTimeField(auto_now=True)
    message = models.TextField()

    def __str__(self):
        return self.title