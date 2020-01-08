from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from datetime import datetime
# from apps.sir.models import Evaluation


class UserManager(BaseUserManager, models.Manager):

    def _create_user(self, username, email, password, is_staff,
            is_superuser, **extra_fields):

        email = self.normalize_email(email)
        if not email:
            raise ValueError('El email debe ser obligatorio')
        user = self.model(username=username, email=email, is_active=True,
                is_staff=is_staff, is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False,
            **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password, True, True,
            **extra_fields)

    def get_by_natural_key(self, username):
        return self.get(username=username)

Sex=(
        ('1','MASCULINO'),
        ('2','FEMENINO'),
        ('3','OTRO'),

)

Section=(
        ('1','MATUTINA'),
        ('2','NOCTURNA'),
)

Status=(
        ('1','ESTUDIANTE'),
        ('2','DOCENTE'),
)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField(default=datetime.now)
    email = models.EmailField(max_length=50, null=True)
    sex = models.CharField(max_length=1, choices=Sex, default="1")
    section =models.CharField(max_length=1, choices=Section, default="1")
    status =models.CharField(max_length=1, choices=Status, default="1")

    objects = UserManager()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_short_name(self):
        return self.username

    class Meta:
        ordering = ['last_name']

    def __unicode__(self):
        return "%s %s" % (self.last_name, self.first_name)

