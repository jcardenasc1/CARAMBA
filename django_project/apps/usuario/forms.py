# -*- encoding: utf-8 -*-
from django import forms
from .models import User


# class UserLoginForm(forms.Form):
#     username = forms.CharField(
#         max_length=50,
#         widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#
#     password = forms.CharField(max_length=50,
#                                widget=forms.TextInput(attrs={
#                                    'class': 'form-control', 'type': 'password', 'placeholder': 'Ingrese una contrasena',
#                                }))
#
#     def clean(self):
#         if not user.objects.filter(username=self.cleaned_data['username']):
#             self.add_error('username','El nombre de usuario no existe!')
#         else:
#             usuario = user.objects.get(username=self.cleaned_data['username'])
#             if not usuario.check_password(self.cleaned_data['password']):
#                 self.add_error('username','Contrasena es incorrecta')


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ('is_active','is_staff','username','is_superuser','groups','user_permissions','last_login')
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Nombres'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Apellidos'}),
            'email':forms.TextInput(attrs={'type':'email','class':'form-control','placeholder':'Escriba su correo electronico'}),
            'password':forms.TextInput(attrs={'type':'password','class':'form-control','placeholder':'contrasena'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name', 'email','birthdate','sex','section')
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Nombres'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Apellidos'}),
            'email':forms.TextInput(attrs={'type':'email','class':'form-control','placeholder':'Escriba su correo electronico'}),
            'birthdate':forms.TextInput(attrs={'class':'form-control','placeholder':'Elija fecha de nacimiento','type':'date'}),
            'sex':forms.Select(attrs={'type':'text','class':'form-control','placeholder':'Sexo'}),
            'section':forms.Select(attrs={'type':'text','class':'form-control','placeholder':'Matutina/Nocturna'}),
        }

class ChangePasswordForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('password',)
        widgets={
            'password':forms.TextInput(attrs={'type':'password','class':'form-control','placeholder':'contrasena'}),
        }

class EditarContrasenaForm(forms.Form):

    # actual_password = forms.CharField(
    #     label='Contrasena actual',
    #     min_length=5,
    #     widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    password = forms.CharField(
        label='Nueva contraseña',
        min_length=5,
        widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Nueva contraseña - (5 caracteres)'}))

    password2 = forms.CharField(
        label='Repetir contraseña',
        min_length=5,
        widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Confirmar contraseña'}))

    def clean_password2(self):
        """Comprueba que password y password2 sean iguales."""

        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return password2