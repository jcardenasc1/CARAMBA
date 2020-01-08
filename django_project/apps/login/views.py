# -*- encoding: utf-8 -*-
from django.shortcuts import render
from .forms import UserLoginForm, RegistroUserForm
from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.views.generic import CreateView
from .functions import LogIn
from apps.usuario.models import User
from django.contrib import messages

def LogOut(request):
    logout(request)
    return redirect(reverse('login'))

def userlogin(request):
    if request.method == "POST":
        if 'register_form' in request.POST:
            user_register = RegistroUserForm(request.POST)
            if user_register.is_valid():
                User.objects.create_user(
                    first_name=user_register.cleaned_data['first_name'].upper(),
                    last_name=user_register.cleaned_data['last_name'].upper(),
                    sex=user_register.cleaned_data['sex'],
                    section=user_register.cleaned_data['section'],
                    birthdate=user_register.cleaned_data['birthdate'],
                    username=user_register.cleaned_data['username'].lower(),
                    email=user_register.cleaned_data['email'],
                    password=user_register.cleaned_data['password'])

                LogIn(request, user_register.cleaned_data['username'].lower(), user_register.cleaned_data['password'])
                return redirect('start')
            else:
                messages.error(request, 'Todos los campos son obligatorios')
        else:
            user_register = RegistroUserForm()
        if 'login_form' in request.POST:
            login_form = UserLoginForm(request.POST)
            if login_form.is_valid():
                LogIn(request, login_form.cleaned_data['username'],
                    login_form.cleaned_data['password'])
                return redirect('start')
            else:
                messages.warning(request, 'Los campos son obligatorios')
        else:
            login_form = UserLoginForm()

    else:
        user_register = RegistroUserForm()
        login_form = UserLoginForm()

    return render(request, 'login/index.html',{'user_register': user_register,'login_form':login_form})

