import json
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response

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
