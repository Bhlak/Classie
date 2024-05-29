from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)
    dep_code = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    def __str__(self):
        return self.name    

class Clist(models.Model):
    course_title = models.CharField(max_length=100)
    course_code = models.CharField(max_length=50)
    #departments = models.CharField(max_length=50)
    student_count_1 = models.IntegerField(default=0)
    student_count_2 = models.IntegerField(default=0)
    student_count_3 = models.IntegerField(default=0)
    student_count_4 = models.IntegerField(default=0)
    student_count_5 = models.IntegerField(default=0)
    faculty = models.CharField(max_length=50)
    level = models.IntegerField()
    departments = models.ManyToManyField(Department, related_name="courses")
    
    def __str__(self):
        return self.course_title
    
    def increment_student_count_1(self,year):
        if year == 1:
            self.student_count_1 += 1
        elif year == 2:
            self.student_count_2 += 1
        elif year == 3:
            self.student_count_3 += 1
        elif year == 4:
            self.student_count_4 += 1
        elif year == 5:
            self.student_count_5 += 1
            
        self.save()