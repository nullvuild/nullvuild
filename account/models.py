# ref. https://infinitt.tistory.com/65

from django.db import models

# Create your models here.
class User(models.Model):
    userid = models.CharField(max_length=15)
    name = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)
    introduction = models.CharField(max_length=100)

