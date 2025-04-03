

from django.db import models

class Tour(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.city}, {self.country}"
