from rest_framework import serializers
from .models import Clist

class ClistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clist
        fields = ['course_code', 'departments']