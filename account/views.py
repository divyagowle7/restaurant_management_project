from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializers import UserProfileSerializer
# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserProfileSerializer
    permission_class=[IsAuthenticated]

    def get_object(self):
        return self.request.user

    def update(self,request.*args,**kwargs):
        partial=True
        instance=self.get_object()
        serializer=self.get_serializer(instance,data=request.data,partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        

