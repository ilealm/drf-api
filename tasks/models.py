from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Task(models.Model):
    PRIORITY_CHOICES = (
        ('1', 'Urgent'),
        ('2', 'Important'),
        ('3', 'Low'),
        ('4', 'Medium'),
        ('5', 'When possible'),
    )
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now=True)
    event_date = models.DateTimeField()
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='Medium')      
    completed = models.BooleanField(default=False)
    message = models.TextField()

    REQUIRED_FIELDS = [ 'title', 'event_date' ]

    class Meta:
        ordering = ['event_date']

    def __str__(self):
        return self.title