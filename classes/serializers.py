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

        department = Department.objects.get(dep_code__exact=dep_code)
        
        courses = department.courses.all()

        for course in courses:
            if course.level == int(year):
                the_class.courses.add(course)

        # print(courses)

        # course = Clist.objects.filter(level=year, departments=dep_name)
        # print(course)
        # courses = Clist.objects.filter()

        return the_class
