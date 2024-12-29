from rest_framework.views import APIView
from myproject.models.User import User as Users
from myproject.serializer import UserSerializer
from rest_framework.response import Response as APIResponse
from rest_framework import status

class UserListCreateAPIView(APIView):

    def get(self, request):
         users = Users.objects.all()
         serialized = UserSerializer(users, many=True)
         return APIResponse(serialized.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the new user to the database
            return APIResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return APIResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

