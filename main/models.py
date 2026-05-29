# main/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_tutor = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='main_users',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='main_users',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subjects = models.CharField(max_length=200)
    skills = models.CharField(max_length=200)
    availability = models.CharField(max_length=200)

class Hire(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
