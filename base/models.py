from django.db import models
from django.contrib.auth.models import User


PRIORITY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    )
    

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username')
    subject = models.CharField(max_length=50)
    notes = models.CharField(max_length=300)
    assigned_to = models.CharField(max_length=50)
    priority = models.CharField( choices = PRIORITY_CHOICES, max_length=50)
    is_completed = models.BooleanField(default=False)
    due_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    created = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __str__(self):
        return self.subject

