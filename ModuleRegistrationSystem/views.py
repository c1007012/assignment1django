from django.shortcuts import render
from .models import Module


def home(request):
    return render(request, 'ModuleRegistrationSystem/home.html', {'title': 'Home'})

def about(request):
    return render(request, 'ModuleRegistrationSystem/about.html', {'title': 'About Us'})

def contact(request):
    return render(request, 'ModuleRegistrationSystem/contact.html', {'title': 'Contact Us'})

def module(request):
    daily_module = {'module': Module.objects.all(), 'title': 'Modules Registered'}
    return render(request, 'ModuleRegistrationSystem/modulelist.html', daily_module)

# Create your views here.
