from django.shortcuts import render
from .models import Clist #, Department
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

# Create your views here.
class ClistAPIView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        dict_clist = [{"course_title":"Introduction to Programming with C", "course_code":"COSC101", "year":"1", "faculty":"Faculty of Computing and Engineering Sciences", "departments" : "Information Technology"},
                      {"course_title":"Introduction to Programming with C", "course_code":"COSC101", "year":"1", "faculty":"Faculty of Computing and Engineering Sciences", "departments" : "Software Engineering"},
                      {"course_title":"Operating Systems1", "course_code":"COSC203", "year":"200", "faculty":"Faculty of Computing and Engineering Sciences", "departments" : "Information Technology"},
                      {"course_title":"Operating Systems1", "course_code":"COSC203", "year":"200", "faculty":"Faculty of Computing and Engineering Sciences", "departments" : "Software Engineering"},
                      {"course_title":"Operating Systems2", "course_code":"COSC303", "year":"300", "faculty":"Faculty of Computing and Engineering Sciences", "departments" : "Information Technology"},
                      {"course_title":"Operating Systems2", "course_code":"COSC303", "year":"300", "faculty":"Faculty of Computing and Engineering Sciences", "departments" : "Software Engineering"},
                      {"course_title":"Machine Learning", "course_code":"COSC400", "year":"400", "faculty":"Faculty of Computing and Engineering Sciences", "departments" : "Software Engineering"},
                      {"course_title":"Machine Learning", "course_code":"COSC400", "year":"400", "faculty":"Faculty of Computing and Engineering Sciences", "departments" : "Information Technology"},
                      {"course_title":"Machine Learning2", "course_code":"COSC500", "year":"500", "faculty":"Faculty of Computing and Engineering Sciences", "departments" : "Information Technology"},
                      {"course_title":"Machine Learning2", "course_code":"COSC500", "year":"500", "faculty":"Faculty of Computing and Engineering Sciences", "departments" : "Software Engineering"},
                      {"course_title":"Biology1", "course_code":"BIO105", "year":"100", "faculty":"Faculty of Medical Sciences", "departments" : "Anatomy"},
                      {"course_title":"Biology2", "course_code":"BIO205", "year":"200", "faculty":"Faculty of Medical Sciences", "departments" : "Physiology"},
                      {"course_title":"Physiology", "course_code":"PHG333", "year":"300", "faculty":"Faculty of Medical Sciences", "departments" : "Physiology"},
                      {"course_title":"Bio-mechanics", "course_code":"BIM422", "year":"400", "faculty":"Faculty of Medical Sciences", "departments" : "Anatomy"},
                      {"course_title":"Bio-mechanics2", "course_code":"BIM522", "year":"500", "faculty":"Faculty of Medical Sciences", "departments" :"Physiology"},
                      {"course_title":"Biology1", "course_code":"BIO105", "year":"100", "faculty":"Faculty of Medical Sciences", "departments" : "Anatomy"},
                      {"course_title":"Biology2", "course_code":"BIO205", "year":"200", "faculty":"Faculty of Medical Sciences", "departments" : "Physiology"},
                      {"course_title":"Physiology", "course_code":"PHG333", "year":"300", "faculty":"Faculty of Medical Sciences", "departments" : "Anatomy"},
                      {"course_title":"Bio-mechanics", "course_code":"BIM422", "year":"400", "faculty":"Faculty of Medical Sciences", "departments" :"Physiology"},
                      {"course_title":"Bio-mechanics2", "course_code":"BIM522", "year":"500", "faculty":"Faculty of Medical Sciences", "departments" : "Anatomy"}
                      ]
        
        # dep_list = [{"name":"Anatomy", "dep_code":"ANY", "faculty": "Faculty of Medical Sciences"},
        #             {"name":"Physiology", "dep_code":"PHYS", "faculty":"Faculty of Medical Sciences"},
        #             {"name":"Information Technology", "dep_code": "COSC", "faculty":"Faculty of Computing and Engineering Sciences"},
        #             {"name":"Software Engineering", "dep_code": "SENG", "faculty":"Faculty of Computing and Engineering Sciences"}]

        # department_dict = {}
        # for dep_dict in dep_list:
        #     department, created = Department.objects.get_or_create(
        #       name=dep_dict["name"],
        #       dep_code=dep_dict["dep_code"],
        #       faculty=dep_dict["faculty"]
        #       )
        #     department_dict[dep_dict["name"]] = department

       
        for data_dict in dict_clist:
            Clist.objects.create(
              course_title = data_dict["course_title"],
              course_code = data_dict["course_code"],
              year = data_dict["year"],
              faculty = data_dict["faculty"],
              departments = data_dict["departments"]
            )
            
            # for dep_name in data_dict["departments"]:
            #     department = department_dict.get(dep_name)
            #     if department:
            #         course.departments.add(department)
            
        return Response({"message":"Course created"})