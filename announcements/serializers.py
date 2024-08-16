from rest_framework import serializers
from .models import Announcements, Comments
from courses.models import Clist
from courses.serializer import ClistSerializer

class AnnouncementsSerializer(serializers.ModelSerializer):
    code = ClistSerializer(many=True)
   
    
    class Meta:
        model = Announcements
        fields = ["announcement_id","announcement","code", "date"]
        
    # def validate(self, data):
    #     course_code = data.get("course_code")  
    #     departments = data.get("departments")
        
    #     print(f"number of courses found with course code {course_code} in {departments} department")
        
    #     try:
    #         code = Clist.objects.get(course_code=course_code, departments=departments)
    #     except Clist.DoesNotExist:
    #         raise serializers.ValidationError(f"No {course_code} found in {departments}")
    #     # if not courses.exists():
    #     #     raise serializers.ValidationError("Not found")
    #     # if courses.count() > 1:
    #     #     raise serializers.ValidationError(f"found multiple courses with {course_code} in {departments} department")
            
    #     data["code"] = code
    #     return data
    
    def create(self, validated_data):
        codes = validated_data.pop('code')
        # departments = validated_data.pop('departments')
        # code = Clist.objects.get(course_code=course_code, departments=departments)
        announcement = Announcements.objects.create(**validated_data)
        for c in codes:
            course_code = c.get('course_code')
            departments= c.get('departments')
            list = Clist.objects.get(course_code=course_code, departments=departments)
            announcement.code.add(list)
        
        return announcement

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'
        
        

#  {
# "announcement_id" : "1",
# "announcement": "This is an announcement",
# "code":[ 
# {"course_code":"COSC203", "departments":"Software Engineering", "course_title":"Operating Systems1"}
# ]
# }


# {
# "content" : "a comment",
# "announcement": 1,
# "student":"23SENG02"
# }
