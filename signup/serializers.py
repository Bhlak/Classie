from rest_framework import serializers
from .models import CustomUser, Student, Lecturer
from datetime import datetime


class CustomUserSerializer(serializers.ModelSerializer):
    matric_no = serializers.CharField(write_only=True, required=False)
    year = serializers.CharField(write_only=True, required=False)
    department = serializers.CharField(write_only=True, required=False)
    faculty = serializers.CharField(write_only=True, required=False)
    type = serializers.CharField(write_only=True, required=False)
    title = serializers.CharField(write_only=True, required=False)
    lecID = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = CustomUser
        fields = "__all__"
    
    def create(self, validated):
        year = validated.pop('year', '')
        matric_no = validated.pop('matric_no', '')
        department = validated.pop('department', '')
        faculty = validated.pop('faculty', '')
        userType = validated.pop('type', '')
        lecID = validated.pop('lecID', '')
        title = validated.pop('title', '')
        user = CustomUser.objects.create_user(**validated)

        if userType == 'student':
            try:
                student = Student.objects.create(user=user, year=year, department=department, faculty=faculty, matric_no=matric_no)
            except Exception as e:
                print(f"Exception E: {e}")
            self.class_checks(student, year, department, matric_no)
        elif userType == 'lecturer':
            Lecturer.objects.create(user=user, lecID=lecID, title=title)
        return user
    
    def class_checks(self, student, year, department, matric_no):
        current_year = datetime.now().year
        matric_year  = int('20' + matric_no[:2])

        dep = self.dep_code_fetch()
        
        if current_year - matric_year == year and department == dep:
            pass

    def dep_fetch(self, dep_code):
        dep = 'placeholder'
        return dep

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class LecturerSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Lecturer
        fields = '__all__'