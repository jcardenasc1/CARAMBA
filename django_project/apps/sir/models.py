from django.db import models
from apps.usuario.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from .validators import valid_extension
# Create your models here.


class TimeStampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Characteristic(TimeStampModel):
    description = models.CharField(max_length=140)
    state = models.BooleanField(default=True)

    def __unicode__(self):
        return self.description

Range=(
        ('1','ESCUELA'),
        ('2','COLEGIO'),
        ('3','UNIVERSIDAD'),

)

class Exercise(TimeStampModel):
    user = models.ForeignKey(User, blank=True, null=True)
    name = models.CharField(max_length=140)
    description = models.CharField(max_length=5000)
    characteristic = models.ForeignKey(Characteristic)
    level = models.IntegerField(default=1, validators=[MaxValueValidator(6), MinValueValidator(0)])
    state = models.BooleanField(default=True)
    range = models.CharField(max_length=1, choices=Range, default="1", blank=True, null=True)

    def __unicode__(self):
        return "%s - %s - %s" % (self.name, self.characteristic.description, self.level)


class Evaluation(TimeStampModel):
    user = models.ForeignKey(User, blank=True, null=True)
    exercise = models.ForeignKey(Exercise)
    file = models.FileField(upload_to='scratch',validators=[valid_extension])
    duration = models.CharField(max_length=10)
    like = models.IntegerField(default=0, validators=[MaxValueValidator(6), MinValueValidator(0)])
    difficulty = models.IntegerField(default=0, validators=[MaxValueValidator(6), MinValueValidator(0)])
    score = models.IntegerField(default=0)
    abstraction = models.IntegerField(default=0)
    parallelization = models.IntegerField(default=0)
    logic = models.IntegerField(default=0)
    synchronization = models.IntegerField(default=0)
    flowControl = models.IntegerField(default=0)
    userInteractivity = models.IntegerField(default=0)
    dataRepresentation = models.IntegerField(default=0)

    def __unicode__(self):
        return "%s - %s" % (self.user.first_name, self.exercise.name)


class Semester(TimeStampModel):
    description = models.CharField(max_length=100)
    state = models.BooleanField(default=True)

    def __unicode__(self):
        return self.description


class Course(TimeStampModel):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE,blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    description = models.CharField(max_length=100)
    state = models.BooleanField(default=True)

    def __unicode__(self):
        return "%s - %s" % (self.description, self.semester)

    def cantidad(self):
        cant = registration.objects.filter(course=self).count()
        return cant


class registration(TimeStampModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,blank=True, null=True)
    state = models.BooleanField(default=True)

    def __unicode__(self):
        return "%s %s - %s" % (self.user.last_name,self.user.first_name, self.course)

    def cantidad(self):
        cant = Evaluation.objects.filter(user=self.user).count()
        return cant
