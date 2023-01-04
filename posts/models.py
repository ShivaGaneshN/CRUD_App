from django.db import models

# Create your models here.
class Details(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return self.name