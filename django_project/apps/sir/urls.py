from django.conf.urls import patterns, include, url
from .views import startExercise,allExercise,Search,Recommended,Level,newExercise, editExercise,\
    searchExercise, listExercise, listCharacteristic, newCharacteristic, editCharacteristic,\
    listCourse, newCourse,editCourse, \
    listSemester,newSemester,editSemester,\
    myStudent,showExercise,myLevel,\
    ReportUserExcel,ReportExerciseExcel,ReportEvaluationExcel

from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(r'^comenzar/$' , login_required(startExercise.as_view(), login_url='/'), name='start'),
    url(r'^ejercicio-todos/$' , allExercise.as_view(), name='allExercise'),
    url(r'^consultar-ejercicio/$' , Search.as_view(), name='SearchExercise'),
    url(r'^recomendacion/$' , Recommended.as_view(), name='Recommended'),
    url(r'^nivelAcademico/$' , Level.as_view(), name='Level'),
    url(r'^crearEjercicio/$' , newExercise.as_view(), name='newExercise'),
    url(r'^editarEjercicio/(?P<pk>\d+)/$' , editExercise.as_view(), name='editExercise'),
    url(r'^misEjercicio/$' , searchExercise.as_view(), name='searchExercise'),
    url(r'^panelEjercicio/$' , listExercise.as_view(), name='adminExercise'),

    url(r'^panelCaracteristicas/$' , listCharacteristic.as_view(), name='adminCharacteristic'),
    url(r'^crearCaracteristica/$' , newCharacteristic.as_view(), name='newCharacteristic'),
    url(r'^editarCaracteristica/(?P<pk>\d+)/$' , editCharacteristic.as_view(), name='editCharacteristic'),

    url(r'^panelSemestre/$' , listSemester.as_view(), name='adminSemester'),
    url(r'^crearSemestre/$' , newSemester.as_view(), name='newSemester'),
    url(r'^editarSemestre/(?P<pk>\d+)/$' , editSemester.as_view(), name='editSemester'),

    url(r'^panelCurso/$' , listCourse.as_view(), name='adminCourse'),
    url(r'^crearCurso/$' , newCourse.as_view(), name='newCourse'),
    url(r'^editarCurso/(?P<pk>\d+)/$' , editCourse.as_view(), name='editCourse'),

    url(r'^miListaEstudiantes/$' , myStudent.as_view(), name='myStudent'),
    url(r'^verEjerciciosEstudiantes/$' , showExercise.as_view(), name='showExercise'),
    url(r'^mi-nivel/$' , myLevel, name='myLevel'),

    url(r'^reporte-usuario/$' , login_required(ReportUserExcel, login_url='/'), name='exportUser'),
    url(r'^reporte-ejercicio/$' , login_required(ReportExerciseExcel, login_url='/'), name='exportExercise'),
    url(r'^reporte-evaluacion/$' , login_required(ReportEvaluationExcel, login_url='/'), name='exportEvaluation'),


    # url(r'configuracion/(?P<slug>[-\w]+)/$' ,configuracion.as_view(), name="config"),
    # url(r'configuracion/pass/(?P<slug>[-\w]+)/$', cambiarcontrasenaView.as_view(), name="pass"),
    # url(r'^editar_contrasena/$', 'apps.usuario.views.editar_contrasena', name='accounts.editar_contrasena'),

)