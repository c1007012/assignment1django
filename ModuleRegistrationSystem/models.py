from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group, Permission
from django.urls import reverse

class Module(models.Model):
    name = models.CharField(max_length = 100)
    code = models.PositiveIntegerField()
    credit = models.PositiveIntegerField()
    category = models.CharField(max_length = 100, choices = [('Face-to-Face', 'Face-to-Face'), ('Online', 'Online')])
    description = models.TextField()
    availability = models.CharField(max_length = 100 , choices = [('Open', 'Open'), ('Closed', 'Closed')])
    courses = models.ManyToManyField(Group)
    
    def __str__(self):
        return f'{self.name}'
    def get_absolute_url(self):
        return reverse('ModuleRegistrationSystem:module-detail', kwargs = {'pk': self.pk})
    
class Registration(models.Model):
    student = models.ForeignKey(User, related_name = 'registrations', on_delete = models.CASCADE)
    module = models.ForeignKey(Module, related_name = 'registrations', on_delete = models.CASCADE)
    date_of_registration = models.DateField(default = timezone.now)
