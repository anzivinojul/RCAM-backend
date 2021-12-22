from django.shortcuts import render
from rest_framework import permissions

from .serializers import MyTokenObtainPairSerializer, RegisterSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class UserAPIView(generics.RetrieveAPIView):
    permissions_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user    

#class UserDetail(generics.RetrieveAPIView):
#    queryset = User.objects.all()
#    permissions_classes = (AllowAny,)
#    serializer_class = UserSerializer

#class UserList(generics.ListAPIView):
#    queryset = User.objects.all()
#    permissions_classes = (AllowAny,)
#    serializer_class = UserAllSerializer