from django.db import models
from datetime import datetime

# Create your models here.
class Subject(models.Model):
    title = models.CharField(max_length=100, blank=False)
    content = models.TextField(blank=False)
    published = models.DateTimeField("Date published.", default=datetime.now())

    def __str__(self):
        return self.title
