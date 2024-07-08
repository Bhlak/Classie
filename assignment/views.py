from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Assignment
from course_list.models import Clist
from rest_framework.permissions import AllowAny
from datetime import datetime
from .serializers import AssignmentSerializer, SubmissionSerializer


class assignmentAPI(APIView):
    permission_classes = ( AllowAny, )

    def get(self, request, format=None):
        queryset = Assignment.objects.all()
        
        serializer = AssignmentSerializer(queryset, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request, format=None):
        data = request.data

        course_code = data.pop("course_code", "")
        dep_code = data.pop("dep_code", "")

        time = [int(a) for a in data["deadline"].split('-')]

        year = time[0]
        month = time[1]
        day = time[2]
        hour = time[3]
        minute = time[4]

        data["deadline"] = datetime(year, month, day, hour, minute)

        course = Clist.objects.get(course_code__exact=course_code, dep_code__exact=dep_code)
        
        data["course"] = course.id

        serializer = AssignmentSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response("IT workedddd", status=status.HTTP_200_OK)

        return Response("Problem Ser", status=status.HTTP_400_BAD_REQUEST)
    
class submissionAPI(APIView):
    permission_classes = ( AllowAny, )

    # def get(self, request, format=None):
    #     pass

    def post(self, request, format=None):
        data = request.data

        serializer = SubmissionSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response("Errorrrrr", status=status.HTTP_400_BAD_REQUEST)
        
