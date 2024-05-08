from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Lecturer
from .serializers import LecturerSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

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

        if password1 == password2:
            if Lecturer.objects.filter(lecID=lecid).exists():
                return Response({'error': 'ID exists'}, status=status.HTTP_400_BAD_REQUEST)
            elif Lecturer.objects.filter(email=email).exists():
                return Response({'error': 'Email Taken'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                data["passwordd"] = password1
                serializer = LecturerSerializer(data=data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response({'message': email}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Passwords do not match.'}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        lecturers = Lecturer.objects.all() 
        serializer = LecturerSerializer(lecturers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)