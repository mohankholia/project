from django.db import models

# Create your models here.


class Signup(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120, primary_key=True)
    password = models.CharField(max_length=16)
    mobile = models.BigIntegerField()

    def __str__(self):
        return self.name
