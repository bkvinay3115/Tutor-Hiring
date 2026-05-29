# main/admin.py

from django.contrib import admin
from .models import User, Student, Tutor, Hire

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Tutor)
admin.site.register(Hire)
