from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100, default="faculty of computing and engineering sciences")
    def __str__(self):
        return self.name    

class Clist(models.Model):
    course_title = models.CharField(max_length=100)
    course_code = models.CharField(max_length=50)
    #departments = models.CharField(max_length=50)
    faculty = models.CharField(max_length=50)
    year = models.IntegerField()
    departments = models.ManyToManyField(Department, related_name="courses")
    
    def __str__(self):
        return self.course_title