from rest_framework import serializers
from .models import Department, Clist

class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clist
        fields = "__all__"