from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "full_name", "email", "password"]
        # , "matric_no", "faculty", "department", "level", "user_type"]