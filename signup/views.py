from rest_framework import status
from rest_framework.views import APIView
from .models import Student, CustomUser, Lecturer
from .serializers import StudentSerializer, CustomUserSerializer, LecturerSerializer
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import AllowAny, IsAdminUser
from course_list.models import Clist


# View to register a user - student or lecturer
class SignUpView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        queryset = CustomUser.objects.all()
        
        serializer = CustomUserSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        try:
            data = request.data

            if data['type'] == "student":

                email = data["email"]
                matric = data["matric_no"]


                if CustomUser.objects.filter(email__exact=email).exists():
                    return Response("Email already in use", status=status.HTTP_400_BAD_REQUEST)
                elif Student.objects.filter(matric_no__exact=matric).exists():
                    return Response("Matric Number already registered", status=status.HTTP_400_BAD_REQUEST)
                else:
                    # Hash the raw password
                    # raw_pwd = data['password']
                    # data['password'] = self.password_hash(raw_pwd)
                    serializer = CustomUserSerializer(data=data)
                    if serializer.is_valid(raise_exception=True):
                        serializer.save()
                        # if data['type'].lower() == "student":
                        #    data2['user'] = serializer.data
                        #    user = data2['user']
                        #    level = data2['level']
                        #    depart = data2['department']
                        #    faculty = data2['faculty']
                        #    matric = data2['matric_no']

                        #    studSer = Student.objects.create(user=user, level=level, department=depart, faculty=faculty, matric_no=matric)
                        #    studSer.save()
                        # elif data['type'] == "Lecturer":
                        #     Lecturer.objects.create(instance)
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
            elif data['type'] == "lecturer":
                email = data['email']
                lecID = data['lecID']

                if CustomUser.objects.filter(email__exact=email).exists():
                    return Response({'error': 'Email Taken'}, status=status.HTTP_400_BAD_REQUEST)
                elif Lecturer.objects.filter(lecID__exact=lecID).exists():
                    return Response({'error': 'Leturer ID exists'}, status=status.HTTP_400_BAD_REQUEST)
                else:

                    serializer = CustomUserSerializer(data=data)
                    if serializer.is_valid(raise_exception=True):
                        serializer.save()
                        return Response({'message': email}, status=status.HTTP_201_CREATED)
            else:
                raise ValueError("Invalid User Type")
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
        
    # def password_hash(self, raw):
    #     try:
    #         hashed_pwd = make_password(raw)
    #     except Exception as e:
    #         print(f"Error encountered: {e}")
    #         return None
    #     return hashed_pwd


# Views for courses a lecturer is teaching
class LecturerCourseView(APIView):
    permission_classes = ( AllowAny, )

    def post(self, request, format=None):
        try:
            data = request.data

            department = data['department']
            course_code = data['course']

            # course = Clist.objects.filter()


        
        except Exception as e:
            return Response({"message": e}, status=status.HTTP_400_BAD_REQUEST)



# # class RegisterAPIView(APIView):
# #     def post(self,request, *args, **kwargs):
        
# #         email = data["email"]
# #         lecid = data["lecID"]
# #         password1 = data["password1"]
# #         password2 = data["password2"]

# #         if password1 == password2:
            # if Lecturer.objects.filter(lecID=lecid).exists():
            #     return Response({'error': 'ID exists'}, status=status.HTTP_400_BAD_REQUEST)
            # elif Lecturer.objects.filter(email=email).exists():
            #     return Response({'error': 'Email Taken'}, status=status.HTTP_400_BAD_REQUEST)
# #             else:
# #                 user = Lecturer.objects()

# #                 data["passwordd"] = password1
                # serializer = LecturerSerializer(data=data)
                # if serializer.is_valid(raise_exception=True):
                #     serializer.save()
                #     return Response({'message': email}, status=status.HTTP_201_CREATED)
# #         else:
# #             return Response({'message': 'Passwords do not match.'}, status=status.HTTP_400_BAD_REQUEST)

# #     def get(self, request, *args, **kwargs):
# #         lecturers = Lecturer.objects.all() 
# #         serializer = LecturerSerializer(lecturers, many=True)
# #         return Response(serializer.data, status=status.HTTP_200_OK)