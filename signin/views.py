# from rest_framework.views import APIView
# from rest_framework import status
# from rest_framework.response import Response
# from django.contrib.auth.hashers import check_password
# from signup.serializers import StudentSerializer
# from signup.models import Student

# # Create your views here.
# class StudentLogin(APIView):
#     def get(self, request, format=None):
        
#         queryset = Student.objects.all()
#         serializer = StudentSerializer(queryset, many=True)

#         return Response(serializer.data, status=status.HTTP_200_OK)


#     def post(self, request, format=None):
#         data = request.data
        
#         matric = data["matric_no"]
#         password = data["password"]

#         if not Student.objects.filter(matric_no__exact=matric).exists():
#             return Response("Invalid Matric Number", status=status.HTTP_400_BAD_REQUEST)
#         else:
#             student = Student.objects.filter(matric_no__exact=matric)
#             serializer = StudentSerializer(student)

#             if serializer.is_valid(raise_exception=True):
#                 studentData = serializer.data
#                 if check_password(studentData["password"]) == password:
#                     return Response("Works")
#                 else:
#                     return Response("Invalid password")

#     def check_password(self, hashed):
#         revealed = check_password(hashed)
#         return revealed

