# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.sir.validators
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Characteristic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(max_length=140)),
                ('state', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(max_length=100)),
                ('state', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(upload_to=b'scratch', validators=[apps.sir.validators.valid_extension])),
                ('duration', models.CharField(max_length=10)),
                ('like', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(6), django.core.validators.MinValueValidator(0)])),
                ('difficulty', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(6), django.core.validators.MinValueValidator(0)])),
                ('score', models.IntegerField(default=0)),
                ('abstraction', models.IntegerField(default=0)),
                ('parallelization', models.IntegerField(default=0)),
                ('logic', models.IntegerField(default=0)),
                ('synchronization', models.IntegerField(default=0)),
                ('flowControl', models.IntegerField(default=0)),
                ('userInteractivity', models.IntegerField(default=0)),
                ('dataRepresentation', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=140)),
                ('description', models.CharField(max_length=5000)),
                ('level', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(6), django.core.validators.MinValueValidator(0)])),
                ('state', models.BooleanField(default=True)),
                ('characteristic', models.ForeignKey(to='sir.Characteristic')),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('state', models.BooleanField(default=True)),
                ('course', models.ForeignKey(blank=True, to='sir.Course', null=True)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(max_length=100)),
                ('state', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='exercise',
            field=models.ForeignKey(to='sir.Exercise'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='evaluation',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='semester',
            field=models.ForeignKey(blank=True, to='sir.Semester', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
