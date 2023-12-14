from django.db import models

# Create your models here.
class Facultet(models.Model):
    name = models.CharField(unique=True)

    def __str__(self):
        return self.name