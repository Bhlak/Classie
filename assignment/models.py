from django.db import models
from courses.models import Clist

class Assignment(models.Model):
    question = models.TextField()
    deadline = models.DateTimeField()
    course = models.ForeignKey(Clist, related_name="course_assigned", on_delete=models.CASCADE)



# {
# "question": "Tis the first question",
# "deadline": "2024-07-03-12-30",
# "course_code": "COSC203",
# "dep_code": "SENG"
# }

class Submission(models.Model):
    text = models.TextField(blank=True)
    pdf = models.FileField(blank=True)
    matric_no = models.CharField(max_length=20)
    assignment = models.ForeignKey(Assignment, related_name="submisson", on_delete=models.CASCADE)


# {
# "text": "First Submission",
# "matric_no": "22/SENG01",
# "assignment": "1"
# }