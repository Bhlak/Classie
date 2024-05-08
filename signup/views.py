import json
from rest_framework import status
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from django.contrib import messages
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

def register(request):
    if request.method == 'POST':
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
