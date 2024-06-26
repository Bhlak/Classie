from django.db import models

# class Department(models.Model):
#     name = models.CharField(max_length=100)
#     dep_code = models.CharField(max_length=100)
#     faculty = models.CharField(max_length=100)
#     def __str__(self):
#         return self.name    

class Clist(models.Model):
    course_title = models.CharField(max_length=100)
    course_code = models.CharField(max_length=50)
    #departments = models.CharField(max_length=50)
    description = models.CharField(max_length = 250, default="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin venenatis, tellus sed iaculis fringilla, tellus quam tempor metus, quis efficitur tellus sapien quis lacus. Vivamus quis neque vitae arcu tempor consectetur non sed libero. Ut viverra ipsum vitae ipsum ultricies, ultricies auctor nulla malesuada. Duis quis sagittis eros, quis commodo massa. Mauris imperdiet erat non ullamcorper sodales. Mauris eget metus turpis.")
    location = models.CharField(max_length=10, default="E202")
    # student_count_1 = models.IntegerField(default=0)
    # student_count_2 = models.IntegerField(default=0)
    # student_count_3 = models.IntegerField(default=0)
    # student_count_4 = models.IntegerField(default=0)
    # student_count_5 = models.IntegerField(default=0)
    faculty = models.CharField(max_length=50)
    year = models.IntegerField()
    departments = models.CharField(max_length = 100)
    student_count = models.IntegerField(default=0)
    dep_code = models.CharField(max_length=100)

class Department(models.Model):
    dep_name = models.CharField(max_length=200)
    dep_code = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.course_title