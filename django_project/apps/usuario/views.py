from django.template import RequestContext
from django.core.urlresolvers import reverse_lazy
from braces.views import LoginRequiredMixin
from datetime import datetime
from django.utils import timezone
from django.core import context_processors
from django.views.generic import CreateView,UpdateView,DeleteView, TemplateView, View, FormView
from .forms import UserForm , EditForm,ChangePasswordForm,EditarContrasenaForm
from .models import User
from apps.sir.models import registration,Course

from django.shortcuts import  render_to_response, render, redirect , get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.contrib.auth.hashers import make_password
from django.contrib import messages

class profile(UpdateView):
    model = User
    form_class = EditForm
    slug_field = 'username'
    fields = ['first_name','last_name', 'email','birthdate','sex','section']
    template_name = 'usuario/perfil.html'
    success_url = reverse_lazy('start')
    context_object_name = 'usuario'

    def get_object(self, queryset=None):
        return self.request.user


def editar_contrasena(request):
    if request.method == 'POST':
        form = EditarContrasenaForm(request.POST)
        if form.is_valid():
            request.user.password = make_password(form.cleaned_data['password'])
            request.user.save()
            # messages.success(request, 'La contrasena ha sido cambiado con exito')
            # messages.success(request, 'Es necesario introducir los datos para entrar')
            return HttpResponseRedirect('/')
    else:
        form = EditarContrasenaForm()
    return render(request, 'usuario/cambio.html', {'form': form})


class list_students(TemplateView):
    template_name = 'usuario/listaEstudiantes.html'

    def get_context_data(self, **kwargs):
        context=super(list_students, self).get_context_data(**kwargs)
        students_list = registration.objects.filter(course__pk=self.kwargs.get('pk')).order_by('user__last_name')
        context['estudiantes']=students_list
        context['cantidad']=context['estudiantes'].count()

        return context


class list_course(TemplateView):
    template_name = 'usuario/listaCursos.html'

    def get_context_data(self, **kwargs):
        context=super(list_course, self).get_context_data(**kwargs)

        if self.request.user.is_superuser:
            course_list = Course.objects.filter().order_by('-created')
        else:
            course_list = Course.objects.filter(user=self.request.user).order_by('-created')
        context['cursos']=course_list
        context['cantidad']=context['cursos'].count()

        return context

class Registered(TemplateView):

    def get(self,request,*args,**kwargs):
        registered = registration.objects.filter(user=self.request.user)
        context=[]
        json = {
                    "registro": registered.exists()
                }
        context.append(json)

        return JsonResponse(context,safe=False)


class CourseList(TemplateView):

    def get(self,request,*args,**kwargs):
        course = Course.objects.all()
        context=[]
        for c in course:
            str = c.user.first_name + ' ' + c.user.last_name
            json = {
                        "id": c.id,
                        "semestre": c.semester.description,
                        "docente": str,
                        "curso": c.description,
                    }
            context.append(json)

        return JsonResponse(context,safe=False)


class Register(TemplateView):

    def get(self,request,*args,**kwargs):
        # print "asds"
        # print request.GET['id']

        registration.objects.create(
            course = Course.objects.get(pk=request.GET['id']),
            user = self.request.user,

        )
        acc = True

        return JsonResponse(acc,safe=False)