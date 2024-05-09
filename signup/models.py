from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=45)
    email = models.EmailField()
    password = models.CharField(max_length=10)

    def checker(self):
        test = input("Input: ")
        return True and check_password(test, self.password)
    
class Lecturer(models.Model):
    full_name = models.CharField(max_length=100)
    title = models.CharField(max_length=15)
    lecID = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    passwordd = models.CharField(max_length=100)

    def __str__(self):
        return self.email