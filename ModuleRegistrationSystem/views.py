from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from .models import Module, Registration
from django.views.generic import ListView, DetailView, FormView
from .forms import ContactForm
from django.core.mail import send_mail
from django. contrib import messages
from django.contrib.auth.models import Group



def home(request):
    daily_course = {'course': Group.objects.all(), 'title' : 'Course List'}
    return render(request, 'ModuleRegistrationSystem/home.html', daily_course)

def about(request):
    return render(request, 'ModuleRegistrationSystem/about.html', {'title': 'About Us'})


def course(request):
    daily_course = {'course': Group.objects.all(), 'title': 'Course List'}
    return render(request, 'ModuleRegistrationSystem/coursepage.html', daily_course)

def modulelist(request):
    daily_module = {'module': Module.objects.all(), 'title': 'Modules Registered'}
    return render(request, 'ModuleRegistrationSystem/modulelist.html', daily_module)


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'ModuleRegistrationSystem/contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactFormView, self).get_context_data(**kwargs)
        context.update({'title': 'Contact Us'})
        return context

    def form_valid(self, form):
        form.send_mail()
        messages.success(self.request, 'Successfully sent the enquiry')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, 'Unable to send the enquiry')
        return super().form_invalid(form)
    
    def get_success_url(self):
        return self.request.path

class PostListView(ListView):
    model = Module
    template_name = 'ModuleRegistrationSystem/modulelist.html'
    context_object_name = 'models'
    ordering = ['-name']

    def get_context_data(self, **kwargs: any):
        context = super().get_context_data(**kwargs)
        course = Group.objects.get(id = self.kwargs.get('fk'))
        context.update({'course': course, 'modules': course.module_set.all()})

        return context

class PostDetailView(DetailView):
    model = Module

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        registrations = Registration.objects.filter(module = self.object)
        context.update({'title': 'Contact Us', 'registrations': registrations})
        
        return context


# Create your views here.
