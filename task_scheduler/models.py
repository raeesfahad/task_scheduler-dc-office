from django.db import models


PRIORITY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    )
    

class Task(models.Model):
    subject = models.CharField(max_length=50)
    notes = models.CharField(max_length=300)
    assigned_to = models.CharField(max_length=50)
    priority = models.CharField( choices = PRIORITY_CHOICES, max_length=50)
    due_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    created = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
