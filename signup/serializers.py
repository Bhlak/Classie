from rest_framework import serializers
from .models import Student, Lecturer

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "full_name", "email", "password"]
        # , "matric_no", "faculty", "department", "level", "user_type"]

class LecturerSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Lecturer
        fields = '__all__'