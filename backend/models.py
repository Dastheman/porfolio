from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    # poster = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField()
    

    def __str__(self):
            return self.firstname
