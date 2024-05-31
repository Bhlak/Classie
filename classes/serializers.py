from rest_framework import serializers
from .models import Classes

class ClassSerializer(serializers.ModelSerializer):
    code = serializers.CharField()

    class Meta:
        model = Classes
        fields = "__all__"
    
    def create(self, validated):
        code = validated.pop('code', '')

        dep_code = code[:4]
        year = code[-1]
        
        the_class = Classes.objects.create(code=code)

        return the_class
