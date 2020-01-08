# -*- encoding: utf-8 -*-
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib import messages


def LogIn(request, username, password):
	user = authenticate(username = username, password = password)
	if user is not None:
		if user.is_active:
			login(request, user)
	else:
		messages.warning(request, 'Usuario o contraseña incorrectos!')