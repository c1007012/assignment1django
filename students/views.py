from django.shortcuts import render, redirect
from django.contrib.auth.views import PasswordResetView
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, CustomPasswordResetForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.groups.add(form.cleaned_data.get('course'))
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! Now you can login!')
            return redirect('login')

        else:
            messages.warning(request, 'Unable to create account!')
        return redirect('ModuleRegistrationSystem:home')
    else:
        form = UserRegisterForm()
        return render(request, 'students/register.html', {'form': form , 'title': 'Student Registration'})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
        if u_form.is_valid and p_form.is_valid:
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been successfully updated')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)
    context = {'u_form': u_form, 'p_form': p_form, 'title': 'Student Profile'}
    return render(request, 'students/profile.html', context)

class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    email_template_name = 'students/password_reset_email.html'
    subject_template_name = 'students/password_reset_subject.txt'
    template_name = 'students/password_reset.html'
    html_email_template_name = 'students/password_reset_email.html'

# Create your views here.
