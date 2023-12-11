from django.shortcuts import render
from .models import Module, Course
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    return render(request, 'ModuleRegistrationSystem/home.html', {'title': 'Home'})

def about(request):
    return render(request, 'ModuleRegistrationSystem/about.html', {'title': 'About Us'})

def contact(request):
    return render(request, 'ModuleRegistrationSystem/contact.html', {'title': 'Contact Us'})

def course(request):
    daily_course = {'course': Course.objects.all(), 'title': 'Course List'}
    return render(request, 'ModuleRegistrationSystem/coursepage.html', daily_course)

def modulelist(request):
    daily_module = {'module': Module.objects.all(), 'title': 'Modules Registered'}
    return render(request, 'ModuleRegistrationSystem/modulelist.html', daily_module)

class PostListView(ListView):
    model = Module
    template_name = 'ModuleRegistrationSystem/modulelist.html'
    context_object_name = 'modules'
    ordering = ['-name']

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Module
    fields = ['name', 'code', 'credit', 'category', 'description', 'availability']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Module
    fields = ['name', 'code', 'credit', 'category', 'description', 'availability']

class PostDetailView(DetailView):
    model = Module


# Create your views here.
