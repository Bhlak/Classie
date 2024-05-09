import json
from rest_framework import status
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from .models import Lecturer


class SignUpView(APIView):
    def get(self, request, format=None):
        title = request.query_params.get("title", "")
        if title:
            queryset = Student.objects.filter(title__icontains=title)
        else:
            queryset = Student.objects.all()
        
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        try:
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        try:
            dat = request.data
            res = Student.objects.get(id__exact=dat['id'])
            serializer = StudentSerializer(res, data=dat)

            print(res.__dict__)

            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                print("nah")
                return Response(status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

class RegisterAPIView(APIView):
    def post(self,request, *args, **kwargs):
        # email = request.data['email']
        # faculty = request.data['faculty']
        # department = request.data['department']
        # course_title = request.data['course_title']
        # course_code = request.data['course_code']
        # password1 = request.data['passwordd']
        # password2 = request.data['passwordd']
        
        data = request.data
        
        email = data["email"]
        lecid = data["lecID"]
        password1 = data["password1"]
        password2 = data["password2"]
        hashedpassword = make_password(password1)
        if password1 == password2:
            if Lecturer.objects.filter(lecID=lecid).exists():
                return Response({'error': 'ID exists'}, status=status.HTTP_400_BAD_REQUEST)
            elif Lecturer.objects.filter(email=email).exists():
                return Response({'error': 'Email Taken'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                lec = Lecturer.objects.create(email=email, lecID=lecid, password=hashedpassword)
                lec.save()
                return Response({'message': data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Passwords do not match.'}, status=status.HTTP_400_BAD_REQUEST)

