from django.shortcuts import render

def home(request):
    return render(request, 'ModuleRegistrationSystem/home.html', {'title': 'Home'})

def about(request):
    return render(request, 'ModuleRegistrationSystem/about.html', {'title': 'About Us'})

def contact(request):
    return render(request, 'ModuleRegistrationSystem/contact.html', {'title': 'Contact Us'})

def module(request):
    return render(request, 'ModuleRegistrationSystem/modulelist.html', {'title': 'List of Module Pages'})

# Create your views here.
