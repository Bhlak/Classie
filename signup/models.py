from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=90)
    matric_no = models.CharField(max_length=10)
    faculty = models.CharField(max_length=15)
    department = models.CharField(max_length=20)
    level = models.IntegerField()
    user_type = models.CharField(max_length=10, default="student")


# {
# "full_name": "Abe",
# "email": "hated@gmail.com",
# "password": "1122",
# "matric_no": "22334455",
# "faculty": "Engineering",
# "department": "Computer Engineering",
# "level": 200,
# "user_type": "student"
# }
    
class Lecturer(models.Model):
    full_name = models.CharField(max_length=100)
    title = models.CharField(max_length=15)
    email = models.EmailField()
    faculty = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    year = models.IntegerField()
    course_title = models.CharField(max_length=100)
    course_code = models.CharField(max_length=100)
    