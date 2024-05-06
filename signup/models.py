from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Student(models.Model):
    full_name = models.CharField(max_length=45)
    email = models.EmailField()
    password = make_password(models.CharField(max_length=10))


    def checker(self):
        test = input("Input: ")
        return True and check_password(test, self.password)