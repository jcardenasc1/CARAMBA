from django.contrib import admin
from .models import Characteristic,Evaluation,Exercise,Semester,Course,registration
# Register your models here.


admin.site.register(Characteristic)
admin.site.register(Evaluation)
admin.site.register(Exercise)

admin.site.register(Semester)
admin.site.register(Course)
admin.site.register(registration)