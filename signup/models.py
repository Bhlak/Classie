from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=45)
    email = models.EmailField()
    password = models.CharField(max_length=10)
    # matric_no = models.CharField(max_length=10)
    # faculty = models.CharField(max_length=15)
    # department = models.CharField(max_length=20)
    # level = models.IntegerField()
    # user_type = models.CharField(max_length=10, default="student")
    
class Lecturer(models.Model):
    full_name = models.CharField(max_length=100)
    title = models.CharField(max_length=15)
    email = models.EmailField()
    faculty = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    year = models.IntegerField()
    course_title = models.CharField(max_length=100)
    course_code = models.CharField(max_length=100)
    