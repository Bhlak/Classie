from django.db import models
from course_list.models import Clist

class Classes(models.Model):
    code = models.CharField(max_length=12, blank=False)
    courses = models.ManyToManyField(Clist, related_name="courses", blank=True)

    def __str__(self):
        return f'Year {self.code[10:]} {self.code[4:8]}' 
