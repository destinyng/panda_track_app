from django.db import models

class Panda(models.Model):
    name=models.CharField(max_length=255)
    age=models.IntegerField()
    sex=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


# Create your models here.
