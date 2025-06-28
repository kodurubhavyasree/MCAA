from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.contrib import messages
from django import forms
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.models import User

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        uname = request.POST['username']
        email = request.POST['email']
        pwd = request.POST['password']

        if User.objects.filter(username=uname).exists():
            messages.error(request, 'Username already exists.')
            return redirect('register')

        User.objects.create(username=uname, email=email, password=pwd)
        messages.success(request, 'Registration successful.')
        return redirect('login')
    
    return render(request, 'register.html')


def user_login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']
        try:
            user = User.objects.get(username=uname, password=pwd)
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            return redirect('home')
        except User.DoesNotExist:
            messages.error(request, 'Invalid credentials.')
            return redirect('login')
    return render(request, 'login.html')


def user_logout(request):
    request.session.flush()
    return redirect('login')

# Create your views here.

def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def student_details(request):
    return render(request,'student_details.html')

class MyPasswordResetForm(SetPasswordForm):
    new_password1=forms.CharField(label="New Password",strip=False,
                                  widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),)
    
new_password2=forms.CharField(label="Confirm New Password",strip=False,
                                  widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),)



# Create your views here.
