from django.shortcuts import render
from rest_framework.response import Response
from .models import Comments, Announcements
from rest_framework.views import APIView
from signup.models import Student
from .serializers import AnnouncementsSerializer, CommentsSerializer
from rest_framework import status

class AnnouncementsAPIView(APIView):
    def get(self, request):
        announcements = Announcements.objects.all()
        serializer = AnnouncementsSerializer(announcements, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AnnouncementsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
class CommentsAPIView(APIView):
    def get(self, request):
        comments = Comments.objects.all()
        serializer = CommentsSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 