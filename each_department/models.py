from django.db import models

# Create your models here.
class Cosc(models.Model):
    course_code = models.CharField(max_length=100)
    course_title = models.CharField(max_length=100)
    year = models.IntegerField()
    
class Phys(models.Model):
    course_code = models.CharField(max_length=100)
    course_title = models.CharField(max_length=100)
    year = models.IntegerField()
    
class Anam(models.Model):
    course_code = models.CharField(max_length=100)
    course_title = models.CharField(max_length=100)
    year = models.IntegerField()
    
class Seng(models.Model):
    course_code = models.CharField(max_length=100)
    course_title = models.CharField(max_length=100)
    year = models.IntegerField()