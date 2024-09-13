from django.db import models

class UserModel(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
