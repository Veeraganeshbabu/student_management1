from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Details(models.Model):
    StudentId = models.CharField(max_length=200, null=True)
    StudentName = models.CharField(max_length=50, null=True)
    BatchName = models.CharField(max_length=50, null=True)

    Graduation = models.CharField(max_length=100, null=True)
    YearOfPass = models.IntegerField(null=True)
    EMail = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.StudentName



