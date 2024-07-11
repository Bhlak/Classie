from rest_framework import serializers
from .models import Classes
from course_list.models import Clist, Department

class ClassSerializer(serializers.ModelSerializer):
    code = serializers.CharField()
    # courses = serializers.ManyRelatedField()

    class Meta:
        model = Classes
        fields = "__all__"
    
    def create(self, validated):
        code = validated.pop('code', '')

        dep_code = code[:4]
        year = code[-1]
        
        the_class = Classes.objects.create(code=code)

        # department = Department.objects.get(dep_code__exact=dep_code)
        
        
        courses = Clist.objects.filter(dep_code__exact=dep_code, year=year)

        for course in courses:
            if course.year == int(year):
                the_class.courses.add(course)
                the_class.save()


        return the_class
