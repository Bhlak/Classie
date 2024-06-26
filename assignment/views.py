from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Assignment
from rest_framework.permissions import AllowAny
from datetime import datetime
from .serializers import AssignmentSerializer


class assignmentAPI(APIView):
    permission_classes = ( AllowAny, )

    def post(self,request, format=None):
        data = request.data

        time = [int(a) for a in data["deadline"].split('-')]

        year = time[0]
        month = time[1]
        day = time[2]
        hour = time[3]
        minute = time[4]

        data["deadline"] = datetime(year, month, day, hour, minute)

        serializer = AssignmentSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response("IT workedddd", status=status.HTTP_200_OK)

        return Response("Shit worked", status=status.HTTP_200_OK)