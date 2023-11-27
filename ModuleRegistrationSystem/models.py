from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Course (models.Model):
    name = models.CharField(max_length = 100)

class Module(models.Model):
    name = models.CharField(max_length = 100)
    code = models.PositiveIntegerField()
    credit = models.PositiveIntegerField()
    category = models.CharField(max_length = 100, choices = [('Face-to-Face', 'Face-to-Face'), ('Online', 'Online')])
    description = models.TextField()
    availability = models.CharField(max_length = 100 , choices = [('Open', 'Open'), ('Closed', 'Closed')])
    course = models.ForeignKey(Course, null = True, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.name} , Module Code: {self.code}'

# Create your models here.
