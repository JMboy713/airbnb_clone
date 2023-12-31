from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import PrivateUserSerializer
from rest_framework.exceptions import ParseError

class Me(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = PrivateUserSerializer(user).data
        return Response(serializer)

    def put(self, request):
        user = request.user
        serializer = PrivateUserSerializer(
            user,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            user=serializer.save()
            serializer=PrivateUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
class Users(APIView):
    def post(self,request):
        password=request.data.get('password')
        if not password:
            raise ParseError 
        
        serializer=PrivateUserSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            user.set_password(password)
            user.save()
            serializer=PrivateUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    