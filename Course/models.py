from django.db import models
from django.contrib.auth.models import Group
from django.urls import reverse

class Module(models.Model):
    name = models.CharField(max_length = 100)
    code = models.PositiveIntegerField()
    credit = models.PositiveIntegerField()
    category = models.CharField(max_length = 100, choices = [('Face-to-Face', 'Face-to-Face'), ('Online', 'Online')])
    description = models.TextField()
    availability = models.CharField(max_length = 100 , choices = [('Open', 'Open'), ('Closed', 'Closed')])

    def __str__(self):
        return f'{self.name}'
    def get_absolute_url(self):
        return reverse('ModuleRegistrationSystem:module-detail', kwargs = {'pk': self.pk})
    
class Course (models.Model):
    name = models.CharField(max_length = 100)
    credit = models.PositiveIntegerField()
    description = models.TextField(default='No description provided.')
    modules = models.ManyToManyField(Module)
    
    def __str__(self):
        return f'{self.name}'
    def get_absolute_url(self):
        return reverse('ModuleRegistrationSystem:course-detail', kwargs = {'pk': self.pk})
    
class CourseGroup(Group):
    description = models.TextField(blank=True)
# Create your models here.
