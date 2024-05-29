from rest_framework import serializers
from .models import CustomUser, Student, Lecturer
from course_list.models import Department
from datetime import datetime
import random


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
            temp = self.class_checks(student, year, department, matric_no)
            student.class_code = temp
            student.save()
        elif userType == 'lecturer':
            Lecturer.objects.create(user=user, lecID=lecID, title=title)
        return user
    
    def class_checks(self, student, year, department, matric_no):
        current_year = datetime.now().year
        matric_year  = int('20' + matric_no[:2])
        matric_code = matric_no[3:7]

        dep_code = self.dep_codefetch(department)

        if int(current_year) - int(matric_year) == int(year) and matric_code == dep_code:
            random1 = random.randint(1000, 9999)
            random2 = random.randint(10, 99)
            class_code = f'{random1}{dep_code}{random2}0{year}'

            return class_code

    def dep_codefetch(self, dep):
        department = Department.objects.get(name__exact=dep)
        return department.dep_code

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class LecturerSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Lecturer
        fields = '__all__'