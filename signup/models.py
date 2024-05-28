from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

from .managers import CustomUserManager



class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=30)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Student(models.Model):
    user = models.OneToOneField(CustomUser, related_name='student', on_delete=models.CASCADE)
    matric_no = models.CharField(max_length=10, unique=True)
    faculty = models.CharField(max_length=15)
    department = models.CharField(max_length=20)
    year = models.IntegerField(default=1)
    is_verified = models.BooleanField(default=False)

    # @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    # def create_student(sender, instance, created, **extras):
    #     if created:
    #         stud = Student.objects.create(user=instance)
    
    # @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    # def save_student(sender, instance, **extras):
    #     instance.student.save()

    # @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    # def create_auth_token(sender, instance=None, created=False, **kwargs):
    #     if created:
    #         Token.objects.create(user=instance)

    # def __str__(self):
    #     return self.matric_no


# {
# "full_name": "Abe",
# "email": "second@gmail.com",
# "password": "2222",
# "matric_no": "1902",
# "faculty": "Engineering",
# "department": "Computer Engineering",
# "year": 2,
# "type": "student"
# }

# {
# "full_name": "Asbe",
# "email": "hasasa@gmail.com",
# "password": "1122",
# "type": "lecturer",
# "lecID": "2311211123",
# "title": "Professor"
# }


class Lecturer(models.Model):
    user = models.OneToOneField(CustomUser, related_name="lecturer", on_delete=models.CASCADE)
    title = models.CharField(max_length=15)
    lecID = models.CharField(max_length=10)
    
    # def __str__(self):
    #     return self.email
    