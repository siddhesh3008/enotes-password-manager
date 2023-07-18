from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Signup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ContactNo = models.CharField(max_length=10, null=True)
    About = models.CharField(max_length=450, null=True)
    Role = models.CharField(max_length=150, null=True)
    RegDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name

class Notes(models.Model):
    signup = models.ForeignKey(Signup, on_delete=models.CASCADE)
    Title = models.CharField(max_length=200, null=True)
    Content = models.CharField(max_length=450, null=True)
    CreationDate = models.DateTimeField(auto_now_add=True)
    UpdationDate = models.DateField(null=True)

    def __str__(self):
        return self.Title

class Passwords(models.Model):
    signup = models.ForeignKey(Signup, on_delete=models.CASCADE)
    Title = models.CharField(max_length=200, null=True)
    Content = models.CharField(max_length=450, null=True)
    Content2 = models.CharField(max_length=550, null=True)
    CreationDate = models.DateTimeField(auto_now_add=True)
    UpdationDate = models.DateField(null=True)

    def __str__(self):
        return self.Title

