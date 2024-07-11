from rest_framework import serializers
from .models import Assignment,Submission
from courses.models import Clist

class AssignmentSerializer(serializers.ModelSerializer):
    question = serializers.CharField(required=True)
    deadline = serializers.DateTimeField(required=True)

    class Meta:
        model = Assignment
        fields = "__all__"

    def create(self, validated):
        question = validated.pop('question', '')
        deadline = validated.pop('deadline', '')
        course = validated.pop('course', '')
        
        try:
            assignment = Assignment.objects.create(question=question, deadline=deadline, course=course)
        except Exception as e:
            print(f"Error Encountered SER: {e}")
        

        return assignment



class SubmissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Submission
        fields = "__all__"

    