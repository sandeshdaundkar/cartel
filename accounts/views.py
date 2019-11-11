from django.shortcuts import render
from .serializers import UserSerializer
from .models import User
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


# Create your views here.
class UserCreateListView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveUpdateDestroyAPI(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

