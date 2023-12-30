from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test, login_required
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
    paginate_by = 3
    model = Module
    template_name = 'ModuleRegistrationSystem/modulelist.html'
    context_object_name = 'module'
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
    
@login_required
def register_module(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    user_groups = request.user.groups.all()

    existing_registration = Registration.objects.filter(student=request.user, module=module).exists()

    if existing_registration:
        messages.info(request, 'You have already registered for this module')
        return redirect('ModuleRegistrationSystem:module-detail', pk=module_id)

    module_courses = module.courses.all()
    if not any(group in user_groups for group in module_courses):
        messages.error(request, 'It is not possible to register for modules that are outside of your course')
        return redirect('ModuleRegistrationSystem:module-detail', pk=module_id)

    if request.method == 'POST':
        registration = Registration(student=request.user, module=module)
        registration.save()


        messages.success(request, 'You are now registered to this Module')

    return redirect('ModuleRegistrationSystem:module-detail', pk=module_id)

@login_required
def unregister_module(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    user = request.user

    existing_registration = Registration.objects.filter(student=user, module=module).exists()

    if not existing_registration:
        messages.info(request, 'You have not registered for this module')
        return redirect('ModuleRegistrationSystem:module-detail', pk=module_id)

    if request.method == 'POST':
        registration = Registration.objects.filter(student=request.user, module=module).first()

        if registration:
            registration.delete()
            messages.success(request, 'You are now unregistered from this Module')
        else:
            messages.error(request, "Error: Registration not found.")


    return redirect('ModuleRegistrationSystem:module-detail', pk=module_id)



# Create your views here.
