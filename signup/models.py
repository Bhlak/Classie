from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    password = models.CharField(max_length=90,  null=False, blank=False)
    matric_no = models.CharField(max_length=10,  null=False, blank=False)
    faculty = models.CharField(max_length=15,  null=False, blank=False)
    department = models.CharField(max_length=20,  null=False, blank=False)
    level = models.IntegerField( null=False, default="heheh", blank=False)
    user_type = models.CharField(max_length=10, default="student", blank=False)


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
    full_name = models.CharField(max_length=100, null=False, blank=False)
    title = models.CharField(max_length=15, null=False, blank=False)
    lecID = models.CharField(max_length=10, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    passwordd = models.CharField(max_length=100, null=False, blank=False)
    
#{
#"id": 2,
#"full_name": "Princess .O. Etowe",
#"title": "Miss",
#"lecID": "BU1222E",
#"email": "petowe122@babcock.edu.ng",
#"password1": "1234",
#"password2":"1234" 
#}
    
    def __str__(self):
        return self.email