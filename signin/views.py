from django.contrib.auth import logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LoginSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from signup.serializers import CustomUserSerializer
from django.forms.models import model_to_dict

class StudentLogin(APIView):    
    permission_classes = (AllowAny, )
    def post(self, request, format=None):

        if request.user.is_authenticated:
            return Response("User already authenticated", status=status.HTTP_200_OK)
        
        data = request.data

        serializer = LoginSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)

        return Response({"token": token.key}, status=status.HTTP_200_OK)
        

class Logout(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        logout(request)
        return Response({"message": "User logged out"})

class Tester(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self, request, format=None):
        # serializer = CustomUserSerializer(data=request.user )
        # if serializer.is_valid(raise_exception=True):
        #     serializer.save()
        return Response({"res": model_to_dict(request.user)}['res']['full_name'])