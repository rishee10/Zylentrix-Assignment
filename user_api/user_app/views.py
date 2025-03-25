from django.shortcuts import render
from rest_framework import serializers
# Create your views here.

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer

class CreateUserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetAllUsersView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class GetUserView(APIView):
    def get(self,request,pk):
        user=User.objects.filter(id=pk).first()
        if user is None:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer=UserSerializer(user)
        return Response(serializer.data)
    
    # def get(self, request, pk):
    #     try:
    #         user = User.objects.get(pk=pk)
    #         serializer = UserSerializer(user)
    #         return Response(serializer.data)
    #     except User.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)

class UpdateUserView(APIView):
    def put(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class DeleteUserView(APIView):
    def delete(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
