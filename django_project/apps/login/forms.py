from django import forms
from apps.usuario.models import User


class UserLoginForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={ 'class': 'form-control','id': 'email', 'type': 'text', 'placeholder': 'Ingrese usuario',
                                          }))

    password = forms.CharField(max_length=50,
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control', 'id': 'password', 'type': 'password', 'placeholder': 'Ingrese una contrasena',
                               }))

class RegistroUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','password','first_name','last_name','email','sex','section','birthdate')
        widgets={
            'first_name':forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Ingrese sus nombre'}),
            'last_name':forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Ingrese sus apellidos'}),
            'sex':forms.Select(attrs={'class': 'form-control', 'type': 'text'}),
            'section':forms.Select(attrs={'class': 'form-control', 'type': 'text'}),
            'birthdate':forms.DateInput(attrs={'class':'form-control','placeholder':'Elija una fecha','type':'date'}),
            # 'status':forms.Select(attrs={'class': 'form-control', 'type': 'text'}),
            'email':forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Ingrese su email'}),
            'username':forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Ingrese usuario'}),
            'password':forms.TextInput(attrs={'type':'password','class':'form-control','placeholder':'Ingrese contrasena'}),
        }

