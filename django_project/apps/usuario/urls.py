from django.conf.urls import patterns, include, url
from .views import profile,editar_contrasena,list_students,Registered,CourseList,Register,list_course

urlpatterns = patterns('',

    url(r'perfil/(?P<slug>[-\w]+)/$' ,profile.as_view(), name="profile"),
    url(r'^editar_contrasena/$', 'apps.usuario.views.editar_contrasena', name='password'),
    url(r'^misEstudiantes/(?P<pk>\d+)/$', list_students.as_view(), name='students'),
    url(r'^misCursos/$', list_course.as_view(), name='courses'),
    url(r'^matricula/$', Registered.as_view(), name='registered'),
    url(r'^listadoCursos/$', CourseList.as_view(), name='CourseList'),
    url(r'^registrarme/$', Register.as_view(), name='Register'),


)