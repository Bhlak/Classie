from rest_framework import status
from rest_framework.views import APIView
from .models import Classes
from .serializers import ClassSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class ClassAPI(APIView):
    permission_classes = (AllowAny, )
    def post(self, request, format=None):
        data = request.data

        try:

            if Classes.objects.filter(code__exact=data['code']).exists():
                the_class = Classes.objects.get(code__exact=data['code'])
                serializer = ClassSerializer(the_class)
                print("Already created")
                return Response({"Class": serializer.data}, status=status.HTTP_200_OK)
            serializer = ClassSerializer(data=data)

            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({"Grrrrrrrrr"}, status=status.HTTP_200_OK)
        except Exception as e:
            print(f'Error Encountered her: {e}')
            return Response(e, status=status.HTTP_409_CONFLICT)

        # return Response({"Working"}, status=status.HTTP_200_OK)
