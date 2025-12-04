from django.db import models


# Create your models here.
class Event(models.Model):
    # This is equivalent to your Mongoose Schema or SQL Table definition
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=200)
    # We use JSONField because you are using Postgres!
    categories = models.JSONField(default=list)

    def __str__(self):
        return self.title
