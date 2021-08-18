from django.db import models


# Create your models here.
class Subject(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published = models.DateTimeField("Date published.")

    def __str__(self):
        return self.title
