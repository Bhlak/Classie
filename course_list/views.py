from django.shortcuts import render
from .models import Clist, Department
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

# Create your views here.
class ClistAPIView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        dict_clist = [{"course_title":"Introduction to Programming with C", "course_code":"COSC101", "year":"1", "faculty":"Faculty of Computing and Engineering Sciences", "departments" : "Information Technology", "dep_code":"ITGY"},
                      {"course_title":"Introduction to Programming with C", "course_code":"COSC101", "year":"1", "faculty":"Faculty of Computing and Engineering Sciences", "departments" : "Software Engineering", "dep_code":"SENG"},
                      {"course_title":"Hardware", "course_code":"COSC111", "year":"1", "faculty":"Faculty of Computing and Engineering Sciences", "departments" : "Software Engineering", "dep_code":"SENG"},
                      {"course_title":"Hardware", "course_code":"COSC111", "year":"1", "faculty":"Faculty of Computing and Engineering Sciences", "departments" : "Information Technology", "dep_code":"ITGY"},
                      
                      {"course_title":"VB.NET", "course_code":"COSC211", "year":"2", "faculty":"Faculty of Computing and Engineering Sciences", "departments" : "Software Engineering", "dep_code":"SENG"},
                      {"course_title":"VB.NET", "course_code":"COSC211", "year":"2", "faculty":"Faculty of Computing and Engineering Sciences", "departments" : "Information Technology", "dep_code":"ITGY"},
                      {"course_title":"Operating Systems1", "course_code":"COSC203", "year":"2", "faculty":"Faculty of Computing and Engineering Sciences", "departments" : "Information Technology", "dep_code":"ITGY"},
                      {"course_title":"Operating Systems1", "course_code":"COSC203", "year":"2", "faculty":"Faculty of Computing and Engineering Sciences", "departments" : "Software Engineering", "dep_code":"SENG"},
                      
                      {"course_title":"Operating Systems2", "course_code":"COSC303", "year":"3", "faculty":"Faculty of Computing and Engineering Sciences", "departments" : "Information Technology", "dep_code":"ITGY"},
                      {"course_title":"Operating Systems2", "course_code":"COSC303", "year":"3", "faculty":"Faculty of Computing and Engineering Sciences", "departments" : "Software Engineering", "dep_code":"SENG"},
                      {"course_title":"ISAAD", "course_code":"COSC313", "year":"3", "faculty":"Faculty of Computing and Engineering Sciences", "departments" : "Information Technology", "dep_code":"ITGY"},
                      {"course_title":"ISAAD", "course_code":"COSC313", "year":"3", "faculty":"Faculty of Computing and Engineering Sciences", "departments" : "Software Engineering", "dep_code":"SENG"},
                      
                      {"course_title":"Machine Learning", "course_code":"COSC400", "year":"4", "faculty":"Faculty of Computing and Engineering Sciences", "departments" : "Software Engineering" ,"dep_code":"SENG"},
                      {"course_title":"Machine Learning", "course_code":"COSC400", "year":"4", "faculty":"Faculty of Computing and Engineering Sciences", "departments" : "Information Technology", "dep_code":"ITGY"},
                      {"course_title":"NMA2", "course_code":"COSC410", "year":"4", "faculty":"Faculty of Computing and Engineering Sciences", "departments" : "Information Technology", "dep_code":"ITGY"},
                      {"course_title":"NMA2", "course_code":"COSC410", "year":"4", "faculty":"Faculty of Computing and Engineering Sciences", "departments" : "Software Engineering" ,"dep_code":"SENG"},
                      
                      {"course_title":"Machine Learning2", "course_code":"COSC500", "year":"5", "faculty":"Faculty of Computing and Engineering Sciences", "departments" : "Information Technology", "dep_code":"ITGY"},
                      {"course_title":"Machine Learning2", "course_code":"COSC500", "year":"5", "faculty":"Faculty of Computing and Engineering Sciences", "departments" : "Software Engineering", "dep_code":"SENG"},
                      {"course_title":"DBMS", "course_code":"COSC510", "year":"5", "faculty":"Faculty of Computing and Engineering Sciences", "departments" : "Software Engineering", "dep_code":"SENG"},
                      {"course_title":"DBMS", "course_code":"COSC510", "year":"5", "faculty":"Faculty of Computing and Engineering Sciences", "departments" : "Information Technology", "dep_code":"ITGY"},
                      
                      {"course_title":"Biology1", "course_code":"BIO105", "year":"1", "faculty":"Faculty of Medical Sciences", "departments" : "Anatomy", "dep_code": "ANAT"},
                      {"course_title":"Surgery", "course_code":"BIO115", "year":"1", "faculty":"Faculty of Medical Sciences", "departments" : "Anatomy", "dep_code": "ANAT"},
                      {"course_title":"Biology1", "course_code":"BIO105", "year":"1", "faculty":"Faculty of Medical Sciences", "departments" : "Physiology",  "dep_code": "PHYS"},
                      {"course_title":"Surgery", "course_code":"BIO115", "year":"1", "faculty":"Faculty of Medical Sciences", "departments" : "Physiology",  "dep_code": "PHYS"},
                    
                    
                      {"course_title":"Biology2", "course_code":"BIO205", "year":"2", "faculty":"Faculty of Medical Sciences", "departments" : "Physiology", "dep_code": "PHYS"},
                      {"course_title":"Vet", "course_code":"BIO215", "year":"2", "faculty":"Faculty of Medical Sciences", "departments" : "Physiology", "dep_code": "PHYS"},
                      {"course_title":"Biology2", "course_code":"BIO205", "year":"2", "faculty":"Faculty of Medical Sciences", "departments" : "Physiology",  "dep_code": "PHYS"},
                      {"course_title":"Vet", "course_code":"BIO215", "year":"2", "faculty":"Faculty of Medical Sciences", "departments" : "Physiology",  "dep_code": "PHYS"},
                      
                      {"course_title":"Physiology", "course_code":"PHG333", "year":"3", "faculty":"Faculty of Medical Sciences", "departments" : "Anatomy", "dep_code": "ANAT"},
                      {"course_title":"Physiology", "course_code":"PHG333", "year":"3", "faculty":"Faculty of Medical Sciences", "departments" : "Physiology", "dep_code": "PHYS"},
                      {"course_title":"Human Anatomy", "course_code":"PHG313", "year":"3", "faculty":"Faculty of Medical Sciences", "departments" : "Anatomy", "dep_code": "ANAT"},
                      {"course_title":"Human Anatomy", "course_code":"PHG313", "year":"3", "faculty":"Faculty of Medical Sciences", "departments" : "Physiology", "dep_code": "PHYS"},
                      
                      {"course_title":"Bio-mechanics", "course_code":"BIM422", "year":"4", "faculty":"Faculty of Medical Sciences", "departments" : "Anatomy", "dep_code": "ANAT"},
                      {"course_title":"Physiology2", "course_code":"PHG432", "year":"4", "faculty":"Faculty of Medical Sciences", "departments" : "Anatomy", "dep_code": "ANAT"},
                      {"course_title":"Bio-mechanics", "course_code":"BIM422", "year":"4", "faculty":"Faculty of Medical Sciences", "departments" :"Physiology", "dep_code": "PHYS"},
                      {"course_title":"Physiology2", "course_code":"PHG432", "year":"4", "faculty":"Faculty of Medical Sciences", "departments" :"Physiology", "dep_code": "PHYS"},
                        
                      {"course_title":"Bio-mechanics2", "course_code":"BIM522", "year":"5", "faculty":"Faculty of Medical Sciences", "departments" :"Physiology", "dep_code": "PHYS"},
                      {"course_title":"Bio-mechanics2", "course_code":"BIM522", "year":"5", "faculty":"Faculty of Medical Sciences", "departments" : "Anatomy", "dep_code": "ANAT"}
                      {"course_title":"Bio-mechanics3", "course_code":"BIM520", "year":"5", "faculty":"Faculty of Medical Sciences", "departments" :"Physiology", "dep_code": "PHYS"},
                      {"course_title":"Bio-mechanics3", "course_code":"BIM520", "year":"5", "faculty":"Faculty of Medical Sciences", "departments" : "Anatomy", "dep_code": "ANAT"},
                      {"course_title":"Bio-mechanics3", "course_code":"BIM520", "year":"5", "faculty":"Faculty of Medical Sciences", "departments" : "Anatomy", "dep_code": "ANAT"}
                      ]
        
        dep_list = [{"dep_name":"Anatomy", "dep_code":"ANAT", "faculty": "Faculty of Medical Sciences"},
                    {"dep_name":"Physiology", "dep_code":"PHYS", "faculty":"Faculty of Medical Sciences"},
                    {"dep_name":"Information Technology", "dep_code": "ITGY", "faculty":"Faculty of Computing and Engineering Sciences"},
                    {"dep_name":"Software Engineering", "dep_code": "SENG", "faculty":"Faculty of Computing and Engineering Sciences"}
                    ]

        #department_dict = {}
        for dep_dict in dep_list:
            Department.objects.create(
              dep_name = dep_dict["dep_name"],
              dep_code = dep_dict["dep_code"],
              faculty = dep_dict["faculty"]
              )
            #department_dict[dep_dict["name"]] = department

       
        for data_dict in dict_clist:
            Clist.objects.create(
              course_title = data_dict["course_title"],
              course_code = data_dict["course_code"],
              year = data_dict["year"],
              faculty = data_dict["faculty"],
              departments = data_dict["departments"],
              dep_code = data_dict["dep_code"]
            )
            
            # for dep_name in data_dict["departments"]:
            #     department = department_dict.get(dep_name)
            #     if department:
            #         course.departments.add(department)
            
        return Response({"message":"Course created"})