from django.contrib import admin
from .models import CustomUser, Student, Lecturer

admin.site.register(CustomUser)
admin.site.register(Student)
admin.site.register(Lecturer)
