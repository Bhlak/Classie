import json
from rest_framework import status
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from django.contrib import messages
from .models import Lecturer
from django.contrib.auth.hashers import make_password


class SignUpView(APIView):
    def get(self, request, format=None):
        
        queryset = Student.objects.all()
        
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        try:
            data = request.data

            # Check if email has been used before
            email = data["email"]
            matric = data["matric_no"]

            if Student.objects.filter(email__exact=email).exists():
                return Response("Email already in use", status=status.HTTP_400_BAD_REQUEST)
            elif Student.objects.filter(matric_no__exact=matric).exists():
                return Response("Matric Number already registered", status=status.HTTP_400_BAD_REQUEST)
            else:
                # Hash the raw password
                raw_pwd = data['password']
                data['password'] = self.password_hash(raw_pwd)

                serializer = StudentSerializer(data=data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
        
    def password_hash(self, raw):
        try:
            hashed_pwd = make_password(raw)
        except Exception as e:
            print(f"Error encountered: {e}")
            return None
        return hashed_pwd

    # def put(self, request, format=None):
    #     try:s
    #         dat = request.data
    #         res = Student.objects.get(id__exact=dat['id'])
    #         serializer = StudentSerializer(res, data=dat)

    #         print(res.__dict__)

    #         if serializer.is_valid(raise_exception=True):
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_200_OK)
    #         else:
    #             print("nah")
    #             return Response(status=status.HTTP_400_BAD_REQUEST)

    #     except Exception as e:
    #         print(e)
    #         return Response(status=status.HTTP_400_BAD_REQUEST)

class LecturerView(APIView):
    def get(self, request):
        queryset = Lecturer.objects.all()
        return Response(status=status.HTTP_200_OK)
    
    def post(self, request):
        # if request.method == 'POST':
        email = request.POST['email']
        faculty = request.POST['faculty']
        department = request.POST['department']
        course_title = request.POST['course_title']
        course_code = request.POST['course_code']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if Lecturer.objects.filter(email=email).exists():
                messages.info(request='email exists')
            else:
                user = Lecturer.objects()
