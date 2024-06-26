from rest_framework import serializers
from .models import Assignment

class AssignmentSerializer(serializers.ModelSerializer):
    question = serializers.CharField(write_only=True, required=True)
    deadline = serializers.DateTimeField(required=True)

    class Meta:
        model = Assignment
        fields = "__all__"