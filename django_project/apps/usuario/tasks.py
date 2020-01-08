from .models import user,Facultad,Cargo,Materia,Nivel
from celery import shared_task
import urllib2, json
from django.contrib.auth.hashers import make_password
from apps.distributivo.models import Distributivo


@shared_task()
def agregaUsuario(usuario_id):
    j = urllib2.urlopen('http://sga.unemi.edu.ec/api?a=apilistadocentes&periodo='+usuario_id)
    j_obj = json.load(j)
    for jo in j_obj:
     nombres = jo['nombredocente']
     apellidos= jo['primerapellido'] + ' ' + jo['segundoapellido']
     segundo = jo['segundoapellido']
     usuario = user.objects.filter(first_name= nombres, last_name = apellidos)
     if not usuario.exists():
         cont=0
         if segundo == '':
            correo = nombres[0] + jo['primerapellido']
         else:
             correo = nombres[0] + jo['primerapellido'] + segundo[0]
         email = user.objects.filter(username__contains=correo.lower())
         if email.exists():
            for x in email:
                cont += 1
                # print cont
            id=str(cont)
            # print correo
            correo=correo+id
         user1=correo.lower()
         # print user1
         user.objects.create(
             first_name = nombres,
             last_name = apellidos,
             facultad = Facultad.objects.get(Descripcion=jo['facultad']),
             email = jo['correo'],
             email2 = jo['correoinst'],
             username = user1,
             password = make_password(user1),
             cargo = Cargo.objects.get(Descripcion=jo['cargo'])
         )


@shared_task()
def agregaDatos(nivel_id):
    try:

        j = urllib2.urlopen('http://sga.unemi.edu.ec/api?a=apilistadocentes&periodo=' + nivel_id )
        j_obj = json.load(j)

        j.close()
        for jo in j_obj:
            niv = Nivel.objects.filter(Descripcion=jo['nivelcurso'])
            if not niv.exists():
                Nivel.objects.create(
                    Descripcion = jo['nivelcurso'],
                )

        for jo in j_obj:
            mat = Materia.objects.filter(Descripcion=jo['materias'])
            if not mat.exists():
                Materia.objects.create(
                    Descripcion = jo['materias'],
                )
        for jo in j_obj:
            cargo = Cargo.objects.filter(Descripcion=jo['cargo'] )
            if not cargo.exists():
                Cargo.objects.create(
                    Descripcion = jo['cargo'],
                )
        for jo in j_obj:
         nombres = jo['nombredocente']
         apellidos= jo['primerapellido'] + ' ' + jo['segundoapellido']
         segundo = jo['segundoapellido']
         usuario = user.objects.filter(first_name= nombres, last_name = apellidos)
         if not usuario.exists():
             cont=0
             if segundo == '':
                correo = nombres[0] + jo['primerapellido']
             else:
                 correo = nombres[0] + jo['primerapellido'] + segundo[0]
             email = user.objects.filter(username__contains=correo.lower())
             if email.exists():
                for x in email:
                    cont += 1
                    # print cont
                id=str(cont)
                # print correo
                correo=correo+id
             user1=correo.lower()
             # print user1
             user.objects.create(
                 first_name = nombres,
                 last_name = apellidos,
                 facultad = Facultad.objects.get(Descripcion=jo['facultad']),
                 email = jo['correo'],
                 email2 = jo['correoinst'],
                 username = user1,
                 password = make_password(user1),
                 cargo = Cargo.objects.get(Descripcion=jo['cargo'])
             )


    except urllib2.HTTPError,e:
        print 'error'
        print e.code
    except urllib2.URLError,e:
        print "error url"
        print e.reason



@shared_task()
def agregaDistributivo(distributivo_id):
    Distributivo.objects.all().delete()
    j = urllib2.urlopen('http://sga.unemi.edu.ec/api?a=apilistadocentes&periodo='+distributivo_id)
    j_obj = json.load(j)
    for jo in j_obj:
        nombres = jo['nombredocente']
        apellidos= jo['primerapellido'] + ' ' + jo['segundoapellido']
        docent=user.objects.get(first_name=nombres,last_name=apellidos)
        distri=Distributivo.objects.filter(Docente=docent,dia=jo['dia'],comienza=jo['inicio'])
        if not distri.exists():

            Distributivo.objects.create(
                Docente = user.objects.get(first_name= nombres, last_name = apellidos),
                dia = jo['dia'],
                materia = Materia.objects.get(Descripcion=jo['materias']),
                nivel= Nivel.objects.get(Descripcion = jo['nivelcurso']),
                comienza = jo['inicio'],
                termina = jo['fin']
              )
        else:
            print 'existe'
