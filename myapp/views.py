from django.shortcuts import render
from rest_framework import generics
from .models import UserModel
from .serializers import UserSerializer

class CreateUser(generics.ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    
class UpdateAndDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
