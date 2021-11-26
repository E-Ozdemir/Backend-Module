from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE,blank=True, null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"