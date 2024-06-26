from django.db import models

class Assignment(models.Model):
    question = models.TextField()
    deadline = models.DateTimeField()

class Submission(models.Model):
    text = models.TextField()
    pdf = models.FileField()
    matric_no = models.CharField(max_length=20)
    assignment = models.ForeignKey(Assignment, related_name="submisson", on_delete=models.CASCADE)




