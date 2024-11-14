# ref. https://infinitt.tistory.com/65

from django.db import models

# Create your models here.
class User(models.Model):
    user_handle = models.CharField(max_length=15)
    user_name = models.CharField(max_length=20)
    user_pwd = models.CharField(max_length=20)
    user_intro = models.CharField(max_length=100)

