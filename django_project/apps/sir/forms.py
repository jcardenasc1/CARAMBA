# -*- encoding: utf-8 -*-
from django import forms
from .models import Evaluation,Characteristic,Exercise,Semester,Course


class EvaluationForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields=('file','like','difficulty','duration','exercise')
        widgets={
            'file':forms.FileInput(attrs={'class':'form-control'}),
            'like':forms.TextInput(attrs={'class':'form-control','placeholder':'Califique el gusto'}),
            'difficulty':forms.TextInput(attrs={'class':'form-control','placeholder':'Califique la dificultad'}),
            'duration':forms.TextInput(attrs={'class':'form-control','placeholder':'Tiempo de duracion','hidden':'hidden'}),
            'exercise':forms.TextInput(attrs={'class':'form-control','placeholder':'Numero de ejercicio','id':'exercise','hidden':'hidden'}),
        }


class CharacteristicForm(forms.ModelForm):
    class Meta:
        model = Characteristic
        exclude = ('created','modified','user')
        widgets={
            'description':forms.TextInput(attrs={'class':'form-control','placeholder':'Paralelismo, Logica, etc'}),
            # 'state':forms.CheckboxInput(attrs={'class':'form-control','id':'switch-inverse','data-inverse':'true'}),
        }


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        exclude = ('created','modified','user')
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre del ejercicio - (Movimientos básicos) '}),
            'description':forms.Textarea(attrs={'class':'form-control','rows':'15', 'cols':'80','placeholder':'Breve descripcion del ejercicio','id':'elm1'}),
            'characteristic':forms.Select(attrs={'type':'text','class':'form-control'}),
            'level':forms.TextInput(attrs={'type':'text','class':'form-control'}),
        }


class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        exclude = ('created','modified')
        widgets={
            'description':forms.TextInput(attrs={'class':'form-control','placeholder':'Escriba el nivel del semestre - (1er Semestre)'}),
            # 'state':forms.CheckboxInput(attrs={'class':'form-control','id':'switch-inverse','data-inverse':'true'}),
        }


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        exclude = ('created','modified')
        widgets={
            'semester' :forms.Select(attrs={'type':'text','class':'form-control'}),
            'user':forms.Select(attrs={'type':'text','class':'form-control'}),
            'description':forms.TextInput(attrs={'class':'form-control','placeholder':'Escriba el nombre del curso - (A1)'}),
            # 'state':forms.CheckboxInput(attrs={'class':'form-control','id':'switch-inverse','data-inverse':'true'}),
        }