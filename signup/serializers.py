from rest_framework import serializers
from .models import CustomUser, Student
# # , Lecturer


class CustomUserSerializer(serializers.ModelSerializer):
    matric_no = serializers.CharField(write_only=True, required=False)
    level = serializers.CharField(write_only=True, required=False)
    department = serializers.CharField(write_only=True, required=False)
    faculty = serializers.CharField(write_only=True, required=False)
    type = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = CustomUser
        fields = "__all__"
    
    def create(self, validated):
        level = validated.pop('level', '')
        matric_no = validated.pop('matric_no', '')
        department = validated.pop('department', '')
        faculty = validated.pop('faculty', '')
        userType = validated.pop('type', '')
        user = CustomUser.objects.create_user(**validated)

        if userType == 'student':
            Student.objects.create(user=user, level=level, department=department, faculty=faculty, matric_no=matric_no)
        
        return user

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

# # class LecturerSerializer(serializers.ModelSerializer): 
# #     class Meta:
# #         model = Lecturer
# #         fields = '__all__'