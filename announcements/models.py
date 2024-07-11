from django.db import models
from course_list.models import Clist
from signup.models import Student
# Create your models here.
class Announcements(models.Model):
    announcement_id = models.IntegerField(primary_key=True)
    announcement = models.TextField()
    code = models.ManyToManyField(Clist, related_name="announcements")
    date = models.DateTimeField(auto_now=True)
    #comments = models.CharField(max_length=100)
    
class Comments(models.Model):
    content = models.TextField()
    announcement = models.ForeignKey(Announcements, related_name="comments", on_delete=models.CASCADE)
    #student = models.ForeignKey(Student, related_name="comments", on_delete=models.CASCADE)